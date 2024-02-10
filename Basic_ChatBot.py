import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me ChatGPT.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thank you!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.", "No need to apologize.",]
    ],
    [
        r"(.*) (good|well|fine)",
        ["That's great to hear!", "Awesome!",]
    ],
    [
        r"quit",
        ["Bye, take care. Have a great day!", "Goodbye!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that. Can you please rephrase?",]
    ]
]

def chatbot():
    print("Hi, I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
