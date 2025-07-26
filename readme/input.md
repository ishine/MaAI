<h1>
<p align="center">
How to use the <b>MaaiInput</b> module
</p>
</h1>
<p align="center">
README: <a href="input.md">English </a> | <a href="input_JP.md">Japanese (日本語) </a>
</p>

MaaiInput (`input.py`) is a module for flexible handling of audio input in MaAI.
It supports audio input via WAV files, microphone, and TCP communication.

## Class List

- `Mic`: Microphone input (real-time)
- `Wav`: WAV file input
- `TCPReceiver`: Receive audio data via TCP
- `TCPTransmitter`: Transmit microphone audio data via TCP
- `Zero`: Generates silent (zero-filled) audio data (intended for temporarily filling system-side audio)

### Basic Usage

#### WAV File Input
```python
from maai import MaaiInput

wav1 = MaaiInput.Wav(wav_file_path="user.wav")
wav2 = MaaiInput.Wav(wav_file_path="system.wav")
```

#### Microphone Input
```python
mic1 = MaaiInput.Mic(mic_device_index=0)
mic2 = MaaiInput.Mic(mic_device_index=1)
```

#### TCP Input
```python
tcp_receiver = MaaiInput.TCPReceiver(ip="0.0.0.0", port=12345)
tcp_receiver.start_server()
```

#### TCP Transmission
```python
tcp_transmitter = MaaiInput.TCPTransmitter(ip="Destination IP", port=12345, mic_device_index=0)
tcp_transmitter.start_process()
```

#### Silent (Zero-filled) Input
```python
zero_input = MaaiInput.Zero()
```

## TCP Audio Data Format

When connecting with your own original system, send audio data to an instance of the `TCPReceiver` class. The data format is as follows:

- Sampling rate: 16,000 Hz
- 1 frame: 160 samples
- Each sample: 8-byte double-precision floating point (double, little endian, -1.0 to +1.0)
- 1 frame data size: 1,280 bytes

### Data Packet Example

| Byte Offset | Data Type | Description |
| ---- | ---- | --- |
| 0 - 7 | Double | Audio Data - Sample 1 |
| 8 - 15 | Double | Audio Data - Sample 2 |
| ... | ... | ... |
| 1264 - 1271 | Double | Audio Data - Sample 159 |
| 1272 - 1279 | Double | Audio Data - Sample 160 |

## Get Device List

You can get a list of microphone devices with `available_mic_devices()`.

```python
from maai import MaaiInput

MaaiInput.available_mic_devices()
```

## Notes

- Only 16,000Hz WAV files are supported
- TCP communication sends/receives audio data for two people per frame
- Each class starts asynchronous processing with `start_process()`

---

For more details, please refer to [README.md](../README.md).
