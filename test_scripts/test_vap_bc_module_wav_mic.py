#!/usr/bin/env python3
"""
Test script for the VAP backchannel model.
Channel 1 (user): microphone input.
Channel 2 (system): silence.
This script verifies the operation of the VAP backchannel model and visualizes p_bc_react and p_bc_emo as bars.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from maai import Maai, MaaiInput, MaaiOutput

def test_vap_bc_with_bar():
    
    MaaiInput.available_mic_devices()
    mic = MaaiInput.Mic(mic_device_index=0)  # Use the first microphone device
    zero = MaaiInput.Zero()  # Use silence for the second channel

    vap = Maai(mode="bc_2type", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=mic, audio_ch2=zero, device="cpu")
    
    bar = MaaiOutput.ConsoleBar(bar_length=30, bar_type="normal")
    vap.start_process()
    
    while True:
        result = vap.get_result()
        bar.update(result)
        
if __name__ == "__main__":
    test_vap_bc_with_bar()
