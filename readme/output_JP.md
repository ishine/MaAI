<h1>
<p align="center">
<b>MaaiOutput</b> モジュールの使い方
</p>
</h1>
<p align="center">
README: <a href="output.md">English </a> | <a href="output_JP.md">Japanese (日本語) </a>
</p>

MaaiOutput (`output.py`) は MaAI の出力を扱うためのモジュールです。
ターンテイキングや相槌、頷きなどの推論結果をバーグラフで表示したり、TCP経由で送受信する機能を持っています。

</br>

## クラス一覧

- `ConsoleBar` : 推論結果をバーグラフで可視化
- `GuiBar` : 推論結果をGUIバーグラフで可視化
- `GuiPlot` : 推論結果を時系列プロットで可視化
- `TcpReceiver` : TCP経由で推論結果を受信
- `TcpTransmitter` : TCP経由で推論結果を送信

</br>

## 基本的な使い方

### バーグラフ表示
```python
from maai import MaaiOutput

bar = MaaiOutput.ConsoleBar(bar_length=30, bar_type="normal")
result = {"x1": 0.7, "x2": 0.3, "t": 1.23}
bar.update(result)
```

### GUIバーグラフ表示
```python
from maai import MaaiOutput

gui_bar = MaaiOutput.GuiBar(bar_type="normal")
result = {"x1": 0.7, "x2": 0.3, "t": 1.23}
gui_bar.update(result)
```

### GUIプロット表示（時系列）
```python
from maai import MaaiOutput

gui_plot = MaaiOutput.GuiPlot(shown_context_sec=10, frame_rate=10, sample_rate=16000)
result = {"x1": [...], "x2": [...], "p_now": [...], "p_future": [...], "vad": [...], "t": 1.23}
gui_plot.update(result)
```

### TCP受信
```python
receiver = MaaiOutput.TcpReceiver(ip="0.0.0.0", port=12345, mode="vap")
receiver.start()
result = receiver.get_result()
```

### TCP送信
```python
transmitter = MaaiOutput.TcpTransmitter(ip="送信先IP", port=12345, mode="vap")
transmitter.start_server()
transmitter.update(result)
```

</br>

## TCP通信による出力データフォーマット

各フレーム処理後にデータが送信されます。
MaAIの処理のフレームレートは入力オーディオとは異なることに注意してください。
例えば、10Hzのモデルでは、オーディオデータのフレームサイズは1600です。
また、すべてのデータはリトルエンディアン形式です。

### ターンテイキング（VAP）の場合

出力データには、入力オーディオデータ、VAP出力（p_nowおよびp_future）、VAD出力が含まれます。

__データ構造（例: 10Hz = 1600サンプル/フレーム）

| 項目              | バイト範囲      | 型     | 内容                       |
|-------------------|----------------|--------|----------------------------|
| データ長          | 0 - 3          | Int    | 全体のバイト数（25,676）   |
| タイムスタンプ    | 4 - 11         | Double | Unixタイムスタンプ         |
| 音声1データ長     | 12 - 15        | Int    | サンプル数（1600）         |
| 音声1サンプル     | 16 - 12815     | Double | 1600個                     |
| 音声2データ長     | 12816 - 12819  | Int    | サンプル数（1600）         |
| 音声2サンプル     | 12820 - 25619  | Double | 1600個                     |
| p_nowデータ長     | 25620 - 25623  | Int    | 要素数（2）                |
| p_now値           | 25624 - 25639  | Double | 2人分                      |
| p_futureデータ長  | 25640 - 25643  | Int    | 要素数（2）                |
| p_future値        | 25644 - 25659  | Double | 2人分                      |
| VADデータ長       | 25660 - 25663  | Int    | 要素数（2）                |
| VAD値             | 25664 - 25679  | Double | 2人分                      |

> ※ 各データ長はフレームレートやモデル設定によって変わります。

---

### 相槌の場合

入力音声（x1, x2）と推論結果（p_bc_react, p_bc_emo）が含まれます。  

__データ構造（例: 10Hz = 1600サンプル/フレーム）

| 項目              | バイト範囲      | 型     | 内容                       |
|-------------------|----------------|--------|----------------------------|
| データ長          | 0 - 3          | Int    | 全体のバイト数（25,640）   |
| タイムスタンプ    | 4 - 11         | Double | Unixタイムスタンプ         |
| x1データ長        | 12 - 15        | Int    | サンプル数（1600）         |
| x1サンプル        | 16 - 12815     | Double | 1600個                     |
| x2データ長        | 12816 - 12819  | Int    | サンプル数（1600）         |
| x2サンプル        | 12820 - 25619  | Double | 1600個                     |
| p_bc_react長      | 25620 - 25623  | Int    | サンプル数（1）            |
| p_bc_react値      | 25624 - 25631  | Double | 1個                        |
| p_bc_emo長        | 25632 - 25635  | Int    | サンプル数（1）            |
| p_bc_emo値        | 25636 - 25643  | Double | 1個                        |

> ※ 各データ長はフレームレートやモデル設定によって変わります。

</br>

## 注意事項

- VAPモデルのフレームレートによって出力データサイズが変わります（例: 20Hzなら800サンプル）
- TCP通信は1フレームごとに全データを送受信
- 各クラスは `start()` または `start_server()` で非同期処理を開始

---

詳細は [README.md](../README_JP.md) も参照してください。
