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

### Tri-lingual (JPN + ENG + CHN) (`language=tri`)

This model is trained on the following three-language datasets:
- [Switchboard corpus](https://catalog.ldc.upenn.edu/LDC97S62)
- [HKUST Mandarin Telephone Speech](https://catalog.ldc.upenn.edu/LDC2005S15)
- [Travel Agency Task Dialogue](https://aclanthology.org/2022.lrec-1.619/)

</br>

## Sample

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
| tri | 5 | 3 |
| tri | 5 | 5 |
| tri | 10 | 3 |
| tri | 10 | 5 |
| tri | 20 | 2.5 |
