# streamlit-llm-app
streamlit の学習

# ディレクトリ構成

```bash
streamlit-llm-app/           ← プロジェクトルート
    ├── pyproject.toml
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore

```

# 環境
- OS: Windows 11
- Python: 3.11.4
- Poetry: 1.9.0

# env ファイル
- .env ファイルを作成して、OPENAI_API_KEY=自身のOpenAI APIキーを記述する
- python-dotenv をインストールして、.env ファイルを読み込むようにする
```python
poetry add python-dotenv
```
- app.py に以下を追加する
```python
from dotenv import load_dotenv

load_dotenv()
```

# 作業手順
- GitHub で、streamlit-llm-app リポジトリを作成
  - リポジトリの作成時に「Add .gitignore」のセレクトボックスで「Python」を選択する

- streamlit-llm-app フォルダを作成

- git clone git@github.com:h-j-s-f-0925/streamlit-llm-app.git

- cd streamlit-llm-app

```bash
# poetry init で、pyproject.toml を作成する
# --no-interaction は、対話形式での入力をスキップするオプション
# --name は、プロジェクト名を指定するオプション
# --description は、プロジェクトの説明を指定するオプション
# --author は、作者名を指定するオプション
# --license は、ライセンスを指定するオプション
# --python は、Pythonのバージョンを指定するオプション
# --dependency は、依存関係を指定するオプション
# --dev-dependency は、開発用の依存関係を指定するオプション
# --readme は、READMEファイルのパスを指定するオプション
# --package は、パッケージの情報を指定するオプション
poetry init --no-interaction --name streamlit-llm-app --description "streamlitの練習用" --author "hoge" --license "MIT"

# .venv フォルダがプロジェクトフォルダ内に生成されるように設定
poetry config virtualenvs.in-project true --local
poetry config --list

# powershell では「\」はエラー
# poetry add \
#   streamlit==1.41.1 \
#   python-dotenv \
#   langchain==0.3.0 \
#   openai==1.47.0 \
#   langchain-community==0.3.0 \
#   langchain-openai==0.2.2 \
#   httpx==0.27.2 \
#   pydantic==2.9.2

# 1行で書く場合
# poetry add streamlit==1.41.1 python-dotenv langchain==0.3.0 openai==1.47.0 langchain-community==0.3.0 langchain-openai==0.2.2 httpx==0.27.2 pydantic==2.9.2

# powershelll
poetry add `
  streamlit==1.41.1 `
  python-dotenv `
  langchain==0.3.0 `
  openai==1.47.0 `
  langchain-community==0.3.0 `
  langchain-openai==0.2.2 `
  httpx==0.27.2 `
  pydantic==2.9.2

# 仮想環境を表示
Invoke-Expression (poetry env activate)

poetry show

# poetry env info で、仮想環境の情報を表示
poetry env info

# VsCode のインタープリターを、仮想環境に変更する

# 仮想環境に入っているので、そのまま、pyton src/main.py でスクリプトの実行
python src/env_practice/main.py

# 仮想環境から出る
deactivate

# which python で、仮想環境のパスが消えていることを確認
which python

```

## 実行
```bash
streamlit run app.py
```

- キャッシュログを確認するには、デバッグモードを有効化
```bash
streamlit run app.py --logger.level=debug
```

# デプロイ
- デプロイ先は、Streamlit Community Cloud を使用する
- Streamlit では、poetry install --no-root を指定できない
- requeirements.txt を作成して、デプロイする

```bash
# 依存状況を共有
# pip freeze > requirements.txt は、Poetry では不要
→ pyproject.toml と poetry.lock をGitにコミット

```

```bash
# デフォルトで poeetry export はインストールされていないので、インストールする必要がある
poetry self add poetry-plugin-export

# poetry export は、pyproject.toml と poetry.lock を元に、requirements.txt を生成する
# --without-hashes は、ハッシュを除外するオプション
poetry export -f requirements.txt --without-hashes -o requirements.txt
```
