<p align="center">
<img src="img/logo_ver2.png" width="300">
</p>

<h1>
<p align="center">
MaAI
</p>
</h1>
<p align="center"><b>リアルタイム</b>かつ<b>軽量</b>な会話AI向け<b>非言語的ふるまい生成</b>ソフトウェア</p>
<p align="center">（Voice Activity Projectionのリアルタイム実装）</p>
<p align="center">
📄 README: <a href="README.md">English </a> | <a href="README_JP.md">Japanese (日本語) </a>
</p>

<b>MaAI</b>は（１）<b>ターンテイキング</b>、（２）<b>相槌</b>、（３）<b>頷き</b>をリアルタイムかつ連続的に予測する、最先端かつ軽量なソフトウェアです。
英語・中国語・日本語に対応しており、今後も対応言語やふるまいの種類を拡大予定です。
会話AI（対話システムやロボット等）向けに設計されており、2チャンネル（ユーザ・システム）または1チャンネル（ユーザのみ）の音声入力に対応します。🎙️
軽量設計のため、CPUのみでも高速に動作します。⚡

プロジェクトの名称の<b>MaAI</b>は、日本語の<b>間（ま）</b>や<b>間合い</b>に由来し、会話におけるタイミングや間合いの調整をAIで実現することを目指しています。

現在サポートしているモデルは主にVoice Activity Projection（VAP）およびその拡張です。
VAPモデルの詳細は以下のリポジトリを参照してください：
https://github.com/ErikEkstedt/VoiceActivityProjection

