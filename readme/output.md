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
- `GuiBar`: Visualizes inference results as GUI bar graphs
- `GuiPlot`: Visualizes inference results as time-series plots
- `TCPReceiver`: Receives inference results via TCP
- `TCPTransmitter`: Sends inference results via TCP

</br>

### Basic Usage

#### Bar Graph Display
```python
from maai import MaaiOutput

bar = MaaiOutput.ConsoleBar(bar_length=30, bar_type="normal")
result = {"x1": 0.7, "x2": 0.3, "t": 1.23}
bar.update(result)
```

#### GUI Bar Graph Display
```python
from maai import MaaiOutput

gui_bar = MaaiOutput.GuiBar(bar_type="normal")
result = {"x1": 0.7, "x2": 0.3, "t": 1.23}
gui_bar.update(result)
```

#### GUI Plot Display (Time Series)
```python
from maai import MaaiOutput

gui_plot = MaaiOutput.GuiPlot(shown_context_sec=10, frame_rate=10, sample_rate=16000)
result = {"x1": [...], "x2": [...], "p_now": [...], "p_future": [...], "vad": [...], "t": 1.23}
gui_plot.update(result)
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

</br>

## Output Data Format via TCP Communication

Data is transmitted after each frame is processed.
Note that the frame rate of MaAI processing differs from the input audio.
For example, with a 10Hz model, the audio frame size is 1600 samples.
All data is in little-endian format.

### For Turn-Taking (VAP)

The output data includes input audio (`x1`, `x2`), VAP outputs (`p_now` and `p_future`), and VAD outputs.

__Data Structure (Example: 10Hz = 1600 samples/frame)__

| Item               | Byte Range         | Type   | Description                      |
|--------------------|-------------------|--------|----------------------------------|
| Data Length        | 0 - 3             | Int    | Total byte size (25,676)         |
| Timestamp          | 4 - 11            | Double | Unix timestamp                   |
| Audio 1 Length     | 12 - 15           | Int    | Number of samples (1600)         |
| Audio 1 Samples    | 16 - 12815        | Double | 1600 samples                     |
| Audio 2 Length     | 12816 - 12819     | Int    | Number of samples (1600)         |
| Audio 2 Samples    | 12820 - 25619     | Double | 1600 samples                     |
| p_now Length       | 25620 - 25623     | Int    | Number of elements (2)           |
| p_now Values       | 25624 - 25639     | Double | 2 values                         |
| p_future Length    | 25640 - 25643     | Int    | Number of elements (2)           |
| p_future Values    | 25644 - 25659     | Double | 2 values                         |
| VAD Length         | 25660 - 25663     | Int    | Number of elements (2)           |
| VAD Values         | 25664 - 25679     | Double | 2 values                         |

> * Data lengths may vary depending on frame rate and model settings.

---

### For Backchannel

Includes input audio (`x1`, `x2`) and inference results (`p_bc_react`, `p_bc_emo`).

__Data Structure (Example: 10Hz = 1600 samples/frame)__

| Item               | Byte Range         | Type   | Description                      |
|--------------------|-------------------|--------|----------------------------------|
| Data Length        | 0 - 3             | Int    | Total byte size (25,640)         |
| Timestamp          | 4 - 11            | Double | Unix timestamp                   |
| x1 Length          | 12 - 15           | Int    | Number of samples (1600)         |
| x1 Samples         | 16 - 12815        | Double | 1600 samples                     |
| x2 Length          | 12816 - 12819     | Int    | Number of samples (1600)         |
| x2 Samples         | 12820 - 25619     | Double | 1600 samples                     |
| p_bc_react Length  | 25620 - 25623     | Int    | Number of samples (1)            |
| p_bc_react Value   | 25624 - 25631     | Double | 1 value                          |
| p_bc_emo Length    | 25632 - 25635     | Int    | Number of samples (1)            |
| p_bc_emo Value     | 25636 - 25643     | Double | 1 value                          |

> * Data lengths may vary depending on frame rate and model settings.

</br>

## Notes

- The output data size changes depending on the VAP model frame rate (e.g., 800 samples for 20Hz)
- TCP communication sends/receives all data per frame
- Each class starts asynchronous processing with `start_process()` or `start_server()`

---

For details, please also refer to [README.md](../README.md).
