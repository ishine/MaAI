import torch
import torch.nn as nn
from torch import Tensor
from typing import Optional, Tuple
import torch.nn.functional as F

from .config import VapConfig
from ..encoder import EncoderCPC
from ..modules import GPT, GPTStereo
from ..objective import ObjectiveVAP

class VapGPT_prompt(nn.Module):
    
    def __init__(self, conf: Optional[VapConfig] = None):
        super().__init__()
        if conf is None:
            conf = VapConfig()
        self.conf = conf
        self.sample_rate = conf.sample_rate
        self.frame_hz = conf.frame_hz

        self.temp_elapse_time = []

        # Single channel
        self.ar_channel = GPT(
            dim=conf.dim,
            dff_k=3,
            num_layers=conf.channel_layers,
            num_heads=conf.num_heads,
            dropout=conf.dropout,
            context_limit=conf.context_limit,
        )

        # Cross channel
        self.ar = GPTStereo(
            dim=conf.dim,
            dff_k=3,
            num_layers=conf.cross_layers,
            num_heads=conf.num_heads,
            dropout=conf.dropout,
            context_limit=conf.context_limit,
        )

        self.objective = ObjectiveVAP(bin_times=conf.bin_times, frame_hz=conf.frame_hz)

        # Outputs
        # Voice activity objective -> x1, x2 -> logits ->  BCE
        self.va_classifier = nn.Linear(conf.dim, 1)
        self.vap_head = nn.Linear(conf.dim, self.objective.n_classes)
        self.prompt_head = nn.Linear(conf.dim, conf.dim_prompt)

        self.prompt_embed1 = nn.Linear(self.conf.dim_prompt, self.conf.dim_prompt_2)
        self.prompt_embed2 = nn.Linear(self.conf.dim_prompt, self.conf.dim_prompt_2)

        self.prompt_dim_red1 = nn.Linear(self.conf.dim + self.conf.dim_prompt_2, self.conf.dim)
        self.prompt_dim_red2 = nn.Linear(self.conf.dim + self.conf.dim_prompt_2, self.conf.dim)

    def load_encoder(self, cpc_model):
        
        # Audio Encoder
        #if self.conf.encoder_type == "cpc":
        self.encoder1 = EncoderCPC(
            load_pretrained=True if self.conf.load_pretrained == 1 else False,
            freeze=self.conf.freeze_encoder,
            cpc_model=cpc_model
        )
        self.encoder1 = self.encoder1.eval()
        #print(self.encoder1)
        #self.encoder1 = self.encoder1.half()
        
        self.encoder2 = EncoderCPC(
            load_pretrained=True if self.conf.load_pretrained == 1 else False,
            freeze=self.conf.freeze_encoder,
            cpc_model=cpc_model
        )

        self.encoder2 = self.encoder2.eval()
        #self.encoder2 = self.encoder2.half()
        
        if self.conf.freeze_encoder == 1:
            print('freeze encoder')
            self.encoder1.freeze()
            self.encoder2.freeze()

    @property
    def horizon_time(self):
        return self.objective.horizon_time

    def encode_audio(self, audio1: torch.Tensor, audio2: torch.Tensor) -> Tuple[Tensor, Tensor]:
        
        x1 = self.encoder1(audio1)  # speaker 1
        x2 = self.encoder2(audio2)  # speaker 2
        
        return x1, x2

    def vad_loss(self, vad_output, vad):
        return F.binary_cross_entropy_with_logits(vad_output, vad)
    
    def set_prompt_ch1(self, prmpt: str):

        pass

    def set_prompt_ch2(self, prmpt: str):

        pass

    def forward(self, x1: Tensor, x2: Tensor) -> Tuple[Tensor, Tensor, list[Tensor]]:
        """
        Forward pass for the VapGPT model.
        
        Args:
            x1 (Tensor): Input audio tensor for speaker 1.
            x2 (Tensor): Input audio tensor for speaker 2.
        
        Returns:
            Tuple[Tensor, Tensor, list[Tensor]]: Output tensors and additional information.
        """
        
        # Encode audio
        x1, x2 = self.encode_audio(x1, x2)

        # Channel swap for temporal consistency
        x1_context_ = self.ar_channel(x1)