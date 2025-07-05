# Refinire Tool Tavily

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Tavily APIを使用したRefinireAgent向けの包括的なWeb検索ツールです。このパッケージは、RefinireエージェントとTavilyの強力なWeb検索機能をシームレスに統合します。

[English README](README.md)

## 特徴

- 🔍 **Web検索統合**: RefinireAgent用の完全なTavily API統合
- 🤖 **Refinireツールデコレータ**: エージェント統合用のすぐに使えるツール
- 📊 **複数の検索タイプ**: 一般、ニュース、研究、コンテキスト最適化検索
- 🛡️ **セキュリティ＆バリデーション**: 入力検証とプロンプトインジェクション保護
- 🔧 **環境管理**: 簡単な設定のためのOneEnv統合
- ✅ **包括的テスト**: 堅牢なエラーハンドリングで68%のテストカバレッジ
- 📚 **豊富なドキュメント**: すべてのユースケース向けの例とガイド

## クイックスタート

### インストール

```bash
pip install refinire-tool-tavily
```

### 環境設定

1. 環境テンプレートを生成:
```bash
oneenv template
```

2. コピーして設定:
```bash
cp .env.example .env
# .envを編集してTavily APIキーを追加
```

3. [https://tavily.com/](https://tavily.com/)からTavily APIキーを取得

### 基本的な使用方法

```python
from refinire_tool_tavily import search_web

# シンプルなWeb検索
result = search_web("Pythonプログラミングのベストプラクティス", max_results=5)

if result["success"]:
    for item in result["results"]:
        print(f"{item['title']}: {item['url']}")
```

### RefinireAgent統合

```python
from refinire import Agent
from refinire_tool_tavily import refinire_web_search

# Web検索機能を持つエージェントを作成
agent = Agent(
    name="WebSearchAgent",
    instructions="必要に応じてWeb検索を使用して最新情報を見つけてください。",
    tools=[refinire_web_search]
)

# エージェントを使用
response = agent.run("AIの最新動向について教えて")
```

## 利用可能なツール

### コア関数

- **`search_web()`**: 完全にカスタマイズ可能な基本Web検索
- **`get_search_context()`**: LLM消費用にフォーマットされた検索結果

### Refinireツール

- **`refinire_web_search`**: エージェント用の一般Web検索ツール
- **`refinire_web_search_context`**: LLM向けコンテキスト最適化検索
- **`refinire_web_search_news`**: AI要約付きニュース特化検索
- **`refinire_web_search_research`**: 学術・研究特化検索

## 検索タイプ

### 一般Web検索
```python
result = search_web(
    query="機械学習トレンド 2024",
    max_results=10,
    include_answer=True
)
```

### ニュース検索
```python
from refinire_tool_tavily import refinire_web_search_news

news = refinire_web_search_news("AI規制", max_results=5)
print(news["answer"])  # AI生成ニュース要約
```

### 研究検索
```python
from refinire_tool_tavily import refinire_web_search_research

research = refinire_web_search_research("ニューラルネットワーク", max_results=3)
# 詳細分析用の生コンテンツを含む
```

## 設定

### 環境変数

| 変数 | 説明 | 必須 | デフォルト |
|------|------|------|------------|
| `TAVILY_API_KEY` | Tavily APIキー | はい | - |
| `LOG_LEVEL` | ログレベル | いいえ | INFO |
| `DEFAULT_MAX_RESULTS` | デフォルト最大結果数 | いいえ | 5 |
| `DEFAULT_INCLUDE_ANSWER` | AI回答を含める | いいえ | false |
| `DEFAULT_INCLUDE_RAW_CONTENT` | 生コンテンツを含める | いいえ | false |

### 高度な設定

```python
from refinire_tool_tavily import ConfigManager

config = ConfigManager()
config.print_config_status()  # 設定確認
config.show_env_help()        # 環境ヘルプ表示
```

## 使用例

### フィルタリング付き基本検索
```python
result = search_web(
    query="Python Webフレームワーク",
    max_results=5,
    include_domains=["python.org", "docs.python.org"],
    exclude_domains=["spam.com"],
    include_answer=True
)
```

### 言語モデル用コンテキスト
```python
from refinire_tool_tavily import get_search_context

context = get_search_context("気候変動対策", max_results=3)
# LLM消費準備済みのフォーマット済みテキストを返す
```

### エラーハンドリング
```python
result = search_web("テストクエリ")

if result["success"]:
    # 結果を処理
    for item in result["results"]:
        print(item["title"])
else:
    print(f"検索失敗: {result['error']}")
```

## 開発

### 開発環境セットアップ

```bash
# リポジトリクローン
git clone https://github.com/kitfactory/refinire-tool-tavily.git
cd refinire-tool-tavily

# 開発モードでインストール
source .venv/bin/activate
uv pip install -e .

# テスト実行
python -m pytest tests/ -v
```

### プロジェクト構造

```
refinire-tool-tavily/
├── src/refinire_tool_tavily/
│   ├── __init__.py          # パッケージエクスポート
│   ├── api.py               # パブリックAPI関数
│   ├── models.py            # Pydanticデータモデル
│   ├── service.py           # Tavilyサービス実装
│   ├── tools.py             # Refinireツールデコレータ
│   ├── config.py            # 設定管理
│   └── oneenv_template.py   # OneEnvテンプレート
├── tests/                   # テストスイート
├── examples/                # 使用例
└── docs/                    # ドキュメント
```

## 依存関係

- **refinire**: RefinireAgent統合
- **tavily-python**: Tavily APIクライアント
- **pydantic**: データ検証
- **oneenv**: 環境管理
- **python-dotenv**: 環境ファイル読み込み

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

貢献を歓迎します！お気軽にPull Requestを提出してください。

## サポート

- 📖 **ドキュメント**: [例とガイド](examples/)
- 🐛 **Issues**: [GitHub Issues](https://github.com/kitfactory/refinire-tool-tavily/issues)
- 💬 **ディスカッション**: [GitHub Discussions](https://github.com/kitfactory/refinire-tool-tavily/discussions)

## 関連プロジェクト

- [Refinire](https://github.com/kitfactory/refinire) - AIエージェントフレームワーク
- [Tavily](https://tavily.com/) - Web検索APIサービス
- [OneEnv](https://github.com/kitfactory/oneenv) - 環境変数管理

## 使用例集

### ニュース情報収集
```python
# 最新のAIニュースを検索
news_result = refinire_web_search_news("人工知能 最新ニュース")
print("AI要約:", news_result["answer"])
```

### 研究情報検索
```python
# 学術論文や技術文書を検索
research_result = refinire_web_search_research("深層学習 Transformer")
for paper in research_result["results"]:
    print(f"論文: {paper['title']}")
    print(f"URL: {paper['url']}")
```

### カスタム検索
```python
# 特定のドメインに絞った検索
result = search_web(
    query="Python チュートリアル",
    include_domains=["python.org", "docs.python.org", "realpython.com"],
    max_results=10,
    include_answer=True
)
```

## トラブルシューティング

### よくある問題

1. **APIキーエラー**:
```bash
# .envファイルを確認
cat .env
# TAVILY_API_KEY=your_actual_api_key_here
```

2. **設定確認**:
```python
from refinire_tool_tavily import check_config
if not check_config():
    print("設定に問題があります")
```

3. **環境テンプレート再生成**:
```bash
oneenv template
cp .env.example .env
```