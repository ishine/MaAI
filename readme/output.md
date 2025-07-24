<h1>
<p align="center">
How to use the <b>MaaiOutput</b> module
</p>
</h1>
<p align="center">
README: <a href="output.md">English </a> | <a href="output_JP.md">Japanese (日本語) </a>
</p>

MaaiOutput (`output.py`) is a module for handling the output of MaAI.
It provides features to visualize inference results such as turn-taking, backchanneling, and nodding as bar graphs, and to send or receive these results via TCP.

## Class List

- `ConsoleBar`: Visualizes inference results as bar graphs
- `TCPReceiver`: Receives inference results via TCP
- `TCPTransmitter`: Sends inference results via TCP

### Basic Usage

#### Bar Graph Display
```python
from maai import MaaiOutput

bar = MaaiOutput.ConsoleBar(bar_length=30, bar_type="normal")
result = {"x1": 0.7, "x2": 0.3, "t": 1.23}
bar.update(result)
```

#### TCP Receiving
```python
receiver = MaaiOutput.TCPReceiver(ip="0.0.0.0", port=12345, mode="vap")
receiver.start_process()
result = receiver.get_result()
```

#### TCP Sending
```python
transmitter = MaaiOutput.TCPTransmitter(ip="Destination IP", port=12345, mode="vap")
transmitter.start_server()
transmitter.update(result)
```

## Output Data Format via TCP Communication

The output data includes input audio data and VAP output (p_now and p_future). Note that the VAP processing frame rate differs from the input audio. For example, with a 20Hz VAP model, the audio frame size for VAP is 800. All data is in little-endian format.

__Data Frame Structure__:

Under these conditions, each output data size is 12,860 bytes. This data is sent after processing each VAP frame.

| Byte Offset | Data Type | Description |
| --- | --- | --- |
| 0 - 3 | Int | Data length (12,860) |
| 4 - 11 | Double | Unix timestamp |
| 12 - 15 | Int | Audio data (Person 1) length (800) |
| 16 - 23 | Double | Audio data (Person 1) - Sample 1 |
| 24 - 31 | Double | Audio data (Person 1) - Sample 2 |
| ... | ... | ... |
| 6408 - 6415 | Double | Audio data (Person 1) - Sample 800 |
| 6416 - 6419 | Int | Audio data (Person 2) length (800) |
| 6420 - 6427 | Double | Audio data (Person 2) - Sample 1 |
| 6428 - 6435 | Double | Audio data (Person 2) - Sample 2 |
| ... | ... | ... |
| 12812 - 12819 | Double | Audio data (Person 2) - Sample 800 |
| 12820 - 12823 | Int | p_now data length (2) |
| 12824 - 12831 | Double | p_now (Person 1) |
| 12832 - 12839 | Double | p_now (Person 2) |
| 12840 - 12843 | Int | p_future data length (2) |
| 12844 - 12851 | Double | p_future (Person 1) |
| 12852 - 12859 | Double | p_future (Person 2) |
| 12860 - 12863 | Int | VAD data length (2) |
| 12864 - 12871 | Double | VAD (Person 1) |
| 12872 - 12879 | Double | VAD (Person 2) |

## Notes

- The output data size changes depending on the VAP model frame rate (e.g., 800 samples for 20Hz)
- TCP communication sends/receives all data per frame
- Each class starts asynchronous processing with `start_process()` or `start_server()`

---

For details, please also refer to [README.md](../README.md).
