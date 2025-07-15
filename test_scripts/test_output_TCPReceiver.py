import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from maai import MaaiOutput

TCP_IP1 = "127.0.0.1"
TCP_PORT1 = 50008

output_tcp_receiver = MaaiOutput.TCPReceiver(ip=TCP_IP1, port=TCP_PORT1, mode="vap")
output_tcp_receiver.start_process()

maai_output_bar = MaaiOutput.Console_bar(bar_type="balance")

while True:
    result = output_tcp_receiver.get_result()
    
    maai_output_bar.update(result)