<h1>
<p align="center">
MaaiInput モジュールの使い方
</p>
</h1>
<p align="center">
README: <a href="input.md">English </a> | <a href="input_JP.md">Japanese (日本語) </a>
</p>

MaaiInput (`input.py`) は MaAI の音声入力を柔軟に扱うためのモジュールです。
WAVファイル、マイク、TCP通信による音声入力をサポートしています。

## クラス一覧

- `Mic` : マイク入力（リアルタイム）
- `Wav` : WAVファイル入力
- `TCPReceiver` : TCP経由で音声データを受信
- `TCPTransmitter` : TCP経由でマイク入力される音声データを送信

### 基本的な使い方

#### WAVファイル入力
```python
from maai import MaaiInput

wav1 = MaaiInput.Wav(wav_file_path="user.wav")
wav2 = MaaiInput.Wav(wav_file_path="system.wav")
```

#### マイク入力
```python
mic1 = MaaiInput.Mic(mic_device_index=0)
mic2 = MaaiInput.Mic(mic_device_index=1)
```

#### TCP入力
```python
tcp_receiver = MaaiInput.TCPReceiver(ip="0.0.0.0", port=12345)
tcp_receiver.start_server()
tcp_receiver.start_process()
```

#### TCP送信
```python
tcp_transmitter = MaaiInput.TCPTransmitter(ip="送信先IP", port=12345, mic_device_index=0)
tcp_transmitter.start_process()
```

## TCP通信による音声データフォーマット

各自のオリジナルのシステムと接続する際には `TCPReceiver` クラスのインスタンスに対して、音声データを送信するとよいでしょう。
その際のデータのフォーマットは下記となります。

- サンプリングレート: 16,000 Hz
- 1フレーム: 160サンプル（各サンプルは2人分の音声データ）
- 各サンプル: 8バイトの倍精度浮動小数点（double, little endian, -1.0～+1.0）
- 1フレームのデータサイズ: 2,560バイト

### 送信順序

- 各サンプルは「1人目の8バイト」→「2人目の8バイト」の順で送信
- 1フレームで160サンプル分（1人目と2人目のペア）が連続して送信される

#### データパケット例

| バイトオフセット | データ型 | 説明 |
| ---- | ---- | --- |
| 0 - 7 | Double | 音声データ (1人目) - サンプル 1 |
| 8 - 15 | Double | 音声データ (2人目) - サンプル 1 |
| 16 - 23 | Double | 音声データ (1人目) - サンプル 2 |
| 24 - 31 | Double | 音声データ (2人目) - サンプル 2 |
| ... | ... | ... |
| 2544 - 2551 | Double | 音声データ (1人目) - サンプル 160 |
| 2552 - 2559 | Double | 音声データ (2人目) - サンプル 160 |

## デバイス一覧取得

マイクデバイスの一覧は `available_mic_devices()` で取得できます。

```python
from maai import MaaiInput

MaaiInput.available_mic_devices()
```

## 注意事項

- WAVファイルは16,000Hzのみ対応
- TCP通信は2人分の音声データを1フレームで送受信
- 各クラスは `start_process()` で非同期処理を開始

---

詳細は [README.md](../README_JP.md) も参照してください。
