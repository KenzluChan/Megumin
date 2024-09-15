from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time

chatbot = ChatBot(
    'Megumin',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': '很抱歉，我無法理解你的意思．:(\nI am sorry, but I do not understand.:(',
            'maximum_similarity_threshold': 0.20,
        }
    ],
    database_uri = r"sqlite:///K:\Megumin\extensions\Chatterbot\data\database.sqlite3"
)



trainer = ChatterBotCorpusTrainer(chatbot)

def get_bot_response(message):
    try:
        response=chatbot.get_response(message)
    except Exception as e:
        response = f"An error occurred: {str(e)}"
    return response
    
def clearbotdata():
    chatbot.storage.drop()
    return "Clear bot data complete!"

def trainbot(language):
    try:
        data = 'chatterbot.corpus.' + language
        trainer.train(data)
        return f'Training bot complete! (data: {language})'
    except Exception as e:
        return '[Error]You used an unsupported language or incorrect syntax. Check available data: https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data.'

