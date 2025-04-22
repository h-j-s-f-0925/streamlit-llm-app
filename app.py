import streamlit as st
from llm import get_llm_chain_by_consultant_expert, get_llm_chain_by_cooking_expert

st.title("LLMアプリ")

st.write("##### 専門家1: コンサルタント")
st.write(
    "入力フォームにテキストを入力し、「実行」ボタンを押すことで、ビジネスアイデアを生成できます。"
)
st.write("##### 専門家2: 料理専門家")
st.write(
    "入力フォームにテキストを入力し、「実行」ボタンを押すことで、料理のアイデアを生成できます。"
)

selected_item = st.radio(
    "LLMに振る舞わせる専門家の種類を選択してください。",
    ["コンサルタント", "料理専門家"],
)

st.divider()

# ラジオボタンでどちらを選択したかによって表示パーツを分岐させている
if selected_item == "コンサルタント":
    input_message = st.text_input(label="業界名を入力してください。")
    # LLMの出力を仮に実装
    # llm_output = "ビジネスアイデアを生成しました。"
    print(input_message)
    if input_message:
        with st.spinner("AIが考えています..."):
            # コンサルタントのLLMを呼び出す
            llm_response = get_llm_chain_by_consultant_expert(input_message)

else:
    input_message = st.text_input(label="料理の材料を入力してください。")
    # llm_output = "マーケティング戦略を生成しました。"
    if input_message:
        with st.spinner("AIが考えています..."):
            # コンサルタントのLLMを呼び出す
            llm_response = get_llm_chain_by_cooking_expert(input_message)

if st.button("実行"):
    st.divider()

    if selected_item == "コンサルタント":
        if input_message:
            st.write(f"AIの回答: **{llm_response}**")

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            st.write(f"AIの回答: **{llm_response}**")

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")
