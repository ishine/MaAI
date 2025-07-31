
<p align="center">
<img src="img/logo_ver2.png" width="300">
</p>


<h1>
<p align="center">
MaAI
</p>
    
<p align="center">
<img src="https://img.shields.io/pypi/v/maai" alt="PyPI - Version">
</p>
</h1>

<p align="center">A <b>Real-time</b> and <b>Light-weight</b> Software for Generation of <b>Non-Linguistic</b> Behavior Generations for Conversational AIs</p>
<p align="center">(Real-time Implementation of Voice Activity Projection)</p>
<p align="center">
📄 README: <a href="README.md">English </a> | <a href="README_JP.md">Japanese (日本語) </a>
</p>

<b>MaAI</b> is a state-of-the-art and light-weight software that can generate (predict) non-linguistic behaviors in real time and continuously.
It supports essential interaction elements such as <b>(1) Turn-Taking</b>, <b>(2) Backchanneling</b>, and <b>(3) Head Nodding</b>.
Currently available for English, Chinese, and Japanese languages, MaAI will continue to expand its language coverage and non-linguistic behavior repertoire in the future.
Designed specifically for conversational AI, including spoken dialogue systems and interactive robots, MaAI handles audio input effectively in either two-channels (user-system) or single-channel (user-only) settings. 🎙️
Thanks to its lightweight design, MaAI operates efficiently, even exclusively on CPU hardware. ⚡

The name <b>MaAI</b> is derived from the Japanese words <b>Ma(間)</b> or <b>Maai(間合い)</b>, which refer to the subtle timing and spacing that humans adjust using various modalities during interactions.  
The <b>AI</b> in MaAI literally stands for Artificial Intelligence, reflecting the aim to develop AI technologies related to these interactional dynamics.

The currently supported models are mainly based on the Voice Activity Projection (VAP) model and its extensions.
Details about the VAP model can be found in the following repository:
https://github.com/ErikEkstedt/VoiceActivityProjection

