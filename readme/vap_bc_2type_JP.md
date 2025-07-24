<h1>
<p align="center">
相槌予測モデル（２種類のタイミング）
</p>
</h1>
<p align="center">
README: <a href="vap_bc_2type.md">English </a> | <a href="vap_bc_2type_JP.md">Japanese (日本語) </a>
</p>

`Maai` クラスの `mode` パラメータは `vap_bc_2type` に設定してください。

本モデルは2チャンネルの16kHz音声データを入力とし、ch1をユーザ、ch2をシステムの音声として想定しています。
そして、システムの相槌（Backchannel, BC）を予測します。

出力は3つのクラス（「相槌なし」「応答系相槌 `p_bc_react`（例：うん、はい）」 「感情表出系相槌 `p_bc_emo`（例：おー、へー）」）の事後確率です。
各クラスの確率は辞書型で返されます。ただし、「相槌なし」はこの辞書には含まれません。

</br>

## 対応言語

現時点では日本語のみ対応しています。
`Maai` クラスの `language` パラメータで指定してください。

### 日本語（`language=jp`）

本モデルは以下の日本語データセットで学習されています：
- [ヒューマンロボット対話コーパス](https://aclanthology.org/2025.naacl-long.367/)

</br>

## 実装例

```python
from maai import Maai, MaaiInput

mic = MaaiInput.Mic(mic_device_index=0)
zero = MaaiInput.Zero()

maai = Maai(mode="vap_bc_2type", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=mic, audio_ch2=zero, device="cpu")
maai.start_process()

while True:
    result = maai.get_result()

    print(result['p_bc_react'])     # 応答系相槌の確率
    print(result['p_bc_emo'])       # 感情表出系相槌の確率
```

</br>

## パラメータ

利用可能なパラメータを以下にまとめます。
`vap_process_rate` はモデルが1秒あたりに処理するサンプル数、`context_len_sec` はモデルへの入力となる文脈の長さ（秒）です。

| `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| jp | 10 | 5 |

</br>

## 📚 論文・参考文献

このモデルを利用した成果を発表する際は、以下の論文を引用してください。🙏

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

