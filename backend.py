import openai

class Chatbot:
    def __init__(self):
        openai.api_key = ""
        #openai.api_key should be added when using

    def get_response(self,user_input):
        response = openai.Completion.create(
            engine="text-embedding-ada-002",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5  #Diveristy of AI's answer
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)