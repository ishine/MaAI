<h1>
<p align="center">
Backchannel Prediction Model (2 Types of Timing)
</p>
</h1>
<p align="center">
README: <a href="vap_bc_2type.md">English </a> | <a href="vap_bc_2type_JP.md">Japanese (日本語) </a>
</p>

Set the `mode` parameter of the `Maai` class to `bc_2type`.

This model takes 2-channel 16kHz audio data as input, assuming ch1 as user audio and ch2 as system audio.
It predicts system backchannels (BC).

The output consists of posterior probabilities for 3 classes: "no backchannel", "reactive backchannel `p_bc_react` (e.g., yeah)", and "emotional backchannel `p_bc_emo` (e.g., oh)".
The probability of each class is returned as a dictionary. However, "no backchannel" is not included in this dictionary.

</br>

## Supported Languages

Currently, only Japanese is supported.
Specify this with the `lang` parameter of the `Maai` class.

### Japanese (`lang=jp`)

This model is trained on the following Japanese dataset:
- [Human-Robot Dialogue Corpus](https://aclanthology.org/2025.naacl-long.367/)

</br>

## Implementation Example

```python
from maai import Maai, MaaiInput

mic = MaaiInput.Mic(mic_device_index=0)
zero = MaaiInput.Zero()

maai = Maai(mode="bc_2type", lang="jp", frame_rate=10, context_len_sec=5, audio_ch1=mic, audio_ch2=zero, device="cpu")
maai.start()

while True:
    result = maai.get_result()

    print(result['p_bc_react'])     # Probability of reactive backchannel
    print(result['p_bc_emo'])       # Probability of emotional backchannel
```

</br>

## Parameters

Available parameters are summarized below.
`vap_process_rate` is the number of samples the model processes per second, and `context_len_sec` is the length of context (in seconds) input to the model.

| `lang` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| jp | 10 | 5 |

</br>

## 📚 Papers & References

When publishing results using this model, please cite the following paper. 🙏

Koji Inoue, Divesh Lala, Gabriel Skantze, Tatsuya Kawaharaa<br>
__Yeah, Un, Oh: Continuous and Real-time Backchannel Prediction with Fine-tuning of Voice Activity Projection__<br>
https://aclanthology.org/2025.naacl-long.367/<br>

```
@inproceedings{inoue2025vapbc,
    author = {Koji Inoue and Divesh Lala and Gabriel Skantze and Tatsuya Kawahara},
    title = {Yeah, Un, Oh: Continuous and Real-time Backchannel Prediction with Fine-tuning of Voice Activity Projection},
    booktitle = {Proceedings of the Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
    pages = {7171--7181},
    year = {2025},
    url = {https://aclanthology.org/2025.naacl-long.367/},
}
```
