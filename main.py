from bardapi import Bard
import os


token = os.environ['BARD_API_KEY']
# = "bwjmGW3gnkzi1lGTxTXXeMQjel9EAtqAze361DMi5wGbeD-zX4aASLeAqoRDukjd_Ee1eQ."


if __name__ == "__main__":
    print("\nWelcome to A-ARD; Alister's version of the Google Chatbot, BARD\n==============================================================\nNote: Type 'bye', 'exit' or 'quit' to exit the app.\n")
    while True:
        input_prompt = input("You: ")
        print()
        if input_prompt.lower() in ["quit", "exit", "bye"]:
            break
        # response = AlisterGPT(inpuT)
        response = Bard(token=token).get_answer(input_prompt)['content']
        print("A-ARD: ", response, "\n")