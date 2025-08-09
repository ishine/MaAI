<h1>
<p align="center">
<b>MaaiInput</b> モジュールの使い方
</p>
</h1>
<p align="center">
README: <a href="input.md">English </a> | <a href="input_JP.md">Japanese (日本語) </a>
</p>

MaaiInput (`input.py`) は MaAI の音声入力を柔軟に扱うためのモジュールです。
WAVファイル、マイク、TCP通信による音声入力をサポートしています。

</br>

## クラス一覧

- `Mic` : マイク入力（リアルタイム）
- `Wav` : WAVファイル入力
- `Tcp` : TCP経由で音声データを受信（サーバ）
- `TcpMic` : TCP経由でマイク入力される音声データを送信（クライアント）
- `Zero` : 無音（ゼロ埋め）データを生成（システム側の音声を一時的に埋めることを想定）
- `Chunk` : チャンク入力
- `TcpChunk` : TCP経由で音声データをチャンク送信（クライアント）

</br>

## 基本的な使い方

### WAVファイル入力
```python
from maai import MaaiInput

wav1 = MaaiInput.Wav(wav_file_path="user.wav")
wav2 = MaaiInput.Wav(wav_file_path="system.wav")
```

### マイク入力
```python
mic1 = MaaiInput.Mic(mic_device_index=0)
mic2 = MaaiInput.Mic(mic_device_index=1)
```

### TCP入力
```python
tcp_receiver = MaaiInput.Tcp(ip="0.0.0.0", port=12345)
tcp_receiver.start_server()
```

### TCPマイク送信
```python
tcp_mic = MaaiInput.TcpMic(server_ip="送信先IP", port=12345, mic_device_index=0)
tcp_mic.start()
```

### 無音（ゼロ埋め）入力
```python
zero_input = MaaiInput.Zero()
```

### チャンク入力
```python
mic_input = MaaiInput.Chunk()
mic_input.put_chunk(mic_chunk)
```

### TCPチャンク送信

```python
tcp_chunk = MaaiInput.TcpChunk(server_ip="送信先IP", port=12345, mic_device_index=0)
tcp_chunk.start()
```

</br>

## TCP通信による音声データフォーマット

各自のオリジナルのシステムと接続する際には `TCPReceiver` クラスのインスタンスに対して、音声データを送信するとよいでしょう。
その際のデータのフォーマットは下記となります。

- サンプリングレート: 16,000 Hz
- 1フレーム: 160サンプル
- 各サンプル: 8バイトの倍精度浮動小数点（double, little endian, -1.0～+1.0）
- 1フレームのデータサイズ: 1,280バイト

### データパケット例

| バイトオフセット | データ型 | 説明 |
| ---- | ---- | --- |
| 0 - 7 | Double | 音声データ - サンプル 1 |
| 8 - 15 | Double | 音声データ - サンプル 2 |
| ... | ... | ... |
| 1264 - 1271 | Double | 音声データ - サンプル 159 |
| 1272 - 1279 | Double | 音声データ - サンプル 160 |

</br>

## デバイス一覧取得

マイクデバイスの一覧は `available_mic_devices()` で取得できます。

```python
from maai import MaaiInput

MaaiInput.available_mic_devices()
```

## 注意事項

- WAVファイルは16,000Hzのみ対応
- TCP通信は2人分の音声データを1フレームで送受信
- 各クラスは `start()` で非同期処理を開始

---

詳細は [README.md](../README_JP.md) も参照してください。
