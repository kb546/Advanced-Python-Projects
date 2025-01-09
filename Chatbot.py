from textblob import TextBlob

#Define intents and their corresponding responses based on keywords
intents = {
    "hours":{
        "keywords":["hours", "open", "close"],
        "response": "We are open from 9 AM to 5 PM, Monday to Friday."
    }
    "return":{
        "keywords":["Refund", "money back", "return"],
        "response": "I'de be happy to help you with the return process. Let me transfer you to a live agent."
    }
}

def get_response(message):
    #Convert the message to lowercase for consistent keyword matching
    message = message.lower()
    #Check if the message containts any keywords assocciated with defined intents.
    if any(word in message for word in intent_data["keywords"]):
        #return the corresponding response if a keyword matches
        return intent_data["response"]
    #Analyze the sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity

    # Return a response based on the sentiment score
    return ("That's so great to hear!" if sentiment > 0 else 
            "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
            "I see. Can you tell me more about that?")

def chat():
    #Greet the user and prompt for input
    print("Chatbot: Hi, How can I help you today?")
    # Continiously prompt the suer for input until they choose to exit
    while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        #Get and print the chatbot's response based on user input
        print(f"/nChatBot: {get_response(user_message)}")

    #Thank the user for chatting when they exit
    print("ChatBot: Thank you chatting. Have a great day!")
if __name__ == "__main__":
    chat() #Start the chat when the script is executed