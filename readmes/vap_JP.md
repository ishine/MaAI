<h1>
<p align="center">
ターンテイキング (VAP) モデル
</p>
</h1>
<p align="center">
README: <a href="vap.md">English </a> | <a href="vap_JP.md">Japanese (日本語) </a>
</p>

`Maai` クラスの `mode` パラメータは `vap` に設定してください。

入力は2チャンネルの16kHz音声データが必要です。

出力は2つあり、`p_now` は2話者間の音声活動が次の0～600ミリ秒で発生する確率、`p_future` は600～2000ミリ秒先の確率を表します。
一般的なターンテイキング用途では `p_now` の利用を推奨します。
どちらの出力も辞書型で返されます。

</br>

## 対応言語

以下の言語に対応しています。
`Maai` クラスの `language` パラメータで指定してください。

### 日本語（`language=jp`）

本モデルは以下の日本語データセットで学習されています：
- [旅行代理店タスク対話コーパス](https://aclanthology.org/2022.lrec-1.619/)
- [ヒューマンロボット対話コーパス](https://aclanthology.org/2025.naacl-long.367/)
- [オンライン会話データセット](https://www.arxiv.org/abs/2506.21191)

### 英語（`language=en`）

本モデルは以下の英語データセットで学習されています：
- [Switchboard コーパス](https://catalog.ldc.upenn.edu/LDC97S62)

### 3言語対応（日本語＋英語＋中国語）（`language=tri`）

本モデルは以下の3言語データセットで学習されています：
- [Switchboard コーパス](https://catalog.ldc.upenn.edu/LDC97S62)
- [HKUST マンダリン電話音声コーパス](https://catalog.ldc.upenn.edu/LDC2005S15)
- [旅行代理店タスク対話コーパス](https://aclanthology.org/2022.lrec-1.619/)

</br>

## 実装例

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

## パラメータ

利用可能なパラメータを以下にまとめます。
`vap_process_rate` はVAPモデルが1秒あたりに処理するサンプル数を指定し、`context_len_sec` はモデルへの入力となる文脈の長さ（秒）を表します。
ご利用の計算環境に合わせて、これらの値を調整してください。

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
