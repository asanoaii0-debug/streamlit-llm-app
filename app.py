from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain import LLMChain

st.title("【提出課題】LLM機能を搭載したWebアプリを開発しよう")

st.write("入力フォームにテキストをお悩みを入力し、「実行」ボタンを押すことで、専門家からのアドバイスを表示することができます。")

selected_item = st.radio(
    label="あなたのお悩みは次のどちらですか？",
    options=["【A】資産形成", "【B】健康増進"]
)

input_message = st.text_input(label="お悩みを入力してください")

if st.button("実行"):
    st.divider()

    if selected_item == "【A】資産形成":
        specialized_area = "資産形成"
    else:
        specialized_area = "健康増進"

    if input_message:
        template = """
        あなたは以下の領域の専門家です。入力された悩みを解決するための具体的なアドバイスを3つ、箇条書きで出力してください。
        領域：{specialized_area}
        悩み：{input_message}
        """

        prompt = PromptTemplate(
            input_variables=["specialized_area", "input_message"],
            template=template
        )

        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

        chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

        result = chain.run(specialized_area=specialized_area, input_message=input_message)
        st.write(result)

    else:
        st.error("悩みを入力してから「実行」ボタンを押してください。")