<b>MaAIソフトウェアを使用したシステム開発・共同研究</b>などは京都大学の[井上昂治](https://inokoj.github.io/)までご相談いただけますと幸いです。

<br>

__デモ動画（YouTube）__ (https://www.youtube.com/watch?v=-uwB6yl2WtI)

[![Demo video](http://img.youtube.com/vi/-uwB6yl2WtI/0.jpg)](https://www.youtube.com/watch?v=-uwB6yl2WtI)

<br>

## 🆕 新着情報

- MaAIプロジェクトおよびリポジトリを公開しました！🚀（2025年7月24日）

<br>

## 🚀 インストール

MaAIはpipで簡単にインストールできます：

```bash
pip install maai
```

> 💡 **注意:** デフォルトではPyTorchのCPU版がインストールされます。GPUで利用したい場合は、事前にCUDA環境に合ったPyTorchのGPU版をインストールしてください。

以下のように実行できます。🏃‍♂️
タスク（mode）に応じたモデルやパラメータは自動でダウンロードされます。
下記は１チャネル目はマイク入力（ユーザ）、２チャネル目は無音（システム）をターンテイキングモデル（VAP）に入力する例です。

```python
from maai import Maai, MaaiInput, MaaiOutput

mic = MaaiInput.Mic()
zero = MaaiInput.Zero() 

maai = Maai(mode="vap", language="jp", frame_rate=10, context_len_sec=5, audio_ch1=mic, audio_ch2=zero, device="cpu")
maai_output_bar = MaaiOutput.ConsoleBar(bar_type="balance")

maai.start_process()
while True:
    result = maai.get_result()
    maai_output_bar.update(result)
```

<br>

## 🧩 モデル

対応モデル（ふるまい・言語・設定など）は今後も追加予定です。
現在利用可能なモデルは[HuggingFaceリポジトリ](https://huggingface.co/maai-kyoto)をご覧ください。

### ターンテイキング

ターンテイキングモデルはVAPを用い、次の瞬間にどちらが発話するかを予測します。

- [VAPモデル](readme/vap_JP.md)
- [ノイズロバストVAPモデル（<b>推奨</b>）](readme/vap_mc_JP.md)
- [1チャンネルVAPモデル]  (準備中)

### 相槌

相槌は「うん」「はい」などの短い聞き手反応で、ターンテイキングとも関連します。

- [VAPベースの相槌予測モデル - 2種類のタイミング](readme/vap_bc_2type_JP.md)
- [VAPベースの相槌予測モデル - タイミングのみ]  (準備中)

### 頷き

頷きは頭の上下運動で、相槌と関連します。発声を伴わず非言語的に聞き手反応を示すことができます。

- [VAPベースの頷き予測モデル](readme/vap_nod_JP.md)

<br>

## 🎚️ 入出力

MaAIモデルへの入力は、`Maai`クラスインスタンスの`process`メソッドを直接呼び出せます。
`MaaiInput`クラスにより、WAVファイル・マイク・TCP通信など柔軟な音声入力が可能です。

- WAVファイル入力: `Wav`クラス 📁
- マイク入力: `Mic`クラス 🎙️
- TCP通信: `TCPReceiver` / `TCPTransmitter`クラス 🌐

これらのクラスを使うことで、用途に応じた音声入力方法を簡単に切り替えられます。

処理結果は、`Maai`クラスインスタンスの`get_result`メソッドで取得できます。
また、`MaaiOutput`クラスを使うことで、さまざまな可視化やTCP通信による出力も可能です。

- コンソール動的出力: `ConsoleBar`クラス 📊
- TCP通信: `TCPReceiver` / `TCPTransmitter`クラス 🌐

詳細は以下のREADMEもご参照ください：
- [入力について](readme/input_JP.md)
- [出力について](readme/output_JP.md)

<br>

## 💡 実装例

`test_scripts`ディレクトリにMaAIモデルの実装例があります。

- ターンテイキング（VAP）
    - [2wavファイル](test_scripts/test_vap_module_2wav.py) 🎧
    - [2マイク入力](test_scripts/test_vap_module_2mic.py) 🎤
    - [2マイク入力(TCP経由)](test_scripts/test_vap_module_2tcp.py) 🌐
    - [1wavファイル と 1マイク入力](test_scripts/test_vap_module_wav_mic.py) 🎧🎤

- 相槌
    - [1マイク入力 と 無音](test_scripts/test_vap_bc_2type_mic.py) 🎤

- 頷き
    - [1wavファイル と 1マイク入力](test_scripts/test_vap_nod_module_wav_mic.py) 🎧🎤

<br>

## 📚 論文・参考文献

本リポジトリを利用した成果を発表する際は、以下の論文を引用してください。🙏

Koji Inoue, Bing'er Jiang, Erik Ekstedt, Tatsuya Kawahara, Gabriel Skantze<br>
__Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection__<br>
International Workshop on Spoken Dialogue Systems Technology (IWSDS), 2024<br>
https://arxiv.org/abs/2401.04868<br>

```
@inproceedings{inoue2024iwsds,
    author = {Koji Inoue and Bing'er Jiang and Erik Ekstedt and Tatsuya Kawahara and Gabriel Skantze},
    title = {Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection},
    booktitle = {International Workshop on Spoken Dialogue Systems Technology (IWSDS)},
    year = {2024},
    url = {https://arxiv.org/abs/2401.04868},
}
```

トリリンガルVAPモデルを利用する場合は、以下も引用してください。

Koji Inoue, Bing'er Jiang, Erik Ekstedt, Tatsuya Kawahara, Gabriel Skantze<br>
__Multilingual Turn-taking Prediction Using Voice Activity Projection__<br>
Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING), pages 11873-11883, 2024<br>
https://aclanthology.org/2024.lrec-main.1036/<br>

```
@inproceedings{inoue2024lreccoling,
    author = {Koji Inoue and Bing'er Jiang and Erik Ekstedt and Tatsuya Kawahara and Gabriel Skantze},
    title = {Multilingual Turn-taking Prediction Using Voice Activity Projection},
    booktitle = {Proceedings of the Joint International Conference on Computational Linguistics and Language Resources and Evaluation (LREC-COLING)},
    pages = {11873--11883},
    year = {2024},
    url = {https://aclanthology.org/2024.lrec-main.1036/},
}
```

ノイズロバストVAPモデルを利用する場合は、以下も引用してください。

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

相槌VAPモデルを利用する場合は、以下も引用してください。

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

<br>

## 📝 ライセンス

本リポジトリのソースコードはMITライセンスです。
学習済みモデルは学術目的のみに利用可能です。

CPCモデルはオリジナルCPCプロジェクト由来です。
ライセンスの詳細は以下を参照してください：
https://github.com/facebookresearch/CPC_audio
