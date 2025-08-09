<h1>
<p align="center">
頷き予測モデル
</p>
</h1>
<p align="center">
README: <a href="vap_nod.md">English </a> | <a href="vap_nod_JP.md">Japanese (日本語) </a>
</p>

`Maai` クラスの `mode` パラメータは `nod` に設定してください。

本モデルは2チャンネルの16kHz音声データを入力とし、ch1をユーザ、ch2をシステムの音声として想定しています。

このモデルは次の3つの形態の頷きをリアルタイムかつ連続的に予測し、辞書形式で返します。

<p align="center">

| `形態` | `説明` | `イメージ` |
| --- | --- | --- |
| short | 移動範囲が小さい | <img src="../img/short.gif" width="200"> |
| long | 移動範囲が大きく、振り上げがない | <img src="../img/long.gif" width="200"> |
| long_p | 移動範囲が大きく、振り上げがある | <img src="../img/long_p.gif" width="200"> |

CG-CA Gene (c) 2023 by Nagoya Institute of Technology, Moonshot R&D Goal 1 Avatar Symbiotic Society
</p>

</br>

## 対応言語

現時点では日本語のみ対応しています。
`Maai` クラスの `language` パラメータで指定してください。

### 日本語（`language=jp`）

本モデルは以下の日本語データセットで学習されています：
- [ヒューマンロボット対話コーパス]()

</br>

## 実装例

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

## パラメータ

利用可能なパラメータを以下にまとめます。
`vap_process_rate` はモデルが1秒あたりに処理するサンプル数、`context_len_sec` はモデルへの入力となる文脈の長さ（秒）です。

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

## 📚 論文・参考文献

このモデルを利用した成果を発表する際は、以下の論文を引用してください。🙏

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