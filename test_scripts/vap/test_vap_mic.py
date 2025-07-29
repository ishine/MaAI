"""
This script is an example of how to use the VapGPT model.
"""

import sys
import os

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/')))

from maai import Maai, MaaiInput, MaaiOutput

def test_vap():

    output = MaaiOutput.ConsoleBar()

    maai = Maai(
        mode="vap",
        language="jp",
        frame_rate=10,
        context_len_sec=5,
        audio_ch1=MaaiInput.Mic(),
        audio_ch2=MaaiInput.Zero(),
        device="cpu",
        force_download=True
    )

    maai.start_process()

    while True:
        result = maai.get_result()
        output.update(result)
        
if __name__ == "__main__":
    try:
        test_vap()
    except KeyboardInterrupt:
        print("Ending the test script.")