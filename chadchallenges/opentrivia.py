#!/usr/bin/env python3

import requests as req

def main():
    trivia_url = "https://opentdb.com/api.php?amount=5&category=15&difficulty=medium&type=multiple"
    
    trivia_response = req.get(trivia_url)

    if trivia_response:
        json_response = trivia_response.json()
        for item in json_response.get('results'):
                questions = item.get('question')
                correct_answers = item.get('correct_answer')
                incorrect_answers = item.get('incorrect_answers')
                first_question = input(questions)
                print(correct_answers)
    else:
        print('Err')

main()
