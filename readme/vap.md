<h1>
<p align="center">
Turn-Taking (VAP) Model
</p>
</h1>
<p align="center">
README: <a href="vap.md">English </a> | <a href="vap_JP.md">Japanese (日本語) </a>
</p>

Set the `mode` parameter of the `Maai` class to `vap`.

The input should be two-channel 16kHz audio.

The outputs are `p_now`, which represents the probability of voice activity between two speakers in the next 0–600 milliseconds, and `p_future`, which corresponds to 600–2000 milliseconds in the future.
For typical turn-taking implementations, it is recommended to use `p_now`.
Both outputs are returned as dictionaries.

</br>

## Language

The following languages are supported.
Specify the language using the `language` parameter of the `Maai` class.

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

### Tri-lingual (JPN + ENG + CHN) (`language=tri`)

This model is trained on the following three-language datasets:
- [Switchboard corpus](https://catalog.ldc.upenn.edu/LDC97S62)
- [HKUST Mandarin Telephone Speech](https://catalog.ldc.upenn.edu/LDC2005S15)
- [Travel Agency Task Dialogue](https://aclanthology.org/2022.lrec-1.619/)

</br>

## Example

```python
from maai import Maai, MaaiInput

wav1 = MaaiInput.Wav(wav_file_path="path_to_your_user_wav_file")
wav2 = MaaiInput.Wav(wav_file_path="path_to_your_system_wav_file")

maai = Maai(mode="vap", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=wav1, audio_ch2=wav2, device="cpu")

maai.start_process()

while True:
    result = maai.get_result()

    print(result['p_now'])
    print(result['p_future'])
```

</br>

## Parameters

The available parameters are summarized below.
`vap_process_rate` specifies the number of samples processed per second by the VAP model, and `context_len_sec` corresponds to the length (in seconds) of the context input to the model.
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

| `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| tri | 5 | 3 |
| tri | 5 | 5 |
| tri | 10 | 3 |
| tri | 10 | 5 |
| tri | 20 | 2.5 |

<br>

## 📚 Publication

Please cite the following paper, if you made any publications made with this model. 🙏

Koji Inoue, Bing'er Jiang, Erik Ekstedt, Tatsuya Kawahara, Gabriel Skantze<br>
__Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection__<br>
International Workshop on Spoken Dialogue Systems Technology (IWSDS), 2024<br>
https://arxiv.org/abs/2401.04868<br>

```
@inproceedings{inoue2024iwsds,
    author = {Koji Inoue and Bing'er Jiang and Erik Ekstedt and Tatsuya Kawahara and Gabriel Skantze},
    title = {Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection},
    booktitle = {International Workshop on Spoken Dialogue Systems Technology (IWSDS)},
    year = {2024},
    url = {https://arxiv.org/abs/2401.04868},
}
```

If you use the multi-lingual VAP model, please also cite the following paper.

Koji Inoue, Bing'er Jiang, Erik Ekstedt, Tatsuya Kawahara, Gabriel Skantze<br>
__Multilingual Turn-taking Prediction Using Voice Activity Projection__<br>
Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING), pages 11873-11883, 2024<br>
https://aclanthology.org/2024.lrec-main.1036/<br>

```
@inproceedings{inoue2024lreccoling,
    author = {Koji Inoue and Bing'er Jiang and Erik Ekstedt and Tatsuya Kawahara and Gabriel Skantze},
    title = {Multilingual Turn-taking Prediction Using Voice Activity Projection},
    booktitle = {Proceedings of the Joint International Conference on Computational Linguistics and Language Resources and Evaluation (LREC-COLING)},
    pages = {11873--11883},
    year = {2024},
    url = {https://aclanthology.org/2024.lrec-main.1036/},
}
```