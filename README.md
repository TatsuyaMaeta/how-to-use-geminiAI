# How to use gemini AI API for free

## summary
Gemini AI's API has recently been released. The API is available free of charge to some extent, and I have created a python version of the procedure to use it.
Please use it systematically.
(Please do not regret to github your API key!!!)

https://ai.google.dev/gemini-api/docs?_gl&hl=ja


## Pricing Model
https://ai.google.dev/pricing?hl=ja#1_5flash

| 項目                                  | 内容                                                                   |
| :------------------------------------ | :--------------------------------------------------------------------- |
| **レートに関する上限**                                        
| リクエスト/分 (RPM)                   | 15 RPM                                                                 |
| トークン/分 (TPM)                     | 100万 TPM                                                              |
| リクエスト/日 (RPD)                   | 1,500 RPD                                                              |
| **料金**                              |                                                                        |
| 入力料金                              | 無料                                                                   |
| 出力料金                              | 無料                                                                   |
| **コンテキストキャッシュ保存**        | 1時間あたり最大100万トークンのストレージが無料                         |
| **チューニング料金**                  | チューニング済みモデルの入出力料金は同じ。チューニングサービスは無料。 |
| **Google 検索によるグラウンディング** | 利用不可                                                               |
| **サービスの改善に使用**              | はい                                                                   |

## Steps for how to use

1. Build a virtual environment in Terminal
   1. This repository uses venv library to build a working environment for python
   ``` 
    python -m venv venv
   ```
1. (After the venv folder has been created in the execution hierarchy)Specify venv's python as the execution interpreter
   1. Execute with the following command
   ```
    source venv/bin/activate
   ```
1. If you need to install the software with the following command, install it from the list in the “iburariwo requirement.txt” file.
    1. Execute with the following command
    ```
    pip install -r requirements.txt
    ```
    1. If you want to install only officially specified libraries, execute only the following commands
       1. 
       ```
        pip install google-generativeai
       ```
       1. Ref: https://ai.google.dev/gemini-api/docs/downloads?hl=ja
 2. Copy the .env.sample file to create the .env file
    1. 
    ```
    cp .env.sample .env2
    ```
1. Get API KEY to use gemini API from google ai studio
   1. https://aistudio.google.com/apikey
1. Enter the obtained API Key in the .env file
   1. 
   ``` .env
    API_KEY=AIza~~~~~~~~~~~~~~~
   ```
2. Run main.py and enter a question
   1. 
   ``` bash
    python main.py
   ```