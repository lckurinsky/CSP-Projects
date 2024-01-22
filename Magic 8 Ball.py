#Lily Kurinsky
#1/22
#Magic 8 Ball
import random

responses = ["Yes", "No", "Maybe", "Can't Be Determined", "Absolutely!","Definetely Not", "Don't Count On It", "It's Looking Good", "Ask Again Later", "I'm Thinking No"]
print("Hello! Welcome to Magic 8 Ball.")
while True:
    ask = input("Please ask a yes-or-no question.")
    if ask.endswith("?"):
        print(random.choice(responses))
        again = input("Would you like to ask another question? (yes or no)")
        if (again == "no"):
            print("Program ended.")
            break
    else:
        print("No question detected. Please re-enter your question.")