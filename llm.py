import os

from dotenv import load_dotenv
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

# .envファイルをロードします
load_dotenv()
api_key_str = os.environ["OPENAI_API_KEY"]
api_key = SecretStr(api_key_str) if api_key_str else None


def get_llm_chain_by_consultant_expert(industry):
    """
    コンサルタントの専門知識を活用して、指定された業界におけるビジネスアイデアを生成します。

    Args:
        industry (str): 業界名。

    Returns:
        str: 生成されたビジネスアイデア。
    """

    template = """
    あなたは優秀なコンサルタントです。以下の業界におけるビジネスアイデアを3つ書いてください。
    業界：{industry}
    ビジネスアイデア：
    """

    prompt = PromptTemplate(
        input_variables=[
            "industry"
        ],  # SimpleSequentialChain は1つで、SequentialChain は 2つ
        template=template,
    )

    # ChatOpenAIのインスタンス（Chat Completions APIにアクセスするためのPythonオブジェクト）を用意
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
        temperature=0.5,
    )

    chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    result = chain.run(industry=industry)
    # print(result)
    return result


def get_llm_chain_by_cooking_expert(ingredient):
    """
    料理の専門知識を活用して、指定された食材を基にユニークな料理アイデアを生成します。

    Args:
        ingredient (str): 食材名。

    Returns:
        str: 生成された料理アイデア。
    """
    template = """
    あなたは料理専門家です。以下の食材において、ユニークな料理アイデアを作成してください。
    食材：{ingredient}
    """

    prompt = PromptTemplate(
        input_variables=[
            "ingredient"
        ],  # SimpleSequentialChain は1つで、SequentialChain は 2つ
        template=template,
    )

    # ChatOpenAIのインスタンス（Chat Completions APIにアクセスするためのPythonオブジェクト）を用意
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
        temperature=0.5,
    )

    chain = LLMChain(
        prompt=prompt,
        llm=llm,
        verbose=True
    )

    result = chain.run(ingredient=ingredient)
    # print(result)
    return result


if __name__ == "__main__":
    # Streamlitアプリを実行するためのコードをここに追加
    get_llm_chain_by_consultant_expert("アパレル")
