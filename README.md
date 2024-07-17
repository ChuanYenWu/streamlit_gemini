## Chinese LLM(Gemini) Chatbot
以中文為主要輸入語言的聊天機器人(使用Gemini API)  
在查詢LLM的API使用時，剛好見到別人文章中使用到了streamlit，發現挺有趣且方便的，就決定來試一試  
[Try it on Streamlit Cloud](https://appgeminizh-tim.streamlit.app/ "link")

### README.md
[中文](/README.md "link")<br>
[English](/README.en.md "link")<br>

### Streamlit
> Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.<br>  

Streamlit讓我們能簡單藉由python架構出app

### 實作功能
連接Gemini API的來實現與LLM的對話、問答，並搭建打字輸入和語音輸入兩種方式。

### Demo
[streamlit-app-2024-07-16-14-07-60.webm](https://github.com/user-attachments/assets/6ee95a04-3cfb-480d-8626-4f544a81404b)


### 檔案
* app.py: 主程式，負責API連接、處理輸入文字訊息、傳送訊息給機器人並接收回應、聊天訊息紀錄與呈現
* voice.py: 將麥克風收錄的內容轉為文字
* 其他(主程式沒有使用):
  * streamlit_app.py: 僅有鍵盤打字輸入的版本
  * test.py: 麥克風測試

### Reference
* Gemini API的使用與基本的streamlit架構參考: [連結](https://medium.com/@speaktoharisudhan/building-a-gemini-powered-chatbot-in-streamlit-e241ed5958c4 "link")
* Assistant機器人的回答反應(逐步輸出，而非一口氣全部輸出): [連結](https://medium.com/@manojpn/building-an-interactive-ai-chat-application-with-streamlit-and-googles-gemini-pro-c7acee4f7ad4 "link")
* 使用麥克風作為chatbot輸入: [連結](https://lightning.ai/aziz/studios/speech-chatbot-speak-to-llms "link") [streamlit-mic-recorder套件 Github](https://github.com/B4PT0R/streamlit-mic-recorder "link")
* App垂直方向的組件布置，使用streamlit_float套件: [連結](https://github.com/streamlit/streamlit/issues/7166 "link") [streamlit-float套件 Github](https://github.com/bouzidanas/streamlit-float "link")

