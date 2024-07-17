## Chinese LLM(Gemini) Chatbot
A chatbot that uses Chinese as the input language (utilizes Gemini API).  
While researching the usage of LLM's API, I happened to see an article where someone used streamlit.
I found it quite interesting and convenient, so I decided to give it a try.  
[Try it on Streamlit Cloud](https://appgeminizh-tim.streamlit.app/ "link")

### README.md
[中文](/README.md "link")<br>
[English](/README.en.md "link")<br>

### Streamlit
> Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.<br>  

### Implemented Features
Connects to the Gemini API to facilitate dialogues and Q&A with LLM, and provides two input methods: typing and voice.

### Demo
[streamlit-app-2024-07-16-14-07-60.webm](https://github.com/user-attachments/assets/6ee95a04-3cfb-480d-8626-4f544a81404b)


### Files
* app.py: Main program, handling API connection, processing input text messages,
          sending messages to the robot and receiving responses, and chat message recording and presentation.
* voice.py: Converts the content recorded by the microphone into text.
* Others (not used in the main program):
  * streamlit_app.py: Version with only keyboard typing input.
  * test.py: Microphone test.

### Reference
* Usage of Gemini API and basic Streamlit structure reference: [Link](https://medium.com/@speaktoharisudhan/building-a-gemini-powered-chatbot-in-streamlit-e241ed5958c4 "link")
* Assistant chatbot response(step-by-step output, not all at once): [Link](https://medium.com/@manojpn/building-an-interactive-ai-chat-application-with-streamlit-and-googles-gemini-pro-c7acee4f7ad4 "link")
* Using microphone as chatbot input: [Link](https://lightning.ai/aziz/studios/speech-chatbot-speak-to-llms "link") [streamlit-mic-recorder package Github](https://github.com/B4PT0R/streamlit-mic-recorder "link")
* Vertical component layout in the app using streamlit_float package: [Link](https://github.com/streamlit/streamlit/issues/7166 "link") [streamlit-float package Github](https://github.com/bouzidanas/streamlit-float "link")
