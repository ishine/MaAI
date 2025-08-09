"""
This script is an example of using a single microphone with the nodding model.
"""

import sys
import os

# For debugging purposes, you can uncomment the following line to add the src directory to the path.
# This allows you to import modules from the src directory without pip installing the package.
# Uncomment the line below if you need to run this script directly without installing the package.

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/')))

from maai import Maai, MaaiInput, MaaiOutput

def test():

    # Use the default mic
    mic = MaaiInput.Mic()

    # Use zero signals for the second channel
    zero = MaaiInput.Zero()

    output = MaaiOutput.ConsoleBar()

    maai = Maai(
        mode="nod",
        language="jp",
        frame_rate=10,
        context_len_sec=5,
        audio_ch1=mic,
        audio_ch2=zero,
        device="cpu"
    )

    maai.start()

    while True:
        result = maai.get_result()
        output.update(result)
        
if __name__ == "__main__":
    try:
        test()
    except KeyboardInterrupt:
        print("Ending the test script.")