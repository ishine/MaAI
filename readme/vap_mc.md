<h1>
<p align="center">
Noise-Robust Turn-Taking (VAP) Model (MC-VAP)
</p>
</h1>
<p align="center">
README: <a href="vap_mc.md">English </a> | <a href="vap_mc_JP.md">Japanese (日本語) </a>
</p>

Please set the `mode` parameter of the `Maai` class to `vap_mc`.

This model has been trained on data with various environmental noises added, and the gain of the speech audio has also been randomly changed.
Therefore, it is expected to operate more robustly in real-world environments than standard models.

The input requires 2-channel, 16kHz audio data.
There are two outputs: `p_now` represents the probability of voice activity between the two speakers occurring in the next 0 to 600 milliseconds, and `p_future` represents the probability from 600 to 2000 milliseconds ahead.
For general turn-taking purposes, we recommend using `p_now`.
Both outputs are returned as dictionaries.

</br>

## Supported Languages

The following languages are supported.
Please specify the language using the `language` parameter of the `Maai` class.
Currently, only Japanese is available, but English and Chinese are planned to be added.

### Japanese (`language=jp`)

This model is trained on the following Japanese datasets:
- [Travel Agency Task Dialogue](https://aclanthology.org/2022.lrec-1.619/)
- [Human-Robot Dialogue](https://aclanthology.org/2025.naacl-long.367/)
- [Online Conversation Dataset](https://www.arxiv.org/abs/2506.21191)

### English (`language=en`)

This model is trained on the following English dataset:
- [Switchboard corpus](https://catalog.ldc.upenn.edu/LDC97S62)
- Online Conversation Dataset

### Chinese (`language=ch`)

This model is trained on the following Chinese dataset:
- [HKUST Mandarin Telephone Speech](https://catalog.ldc.upenn.edu/LDC2005S15)
- Online Conversation Dataset

<!-- ### Tri-lingual (JPN + ENG + CHN) (`language=tri`)

This model is trained on the following three-language datasets:
- [Switchboard corpus](https://catalog.ldc.upenn.edu/LDC97S62)
- [HKUST Mandarin Telephone Speech](https://catalog.ldc.upenn.edu/LDC2005S15)
- [Travel Agency Task Dialogue](https://aclanthology.org/2022.lrec-1.619/) -->

</br>

## Example Implementation

```python
from maai import Maai, MaaiInput

wav1 = MaaiInput.Wav(wav_file_path="path_to_your_user_wav_file")
wav2 = MaaiInput.Wav(wav_file_path="path_to_your_system_wav_file")

maai = Maai(mode="vap_mc", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=wav1, audio_ch2=wav2, device="cpu")

maai.start()

while True:
    result = maai.get_result()

    print(result['p_now'])
    print(result['p_future'])
```

</br>

## Parameters

The available parameters are summarized below.
`vap_process_rate` specifies the number of samples the VAP model processes per second, and `context_len_sec` represents the length of the context (in seconds) input to the model.
Please adjust these values according to your computing environment.

| `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| jp | 5 | 3 |
| jp | 5 | 5 |
| jp | 10 | 3 |
| jp | 10 | 5 |
| jp | 20 | 2.5 |

| `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| en | 5 | 3 |
| en | 5 | 5 |
| en | 10 | 3 |
| en | 10 | 5 |
| en | 20 | 2.5 |

| `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| ch | 5 | 3 |
| ch | 5 | 5 |
| ch | 10 | 3 |
| ch | 10 | 5 |
| ch | 20 | 2.5 |

<!-- | `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| tri | 5 | 3 |
| tri | 5 | 5 |
| tri | 10 | 3 |
| tri | 10 | 5 |
| tri | 20 | 2.5 | -->

<br>

## 📚 Papers and References

When publishing results using this model, please cite the following paper. 🙏

Koji Inoue, Yuki Okafuji, Jun Baba, Yoshiki Ohira, Katsuya Hyodo, Tatsuya Kawahara<br>
__A Noise-Robust Turn-Taking System for Real-World Dialogue Robots: A Field Experiment__<br>
https://www.arxiv.org/abs/2503.06241<br>

```
@misc{inoue2025noisevap,
    author = {Koji Inoue and Yuki Okafuji and Jun Baba and Yoshiki Ohira and Katsuya Hyodo and Tatsuya Kawahara},
    title = {A Noise-Robust Turn-Taking System for Real-World Dialogue Robots: A Field Experiment},
    year = {2025},
    note = {arXiv:2503.06241},
    url = {https://www.arxiv.org/abs/2503.06241},
}
```
