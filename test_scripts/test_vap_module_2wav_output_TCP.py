#!/usr/bin/env python3
"""
VAPモデルのテストスクリプト
WAVファイルを使用してVAPモデルの動作を確認してコンソール上に可視化します
"""

import sys
import os

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from maai import Maai, MaaiInput, MaaiOutput

wav_file_path1 = "../input/wav_sample/jpn_inoue_16k.wav"
wav_file_path2 = "../input/wav_sample/jpn_sumida_16k.wav"

frame_rate = 10
context_len_sec = 5

def test_vap_with_console():
    """VAPモデルをコンソール出力でテスト"""
    
    mode = "vap"
    vap = Maai(
        mode=mode,
        frame_rate=frame_rate,
        context_len_sec=context_len_sec,
        audio_ch1=MaaiInput.Wav(wav_file_path=wav_file_path1),
        audio_ch2=MaaiInput.Wav(wav_file_path=wav_file_path2),
        device="cpu"
    )
    output_tcp_transmitter = MaaiOutput.TCPTransmitter(ip="127.0.0.1", port=50008, mode=mode)
    output_tcp_transmitter.start_server()
    
    vap.start_process()
    
    while True:
        result = vap.get_result()
        
        output_tcp_transmitter.update(result)

if __name__ == "__main__":
    test_vap_with_console()