<h1>
<p align="center">
ノイズロバストターンテイキング（VAP）モデル (MC-VAP)
</p>
</h1>
<p align="center">
README: <a href="vap_mc.md">English </a> | <a href="vap_mc_JP.md">Japanese (日本語) </a>
</p>

`Maai` クラスの `mode` パラメータは `vap_mc` に設定してください。

このモデルは学習データに様々な環境雑音を重畳し、さらに発話音声のゲインもランダムに変更させています。
そのため実環境で通常のモデルより頑健に動作することが期待されます。

入力は2チャンネルの16kHz音声データが必要です。
出力は2つあり、`p_now` は2話者間の音声活動が次の0～600ミリ秒で発生する確率、`p_future` は600～2000ミリ秒先の確率を表します。
一般的なターンテイキング用途では `p_now` の利用を推奨します。
どちらの出力も辞書型で返されます。

</br>

## 対応言語

以下の言語に対応しています。
`Maai` クラスの `language` パラメータで指定してください。
現時点では日本語のみですが、英語・中国語も追加予定です。

### 日本語（`language=jp`）

本モデルは以下の日本語データセットで学習されています：
- [旅行代理店タスク対話コーパス](https://aclanthology.org/2022.lrec-1.619/)
- [ヒューマンロボット対話コーパス](https://aclanthology.org/2025.naacl-long.367/)
- [オンライン会話データセット](https://www.arxiv.org/abs/2506.21191)

</br>

## 実装例

```python
from maai import Maai, MaaiInput

wav1 = MaaiInput.Wav(wav_file_path="path_to_your_user_wav_file")
wav2 = MaaiInput.Wav(wav_file_path="path_to_your_system_wav_file")

maai = Maai(mode="vap_mc", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=wav1, audio_ch2=wav2, device="cpu")

maai.start_process()

while True:
    result = maai.get_result()

    print(result['p_now'])
    print(result['p_future'])
```

</br>

## パラメータ

利用可能なパラメータを以下にまとめます。
`vap_process_rate` はVAPモデルが1秒あたりに処理するサンプル数を指定し、`context_len_sec` はモデルへの入力となる文脈の長さ（秒）を表します。
ご利用の計算環境に合わせて、これらの値を調整してください。

| `language` | `vap_process_rate` | `context_len_sec` |
| --- | --- | --- |
| jp | 10 | 5 |

<br>

## 📚 論文・参考文献

本リポジトリを利用した成果を発表する際は、以下の論文を引用してください。🙏

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
