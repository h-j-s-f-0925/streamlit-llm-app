import streamlit as st
from llm import get_llm_chain_by_consultant_expert, get_llm_chain_by_cooking_expert

st.title("LLMアイデア生成アプリ")

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


# キャッシュされた関数
@st.cache_data(show_spinner=False)
def cached_llm_response(selected_item, input_message):
    if selected_item == "コンサルタント":
        return get_llm_chain_by_consultant_expert(input_message)
    else:
        return get_llm_chain_by_cooking_expert(input_message)


# セッション状態の初期化
if "llm_response" not in st.session_state:
    st.session_state.llm_response = None
if "input_message" not in st.session_state:
    st.session_state.input_message = ""

# ラジオボタンでどちらを選択したかによって表示パーツを分岐させている
if selected_item == "コンサルタント":
    st.session_state.input_message = st.text_input(
        label="業界名を入力してください。",
        # フォームの初期値を設定
        value=st.session_state.input_message,
    )
else:
    st.session_state.input_message = st.text_input(
        label="料理の材料を入力してください。",
        # フォームの初期値を設定
        value=st.session_state.input_message,
    )

if st.button("実行"):
    if st.session_state.input_message:
        with st.spinner("AIが考えています..."):
            # キャッシュされたLLMの応答を取得
            st.session_state.llm_response = cached_llm_response(
                selected_item, st.session_state.input_message
            )
    else:
        st.error("テキストを入力してから「実行」ボタンを押してください。")

# 結果の表示
if st.session_state.llm_response:
    st.divider()
    st.write(f"AIの回答: **{st.session_state.llm_response}**")
