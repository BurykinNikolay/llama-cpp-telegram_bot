#Extension connecting llama-cpp-python to telegram bot api.
-
![Image1](https://github.com/innightwolfsleep/storage/raw/main/textgen_telegram.PNG)

This is wrapper for [abetlen/llama-cpp-python](https://github.com/abetlen/llama-cpp-python) providing chat like telegram bot interface.

REQUIREMENTS:
- python-telegram-bot==13.15
- pyyaml
- deep-translator==1.9.2
- llama-cpp-python

HOW TO INSTALL:
1) clone this repo 
```
git clone https://github.com/innightwolfsleep/llama-cpp-telegram_bot 
```
2) install requirements. 
```
pip install -r llama-cpp-telegram_bot\requirements.txt
```

HOW TO USE:
1) add your bot token to llama-cpp-telegram_bot/telegram_token.txt (ask https://t.me/BotFather how to get token)
2) add your model bin file to llama-cpp-telegram_bot/models
3) write path to your bin model file in llama-cpp-telegram_bot/telegram_llm_model_path.txt
2) run 
```
cd llama-cpp-telegram_bot
python main.py
```

FEATURES:
- chat and notebook modes
- session for all users are separative (by chat_id)
- local session history - conversation won't be lost if server restarts. Separated history between users and chars.
- nice "X typing" during generating (users will not think that bot stucking)
- buttons: continue previous message, regenerate last message, remove last messages from history, reset history button, new char loading menu
- you can load new characters from text-generation-webui\characters with "/load" command!!!
- you can load new model during conversation with /models 
- chatting # prefix for impersonate: "#You" or "#Castle guard" or "#Alice thoughts about me"
- "!" prefix to replace last bot message
- save/load history in chat by downloading/forwarding to chat .json file
- integrated auto-translate (you can set model/user language parameter) 

TBC:
- replace "X typing" by yield from generator
- group chat mode (need to be tested, does current workflow is ok?)
- migrate to aiogram or not?
