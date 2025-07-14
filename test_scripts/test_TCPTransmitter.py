import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from maai import VapInput

VapInput.available_mic_devices()

TCP_IP1 = "127.0.0.1"
TCP_PORT1 = 12345
TCP_IP2 = "127.0.0.1"
TCP_PORT2 = 12346

mic1_transmitter = VapInput.TCPTransmitter(ip=TCP_IP1, port=TCP_PORT1, mic_device_index=1)
mic2_transmitter = VapInput.TCPTransmitter(ip=TCP_IP2, port=TCP_PORT2, mic_device_index=1)
mic1_transmitter.start_process()
mic2_transmitter.start_process()

while True:
    time.sleep(1)