import json
import random
    
def get_question(quiz_data):
    print(quiz_data["question"])
    for i, choice in enumerate(quiz_data["choices"], 1):
        print(f"{i}) {choice}")

def get_answer():
    while True:
        choice = int(input("Enter your answer (1/2/3/4): "))
        if choice in (1,2,3,4):
            return str(choice)
        else:
            print("Invalid choice. Please choose from 1,2,3,4")

def check_answer(quiz_data, answer):
    return answer == quiz_data["correct_ans"]

def main():

    file_path = "quiz_data.json"
    with open(file_path, 'r') as f:
        questions = json.load(f)
    
    total_questions = 10
    num_questions = int(input("Enter number of questions that you wish to enter between 1 and 10: "))
    if(num_questions > 10 or num_questions < 1):
        print("Please restart the program and enter a number between 1 and 10.")
        exit()

    score = 0

    random_questions = random.sample(questions, num_questions)

    print("Welcome to the MCQ Quiz!\n")

    for i, quiz_data in enumerate(random_questions, 1):
        print(f"Question {i}/{num_questions}: ")
        get_question(quiz_data)
        answer = get_answer()
        if check_answer(quiz_data, answer)==True:
            print("Correct answer!\n")
            score+=1
        else:
            print(f"Wrong answer! The correct answer is {quiz_data['choices'][int(quiz_data['correct_ans']) - 1]}.\n")

    print(f"MCQ Complete! Your total score is: {score}/{num_questions}")

if __name__=="__main__":
    main()
