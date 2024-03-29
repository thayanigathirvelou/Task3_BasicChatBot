import nltk
from nltk.chat.util import Chat, reflections


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
        r"what is your favorite color?",
        ["I'm just a chatbot, so I don't have a favorite color. What's yours?",]
    ],
    [
        r"how old are you?",
        ["I don't have an age. I'm here to assist you with any questions you have.",]
    ],
    [
        r"tell me about yourself",
        ["I am a chatbot designed to assist and engage in conversations. Ask me anything!",]
    ],
    [
        r"favorite food",
        ["I don't eat, but I'm here to help with any questions or concerns you may have.",]
    ],
    [
        r"weather today",
        ["I'm afraid I don't have real-time data. You can check a weather website for accurate information.",]
    ],
    [
        r"how can I learn programming?",
        ["There are many online resources like tutorials, courses, and coding platforms. Find what suits your learning style!",]
    ],
    [
        r"what's your favorite movie?",
        ["I don't watch movies, but I've heard 'The Matrix' is quite popular among humans.",]
    ],
    [
        r"do you dream?",
        ["I don't dream, but I'm here to help you achieve your goals. What can I assist you with?",]
    ],
    [
        r"tell me about artificial intelligence",
        ["Artificial Intelligence (AI) is the simulation of human intelligence in machines. It involves tasks like learning, reasoning, and problem-solving.",]
    ],
    [
        r"tell me a programming joke",
        ["Why do programmers prefer dark mode? Because light attracts bugs!",]
    ],
    [
        r"who created you?",
        ["I was created by a team of developers working with OpenAI.",]
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
