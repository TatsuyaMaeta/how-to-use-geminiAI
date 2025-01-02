import os
from dotenv import load_dotenv
import google.generativeai as genai

import questionary

import colored_traceback
# エラーが発生した際に、エラー箇所を色付きで表示する
colored_traceback.add_hook()

# .envファイルのパスを指定して読み込む
load_dotenv(".env")

# 環境変数を利用する
API_KEY = os.getenv("API_KEY")

# print(f"API_KEY: ", API_KEY)

# ユーザーに質問をする
indicative_sentence = questionary.text("Gemini AIへの質問をここに書いてください").ask()

# APIキーを設定して、モデルを生成
genai.configure(api_key=API_KEY)

# モデルを生成
model = genai.GenerativeModel("gemini-1.5-flash")

# モデルを利用して、質問に対する回答を生成
response = model.generate_content(indicative_sentence)

print(f"""
質問：{indicative_sentence}
====================
回答：{response.text}
""")
