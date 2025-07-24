<h1>
<p align="center">
<b>MaaiOutput</b> モジュールの使い方
</p>
</h1>
<p align="center">
README: <a href="output.md">English </a> | <a href="output_JP.md">Japanese (日本語) </a>
</p>

MaaiOutput (`output.py`) は MaAI の音声出力や可視化、TCP通信による出力を扱うためのモジュールです。
ターンテイキングや相槌、頷きなどの推論結果をバーグラフで表示したり、TCP経由で送信する機能を持っています。

## クラス一覧

- `ConsoleBar` : 推論結果をバーグラフで可視化
- `TCPReceiver` : TCP経由で推論結果を受信
- `TCPTransmitter` : TCP経由で推論結果を送信

### 基本的な使い方

#### バーグラフ表示
```python
from maai import MaaiOutput

bar = MaaiOutput.ConsoleBar(bar_length=30, bar_type="normal")
result = {"x1": 0.7, "x2": 0.3, "t": 1.23}
bar.update(result)
```

#### TCP受信
```python
receiver = MaaiOutput.TCPReceiver(ip="0.0.0.0", port=12345, mode="vap")
receiver.start_process()
result = receiver.get_result()
```

#### TCP送信
```python
transmitter = MaaiOutput.TCPTransmitter(ip="送信先IP", port=12345, mode="vap")
transmitter.start_server()
transmitter.update(result)
```

## TCP通信による出力データフォーマット

出力データには、入力オーディオデータとVAP出力（p_nowおよびp_future）が含まれます。VAP処理のフレームレートは入力オーディオとは異なることに注意してください。例えば、20HzのVAPモデルでは、VAPにおけるオーディオデータのフレームサイズは800です。また、すべてのデータはリトルエンディアン形式です。

__データフレームの構成__:

上記の条件下では、各出力データのサイズは12,860バイトとなります。このデータは、各VAPフレームの処理後に送信されます。

| バイトオフセット | データ型 | 説明 |
| --- | --- | --- |
| 0 - 3 | Int | 送信データ長 (12,860) |
| 4 - 11 | Double | Unix タイムスタンプ |
| 12 - 15 | Int | 音声データ (1人目) のデータ長 (800) |
| 16 - 23 | Double | 音声データ (1人目) - サンプル 1 |
| 24 - 31 | Double | 音声データ (1人目) - サンプル 2 |
| ... | ... | ... |
| 6408 - 6415 | Double | 音声データ (1人目) - サンプル 800 |
| 6416 - 6419 | Int | 音声データ (2人目) のデータ長 (800) |
| 6420 - 6427 | Double | 音声データ (2人目) - サンプル 1 |
| 6428 - 6435 | Double | 音声データ (2人目) - サンプル 2 |
| ... | ... | ... |
| 12812 - 12819 | Double | 音声データ (2人目) - サンプル 800 |
| 12820 - 12823 | Int | p_now のデータ長 (2) |
| 12824 - 12831 | Double | p_now (1人目) |
| 12832 - 12839 | Double | p_now (2人目) |
| 12840 - 12843 | Int | p_future のデータ長 (2) |
| 12844 - 12851 | Double | p_future (1人目) |
| 12852 - 12859 | Double | p_future (2人目) |
| 12860 - 12863 | Int | VAD のデータ長 (2) |
| 12864 - 12871 | Double | VAD (1人目) |
| 12872 - 12879 | Double | VAD (2人目) |

## 注意事項

- VAPモデルのフレームレートによって出力データサイズが変わります（例: 20Hzなら800サンプル）
- TCP通信は1フレームごとに全データを送受信
- 各クラスは `start_process()` または `start_server()` で非同期処理を開始

---

詳細は [README.md](../README_JP.md) も参照してください。
