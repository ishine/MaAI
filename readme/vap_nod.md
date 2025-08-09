<h1>
<p align="center">
Nod Prediction Model
</p>
</h1>
<p align="center">
README: <a href="vap_nod.md">English </a> | <a href="vap_nod_JP.md">Japanese (日本語) </a>
</p>

Set the `mode` parameter of the `Maai` class to `nod`.

This model takes 2-channel 16kHz audio data as input, assuming ch1 as user audio and ch2 as system audio.

It predicts the following three types of nods in real time and continuously, returning the results as a dictionary.

<p align="center">

| `type` | `description` | `image` |
| --- | --- | --- |
| short | Small movement range | <img src="../img/short.gif" width="200"> |
| long | Large movement range, no upward swing | <img src="../img/long.gif" width="200"> |
| long_p | Large movement range, with upward swing | <img src="../img/long_p.gif" width="200"> |

CG-CA Gene (c) 2023 by Nagoya Institute of Technology, Moonshot R&D Goal 1 Avatar Symbiotic Society
</p>

</br>

## Supported Languages

Currently, only Japanese is supported.
Specify this with the `language` parameter of the `Maai` class.

### Japanese (`language=jp`)

This model is trained on the following Japanese dataset:
- [Human-Robot Dialogue Corpus]()

</br>

## Example Implementation

```python
from maai import Maai, MaaiInput

mic = MaaiInput.Mic(mic_device_index=0)
zero = MaaiInput.Zero()

maai = Maai(mode="nod", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=mic, audio_ch2=zero,device="cpu")
maai.start()

while True:
    result = maai.get_result()

    print(result['short'])
    print(result['long'])
    print(result['long_p'])
```

</br>

## Parameters

Available parameters are summarized below.
`vap_process_rate` is the number of samples the model processes per second, and `context_len_sec` is the length of context (in seconds) input to the model.

| `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| jp | 5 | 3 |
| jp | 5 | 5 |
| jp | 5 | 10 |
| jp | 10 | 3 |
| jp | 10 | 5 |
| jp | 10 | 10 |
| jp | 20 | 3 |
| jp | 20 | 5 |
| jp | 20 | 10 |

<br>

## 📚 Papers & References

When publishing results using this model, please cite the following paper. 🙏

Kazushi Kato, Koji Inoue, Divesh Lala, Keiko Ochi, Tatsuya Kawahara<br>
__Real-time Generation of Various Types of Nodding for Avatar Attentive Listening System__<br>
https://www.arxiv.org/abs/2507.23298<br>

```
@inproceedings{kato2025icmi,
    author = {Kazushi Kato and Koji Inoue and Divesh Lala and Keiko Ochi and Tatsuya Kawahara},
    title = {Real-time Generation of Various Types of Nodding for Avatar Attentive Listening System},
    booktitle = {International Conference on Multimodal Interaction (ICMI)},
    year = {2025},
}
```