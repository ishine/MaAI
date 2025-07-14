#!/usr/bin/env python3
"""
VAPモデルのテストスクリプト
TCPで受信した音声データをVAPモデルに入力し、動作を確認します
"""

import sys
import os
import numpy as np
import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from matplotlib import animation
import threading

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from maai import Vap, VapInput

frame_rate = 5
context_len_sec = 3

def test_vap_with_gui():
    global wav1, wav2, p_ns, p_ft, p_react, p_emo

    # TCP受信の設定
    TCP_IP1 = "127.0.0.1"
    TCP_PORT1 = 12345
    TCP_IP2 = "127.0.0.1"
    TCP_PORT2 = 12346
    
    mic1_receiver = VapInput.TCPReceiver(ip=TCP_IP1, port=TCP_PORT1)
    mic2_receiver = VapInput.TCPReceiver(ip=TCP_IP2, port=TCP_PORT2)
    
    mic1_receiver.start_server()
    mic2_receiver.start_server()
    
    vap = Vap(
        mode="vap",
        frame_rate=frame_rate,
        context_len_sec=context_len_sec,
        mic1=mic1_receiver,
        mic2=mic2_receiver,
        device="cpu"
    )
    vap_bc = Vap(
        mode="bc",
        frame_rate=frame_rate,
        context_len_sec=context_len_sec,
        mic1=mic1_receiver,
        mic2=mic2_receiver,
    )

    vap.start_process()
    vap_bc.start_process()

    while True:
        result = vap.get_result()
        result_bc = vap_bc.get_result()

        x1 = result['x1']
        wav1 = np.append(wav1, x1)
        wav1 = wav1[-MAX_CONTEXT_WAV_LEN:]

        x2 = result['x2']
        wav2 = np.append(wav2, x2)
        wav2 = wav2[-MAX_CONTEXT_WAV_LEN:]

        p_ns = np.append(p_ns, result['p_now'][0])
        p_ns = p_ns[-MAX_CONTEXT_LEN:]

        p_ft = np.append(p_ft, result['p_future'][0])
        p_ft = p_ft[-MAX_CONTEXT_LEN:]

        # バックチャンネル出力
        p_react = np.append(p_react, result_bc['p_bc_react'][0])
        p_react = p_react[-MAX_CONTEXT_LEN:]
        p_emo = np.append(p_emo, result_bc['p_bc_emo'][0])
        p_emo = p_emo[-MAX_CONTEXT_LEN:]

