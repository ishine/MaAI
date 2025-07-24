#!/usr/bin/env python3
"""
Test script for the VAP backchannel model.
Channel 1 (user): microphone input.
Channel 2 (system): silence.
This script verifies the operation of the VAP backchannel model and visualizes p_bc_react and p_bc_emo as bars.
"""

import sys, os

# For debugging
# Add the src directory to the path to allow importing the maai module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from maai import Maai, MaaiInput, MaaiOutput

# Test function for the VAP backchannel model
# Uses microphone input and silent input, and visualizes the results as bars

def test_vap_bc_with_bar():

    # Show available microphone devices (for debugging)
    MaaiInput.available_mic_devices()
    
    # Select the first microphone device
    mic = MaaiInput.Mic(device_name='マイク (Logicool Webcam C925e)')  # Use the default microphone device
    
    # Use silence for the second channel
    zero = MaaiInput.Zero()  # Use silence for the second channel

    # Create an instance of the VAP model
    # mode: bc_2type (two types of backchannel), Japanese, frame rate 10Hz, context length 5 seconds, CPU
    vap = Maai(mode="bc_2type", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=mic, audio_ch2=zero, device="cpu")
    
    # Create an output instance for bar visualization (console bar with length 30)
    # bar = MaaiOutput.ConsoleBar(bar_length=30, bar_type="normal")
    bar = MaaiOutput.GuiBar(bar_type="normal")
    
    # Start the VAP model process
    vap.start_process()
    
    # Continuously get results and update the bar
    while True:
        result = vap.get_result()  # Get inference result from the model
        bar.update(result)         # Update the bar visualization
        # Can be stopped with Ctrl+C
        
if __name__ == "__main__":
    # Call the test function when the script is executed directly
    test_vap_bc_with_bar()
