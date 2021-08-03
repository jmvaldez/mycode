#!/usr/bin/env python3

import requests

def yes_no_question(question):
    user_answer = input(question).lower()
    if user_answer == "yes" or user_answer == "no":
        return user_answer
    else:
        return yesNoQuestion(question)

def main():
     url = "https://api.kanye.rest"
     request_status = requests.get(url).status_code
     while request_status == 200:
         try:
            user_wants_kanye = yes_no_question("Are you ready for some Kanye inspo? Yes or No?")
            if user_wants_kanye == "yes":
                response = requests.get(url).json()
                print(response.get("quote"))
                more_quotes_please = yes_no_question("Do you need more inspo? Yes or No?")
                if more_quotes_please == "yes":
                    response = requests.get(url).json()
                    print(response.get("quote"))
                    more_quotes_please = yes_no_question("Do you need more inspo? Yes or No?")
                elif more_quotes_please == "no":
                    response = requests.get(url).json()
                    print("Too bad... Yeezy gonna give it to ya anyway")
                    print(response.get("quote"))
                    break
            else:
                print("Kanye West says bye.")
         except:
             print("Request returned an error.")

if __name__ == "__main__":
    main()