if __name__ == "__main__":

    SHOWN_CONTEXT_LEN_SEC = 10
    SAMPLE_RATE = 16000
    SAMPE_VAP_RATE = frame_rate

    MAX_CONTEXT_LEN = SAMPE_VAP_RATE * SHOWN_CONTEXT_LEN_SEC
    MAX_CONTEXT_WAV_LEN = SAMPLE_RATE * SHOWN_CONTEXT_LEN_SEC

    def animate(frame_index):
        ax1_sub.set_data(time_x1, wav1)
        ax2_sub.set_data(time_x2, wav2)

        ax3_sub1 = ax3.fill_between(
            time_x3, y1=0.5, y2=p_ns, where=p_ns > 0.5, color='y')
        ax3_sub2 = ax3.fill_between(
            time_x3, y1=p_ns, y2=0.5, where=p_ns < 0.5, color='b')

        ax4_sub1 = ax4.fill_between(
            time_x4, y1=0.5, y2=p_ft, where=p_ft > 0.5, color='y')
        ax4_sub2 = ax4.fill_between(
            time_x4, y1=p_ft, y2=0.5, where=p_ft < 0.5, color='b')

        ax5_sub1 = ax5.fill_between(
            time_x5, y1=0.0, y2=p_react, color='tomato')
        ax5.axhline(y=0.5, color='black', linestyle='--')

        ax6_sub1 = ax6.fill_between(
            time_x6, y1=0.0, y2=p_emo, color='violet')
        ax6.axhline(y=0.5, color='black', linestyle='--')

        return ax1_sub, ax2_sub, ax3_sub1, ax3_sub2, ax4_sub1, ax4_sub2, ax5_sub1, ax6_sub1

    root = tkinter.Tk()
    root.wm_title("Real-time VAP + BC demo (TCP input)")

    fig, ax = plt.subplots(6, 1, tight_layout=True, figsize=(18,18))

    # Wave 1
    ax1 = ax[0]
    ax1.set_title('Input waveform 1 (TCP)')
    ax1.set_xlabel('Time [s]')
    time_x1 = np.linspace(-SHOWN_CONTEXT_LEN_SEC, 0, MAX_CONTEXT_WAV_LEN)
    wav1 = np.zeros(len(time_x1))
    ax1.set_ylim(-1, 1)
    ax1.set_xlim(-SHOWN_CONTEXT_LEN_SEC, 0)
    ax1_sub, = ax1.plot(time_x1, wav1, c='y')

    # Wave 2
    ax2 = ax[1]
    ax2.set_title('Input waveform 2 (TCP)')
    ax2.set_xlim(-SHOWN_CONTEXT_LEN_SEC, 0)
    ax2.set_xlabel('Time [s]')
    time_x2 = np.linspace(-SHOWN_CONTEXT_LEN_SEC, 0, MAX_CONTEXT_WAV_LEN)
    wav2 = np.zeros(len(time_x2))
    ax2.set_ylim(-1, 1)
    ax2_sub, = ax2.plot(time_x2, wav2, c='b')

    # p_now
    ax3 = ax[2]
    ax3.set_title('Output p_now (short-term turn-taking prediction)')
    ax3.set_xlabel('Sample')
    ax3.set_xlim(0, MAX_CONTEXT_LEN)
    ax3.set_ylim(0, 1)
    time_x3 = np.linspace(0, MAX_CONTEXT_LEN, MAX_CONTEXT_LEN)
    p_ns = np.ones(len(time_x3)) * 0.5

    # p_future
    ax4 = ax[3]
    ax4.set_title('Output p_future (long-term turn-taking prediction)')
    ax4.set_xlabel('Sample')
    ax4.set_xlim(0, MAX_CONTEXT_LEN)
    ax4.set_ylim(0, 1)
    time_x4 = np.linspace(0, MAX_CONTEXT_LEN, MAX_CONTEXT_LEN)
    p_ft = np.ones(len(time_x4)) * 0.5

    # p_react
    ax5 = ax[4]
    ax5.set_title('Output p_bc_react (reactive backchannel prediction)')
    ax5.set_xlabel('Sample')
    ax5.set_xlim(0, MAX_CONTEXT_LEN)
    ax5.set_ylim(0, 1)
    time_x5 = np.linspace(0, MAX_CONTEXT_LEN, MAX_CONTEXT_LEN)
    p_react = np.ones(len(time_x5)) * 0.0

    # p_emo
    ax6 = ax[5]
    ax6.set_title('Output p_bc_emo (emotional backchannel prediction)')
    ax6.set_xlabel('Sample')
    ax6.set_xlim(0, MAX_CONTEXT_LEN)
    ax6.set_ylim(0, 1)
    time_x6 = np.linspace(0, MAX_CONTEXT_LEN, MAX_CONTEXT_LEN)
    p_emo = np.ones(len(time_x6)) * 0.0

    ani = animation.FuncAnimation(
        fig,
        animate,
        interval=250,
        blit=True
    )

    # matplotlib を GUI(Tkinter) に追加する
    canvas = FigureCanvasTkAgg(fig, master=root)
    toolbar = NavigationToolbar2Tk(canvas, root)
    canvas.get_tk_widget().pack()

    thread_vap = threading.Thread(target=test_vap_with_gui, daemon=True)
    thread_vap.start()

    tkinter.mainloop() 