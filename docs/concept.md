# Tavily Tool

- 環境変数で必要な設定を取得する。
- refinireのtoolデコレータを使用し、RefinireAgentにWeb検索のAPIを提供する。


## 1. 前提
- プロジェクトルートに `.venv/` があり、仮想環境は起動済み  
- `claude` コマンド実行時に自動的に仮想環境を利用  

## 2. プロジェクト構成
```plaintext
/project-root
  /src
  /docs
  pyproject.toml
  todo.md
  .venv/
  /examples
  /tests
    /unit    ← ユニットテスト
    /e2e     ← バックエンド言語で記述するフロントエンドE2Eテスト
  /frontend   ← 任意
```

### 依存管理: 

- .venv/bin/activate && uv add <package>
- .venv/bin/activate && uv pip install <package> を使用
- .venv/bin/activate && pytestとカバレッジを使用

pytest設定 (pyproject.toml):

```
[project.optional-dependencies]
dev = [
  "pytest>=8.0.0",
  "pytest-cov>=4.1.0"
]
[tool.pytest.ini_options]
testpaths = ["src/tests"]
python_files = ["test_*.py"]
addopts = [
  "--import-mode=importlib",
  "--cov=src",
  "--cov-report=term-missing"
]
```

## 3. 品質制約

* 単一責任原則 (SRP)
各クラスは1責務のみ、200行以内に抑える

* DRY原則
重複コードは共通ユーティリティに抽出

* モジュール化 & ステップ生成
「モデル → サービス → コントローラ」を順次生成し、各ステップで自己レビュー

* セキュリティ & プロンプトインジェクション対策
  入力は必ずバリデーション層で検証し、直接埋め込み禁止

## 4. 設計ガイドライン強化

* ドメイン駆動型設計:
要件定義からエンティティ（データクラス）を最初に生成し、その属性と関係性に基づくクラス図（Mermaid）を作成

* クラス設計テーブル: 
各クラスごとに「名前・責務・属性一覧・メソッド一覧」を表形式で出力し、役割を明示化

* 属性取捨選択チェック:
属性を「必須」「オプショナル」「コレクション（List/Dict）」に分類し、コレクション属性は独立したValue ObjectやEntityとするか、別モジュールで扱うよう指示

各属性について「型」「多重度（1:1、1:N）」「他エンティティ共有性」をテーブル化してチェック

* 凝集度＆結合度チェック:
各クラス間の依存関係を強調し、1つのクラスに多くの依存が集中しないか確認する

* インターフェース定義:
公開メソッドのみを一覧化し、APIとしての振る舞いを切り出す

* 主要クラスレビュー:

抽象化クラス・ユースケースクラス・ファサードクラスなど、アーキテクチャ上重要なクラスをピックアップしレビュー

各クラスの公開メソッドについて、責務の一貫性・パラメータ数・返却値の明確さを評価し、メソッド呼び出しフローをサンプルコード付きで示す

ユーザー観点を重視し、最小限の呼び出しで完結するAPIを追求。複雑な前処理や属性組み立てが必要な場合はユーティリティ関数やビルダーを用いて隠蔽

必要に応じて例外・エラーケースを含むシナリオと、適切なエラーハンドリング設計を提示

* 一貫性チェック:
ネーミング規約、例外設計、ロギング、トランザクション境界など横断的関心事の適用状況を確認

* 拡張性チェック:
新たな機能追加時の影響範囲を最小に抑える設計か評価

## 4. 生成の順序

* 要件確認
* クラス名・役割・入力値と返却値を1文ずつ列挙
* データモデル定義
  Pydantic or @dataclass で属性とバリデーションを明示

* サービス実装
  ビジネスロジックはサービス層に集約し、コメントで「ここがビジネスロジックの核」

* コントローラ実装
 パラメータ取得→サービス呼び出し→レスポンス返却を厳格に

* テストスケルトン生成
  src/tests/ に pytest テスト関数を各層最低1つずつ作成

## 5. テスト & 計画

* TDD に従い、テストがパスしないと次の機能実装には進まない

* ユニットテスト: tests/unit/ 以下に pytest テスト関数を各層最低1つずつ作成

* E2E テスト: フロントエンドがある場合のみ、バックエンド言語（Python等）で tests/e2e/ にフロントエンド向け E2E テストを記述し、CLI もしくはテストランナーで実行可能に設定

* todo.md: 要件定義→アーキテクチャ→ユースケース→機能仕様→実装→テスト（unit & e2e）→検証 の粒度

## 7. デバッグサーバー設定
開発者も実行することがあるので、デフォルトとずらして実行し、確認する。

* バックエンド: デフォルト（8000）→8001 などに変更し起動
* フロントエンド: デフォルト（3000）→3001 などに変更し起動

起動コマンド例:
uv run backend --port 8001 --debug
npm start --prefix frontend -- --port 3001