For <b>system development or collaborative research using MaAI software</b>, please contact [Koji Inoue](https://inokoj.github.io/) at Kyoto University.

<br>

__Demo video on YouTube__ (https://www.youtube.com/watch?v=-uwB6yl2WtI)

[![Demo video](http://img.youtube.com/vi/-uwB6yl2WtI/0.jpg)](https://www.youtube.com/watch?v=-uwB6yl2WtI)

<br>

## 🆕 Update

- We launched the MaAI project and repository here! 🚀  (July 24th, 2025)

<br>

## 🚀 Getting Started

To quickly get started with MaAI, you can install it using pip:

```bash
pip install maai
```

> 💡 **Note:** By default, the CPU version of PyTorch will be installed. If you wish to run MaAI on a GPU, please install the GPU version of PyTorch that matches your CUDA environment before proceeding.

You can run it as follows. 🏃‍♂️
The appropriate model for the task (mode) and parameters will be downloaded automatically.  
Below is an example of using the turn-taking model (VAP) with the first channel as microphone input (user) and the second channel as silence (system).

```python
from maai import Maai, MaaiInput, MaaiOutput

mic = MaaiInput.Mic()
zero = MaaiInput.Zero() 

maai = Maai(mode="vap", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=mic, audio_ch2=zero, device="cpu")
maai_output_bar = MaaiOutput.ConsoleBar(bar_type="balance")

maai.start_process()
while True:
    result = maai.get_result()
    maai_output_bar.update(result)
```

<br>

## 🧩 Models

We support the following models (behavior, language, audio setting, etc.), and more models will be added in the future.
Currently available models can be found in [our HuggingFace repository](https://huggingface.co/maai-kyoto).

### Turn-Taking

The turn-taking model uses the original VAP as is and predicts which participant will speak in the next moment.

- [VAP Model](readme/vap.md)
- [Noise-Robust VAP Model (<b>Recommended</b>)](readme/vap_mc.md)
- [Single-Channel VAP Model] (In Preparation ...)

### Backchannel

Backchannels are short listener responses such as `yeah` and `oh`, that are also related to turn-taking.

- [VAP-based Backchannel Prediction Model - Timing for Two types](readme/vap_bc_2type.md)
- [VAP-based Backchannel Prediction Model - Timing Only] (In Preparation ...)

### Nodding

Nodding refers to the up-and-down movement of the head and is closely related to backchanneling. Unlike backchannels that involve vocal responses, nodding allows the listener to express their reaction non-verbally.

- [VAP-based Nodding Prediction Model](readme/vap_nod.md)

<br>

## 🎚️ Input / Output

For input to the MaAI model, you can directly call the `process` method of a `Maai` class instance.  
The `MaaiInput` class also provides flexible input options, supporting audio from WAV files, microphone input, and TCP communication.

- WAV file input: `Wav` class 📁
- Microphone input: `Mic` class 🎙️
- TCP communication: `TCPReceiver` / `TCPTransmitter` classes 🌐
- Chunk input: `Chunk` class 📦

By using these classes, you can easily adapt the audio input method to your specific use case.

For output, you can retrieve the processing results using the `get_result` method of the `Maai` class instance.
The `MaaiOutput` class also supports several ways of visualization and also TCP communication.

- Console Dynamic Output: `ConsoleBar` class 📊
- GUI bar graph output: `GuiBar` class 🖼️
- GUI plot output: `GuiPlot` class 📈
- TCP communication: `TCPReceiver` / `TCPTransmitter` classes 🌐

For more details, please refer to the following README files:
- [Input Readme](readme/input.md)
- [Output Readme](readme/output.md)

<br>

## 💡 Example Implementation

You can find example implementations of MaAI models in the [test_scripts](test_scripts) directory of this repository.

- Turn-Taking (VAP)
    - [With 2 wav file inputs](test_scripts/test_vap_module_2wav.py) 🎧
    - [With 2 mic inputs](test_scripts/test_vap_module_2mic.py) 🎤
    - [With 2 mic inputs via TCP networks](test_scripts/test_vap_module_2tcp.py) 🌐
    - [With 1 wav file and 1 mic input](test_scripts/test_vap_module_wav_mic.py) 🎧🎤

- Backchannel
    - [With 1 mic input and silence](test_scripts/test_vap_bc_2type_mic.py) 🎤

- Nodding
    - [With 1 wav file and 1 mic input](test_scripts/test_vap_nod_module_wav_mic.py) 🎧🎤

- Input/Output
 - TBA

<br>

## 📚 Publication

Please cite the following paper, if you made any publications made with this repository. 🙏

Koji Inoue, Bing'er Jiang, Erik Ekstedt, Tatsuya Kawahara, Gabriel Skantze<br>
__Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection__<br>
International Workshop on Spoken Dialogue Systems Technology (IWSDS), 2024<br>
https://arxiv.org/abs/2401.04868<br>

```
@inproceedings{inoue2024iwsds,
    author = {Koji Inoue and Bing'er Jiang and Erik Ekstedt and Tatsuya Kawahara and Gabriel Skantze},
    title = {Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection},
    booktitle = {International Workshop on Spoken Dialogue Systems Technology (IWSDS)},
    year = {2024},
    url = {https://arxiv.org/abs/2401.04868},
}
```


If you use the multi-lingual VAP model, please also cite the following paper.

Koji Inoue, Bing'er Jiang, Erik Ekstedt, Tatsuya Kawahara, Gabriel Skantze<br>
__Multilingual Turn-taking Prediction Using Voice Activity Projection__<br>
Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING), pages 11873-11883, 2024<br>
https://aclanthology.org/2024.lrec-main.1036/<br>

```
@inproceedings{inoue2024lreccoling,
    author = {Koji Inoue and Bing'er Jiang and Erik Ekstedt and Tatsuya Kawahara and Gabriel Skantze},
    title = {Multilingual Turn-taking Prediction Using Voice Activity Projection},
    booktitle = {Proceedings of the Joint International Conference on Computational Linguistics and Language Resources and Evaluation (LREC-COLING)},
    pages = {11873--11883},
    year = {2024},
    url = {https://aclanthology.org/2024.lrec-main.1036/},
}
```

If you also use the noise-robusst VAP model, please also cite the following paper.

Koji Inoue, Yuki Okafuji, Jun Baba, Yoshiki Ohira, Katsuya Hyodo, Tatsuya Kawahara<br>
__A Noise-Robust Turn-Taking System for Real-World Dialogue Robots: A Field Experiment__<br>
https://www.arxiv.org/abs/2503.06241<br>

```
@misc{inoue2025noisevap,
    author = {Koji Inoue and Yuki Okafuji and Jun Baba and Yoshiki Ohira and Katsuya Hyodo and Tatsuya Kawahara},
    title = {A Noise-Robust Turn-Taking System for Real-World Dialogue Robots: A Field Experiment},
    year = {2025},
    note = {arXiv:2503.06241},
    url = {https://www.arxiv.org/abs/2503.06241},
}
```

If you also use the backchannel VAP model, please also cite the following paper.

Koji Inoue, Divesh Lala, Gabriel Skantze, Tatsuya Kawaharaa<br>
__Yeah, Un, Oh: Continuous and Real-time Backchannel Prediction with Fine-tuning of Voice Activity Projection__<br>
https://aclanthology.org/2025.naacl-long.367/<br>

```
@inproceedings{inoue2025vapbc,
    author = {Koji Inoue and Divesh Lala and Gabriel Skantze and Tatsuya Kawahara},
    title = {Yeah, Un, Oh: Continuous and Real-time Backchannel Prediction with Fine-tuning of Voice Activity Projection},
    booktitle = {Proceedings of the Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
    pages = {7171--7181},
    year = {2025},
    url = {https://aclanthology.org/2025.naacl-long.367/},
}
```

<br>

## 📝 License

The source code in this repository is licensed under the MIT license.
The trained models are used for only academic purposes.

The pre-trained CPC model is from the original CPC project and please follow its specific license.
Refer to the original repository at https://github.com/facebookresearch/CPC_audio for more details.
