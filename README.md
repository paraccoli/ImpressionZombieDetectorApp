# Twitter Impression Zombie Detector

[English](#english) | [日本語](#日本語)

## English

### Overview
Twitter Impression Zombie Detector is a Python-based GUI application that helps identify potential "zombie" followers on Twitter. These are accounts that interact with tweets at an unusually high frequency, which may indicate automated or inauthentic behavior.

### Features
- Detect impression zombies based on user-defined threshold
- Analyze Twitter user's followers and their interaction patterns
- Bilingual support (English and Japanese)
- Easy-to-use graphical interface
- Secure handling of Twitter API credentials
- Settings management for API keys and thresholds

### Requirements
- Python 3.6 or higher
- tweepy library
- tkinter library (usually comes pre-installed with Python)

### Installation
1. Clone or download this repository.
2. Install the required library:
   ```
   pip install tweepy pytk
   ```

### Usage
1. Run the application with the following command:
   ```
   python main.py
   ```
2. The GUI window will open.
3. Select your preferred language from the language menu.
4. Enter the Twitter username you want to analyze in the "Twitter Username" field.
5. Set the threshold for zombie detection (default is 0.8).
6. Click the "Detect Zombies" button to start the analysis.
7. View the results in the text area below.

### File Structure
- `main.py`: Entry point of the application
- `gui/main_window.py`: Implements the main window of the graphical user interface
- `gui/dashboard.py`: Implements the dashboard frame
- `gui/zombie_detector.py`: Implements the zombie detector frame
- `gui/settings.py`: Implements the settings window
- `utils/twitter_api.py`: Provides Twitter API interaction functionality
- `utils/localization.py`: Manages translations for multi-language support
- `config.py`: Stores configuration settings

### Security Notes
- This application requires Twitter API credentials. Never share these credentials or commit them to public repositories.
- The application is intended for educational and analytical purposes. Use it responsibly and in compliance with Twitter's terms of service.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 日本語

### 概要
Twitter Impression Zombie Detectorは、Twitterの潜在的な「ゾンビ」フォロワーを識別するためのPython製のGUIアプリケーションです。これらは異常に高い頻度でツイートに反応するアカウントで、自動化された行動や不自然な振る舞いを示している可能性があります。

### 特徴
- ユーザー定義の閾値に基づくインプレッションゾンビの検出
- Twitterユーザーのフォロワーとその相互作用パターンの分析
- 日本語と英語のバイリンガルサポート
- 使いやすいグラフィカルインターフェース
- Twitter API認証情報の安全な取り扱い
- APIキーと閾値の設定管理

### 必要条件
- Python 3.6以上
- tweepyライブラリ
- tkinterライブラリ（通常Pythonにプリインストールされています）

### インストール方法
1. このリポジトリをクローンまたはダウンロードします。
2. 必要なライブラリをインストールします：
   ```
   pip install tweepy pytk
   ```

### 使用方法
1. 以下のコマンドでアプリケーションを実行します：
   ```
   python main.py
   ```
2. GUIウィンドウが開きます。
3. 言語メニューから希望の言語を選択します。
4. 「Twitterユーザー名」フィールドに分析したいTwitterユーザー名を入力します。
5. ゾンビ検出の閾値を設定します（デフォルトは0.8）。
6. 「ゾンビを検出」ボタンをクリックして分析を開始します。
7. 結果を下のテキストエリアで確認します。

### ファイル構成
- `main.py`: アプリケーションのエントリーポイント
- `gui/main_window.py`: グラフィカルユーザーインターフェースのメインウィンドウを実装
- `gui/dashboard.py`: ダッシュボードフレームを実装
- `gui/zombie_detector.py`: ゾンビ検出フレームを実装
- `gui/settings.py`: 設定ウィンドウを実装
- `utils/twitter_api.py`: Twitter API連携機能を提供
- `utils/localization.py`: 多言語サポートのための翻訳を管理
- `config.py`: 設定情報を保存

### セキュリティについて
- このアプリケーションはTwitter APIの認証情報を必要とします。これらの認証情報を共有したり、公開リポジトリにコミットしたりしないでください。
- このアプリケーションは分析目的で作成されています。Twitterの利用規約に従って使用してください。

## 作成者 Developer
- 作成者: xM1guel
- GitHub: https://github.com/xM1guel
- Zenn: https://zenn.dev/miguel