from bardapi import Bard
import os


# os.environ['_BARD_API_KEY'] = os.environ['BARD_API_KEY']
# os.environ['_BARD_API_KEY'] = ${{ secrets.BARD_API_KEY }}
token = os.environ['API_KEY']
# token = ${{ secrets.BARD_API_KEY }}
# os.environ['_BARD_API_KEY'] = ""


if __name__ == "__main__":
    print("\nWelcome to A-ARD; Alister's version of the Google Chatbot, BARD\n==============================================================\nNote: Type 'bye', 'exit' or 'quit' to exit the app.\n")
    while True:
        input_prompt = input("You: ")
        print()
        print(token)
        if input_prompt.lower() in ["quit", "exit", "bye"]:
            break
        # response = AlisterGPT(inpuT)
        response = Bard().get_answer(input_prompt)['content']
        print("A-ARD: ", response, "\n")