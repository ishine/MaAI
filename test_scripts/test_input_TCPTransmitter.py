import sys
import os
import time

# Add the src directory to the Python path to allow importing local modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from maai import MaaiInput  # Import MaaiInput class from maai module

# Print available microphone devices for reference
MaaiInput.available_mic_devices()

# Define TCP connection parameters for two transmitters
TCP_IP1 = "127.0.0.1"      # IP address for first transmitter
TCP_PORT1 = 12345          # Port for first transmitter
TCP_IP2 = "127.0.0.1"      # IP address for second transmitter
TCP_PORT2 = 12346          # Port for second transmitter

# Create TCPTransmitter instances for two microphones
mic1_transmitter = MaaiInput.TCPTransmitter(ip=TCP_IP1, port=TCP_PORT1, mic_device_index=0)  # First mic transmitter
mic2_transmitter = MaaiInput.TCPTransmitter(ip=TCP_IP2, port=TCP_PORT2, mic_device_index=0)  # Second mic transmitter

# Start the transmission processes for both microphones
mic1_transmitter.start_process()
mic2_transmitter.start_process()

# Keep the script running to maintain transmission
while True:
    time.sleep(1)  # Sleep to prevent busy-waiting