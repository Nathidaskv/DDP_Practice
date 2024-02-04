"""
#Practicing how to make choices in python

def add(x, y):
    # Implement addition here
    return x + y

def subtract(x, y):
    # Implement subtraction here
    return x - y

def multiply(x, y):
    # Implement multiplication here
    return x * y

def divide(x, y):
    # Implement division here
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def main():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        result = "Invalid input"

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
"""


import random

class EnglishTest:
    def __init__(self):
        self.questions = {
            1: {
                "question": "What is the capital of France?",
                "choices": [
                    "A. Berlin",
                    "B. Madrid",
                    "C. London",
                    "D. Paris"
                ],
                "correct_choice": "D"
            },
            2: {
                "question": "Which of these is a mammal?",
                "choices": [
                    "A. Snake",
                    "B. Fish",
                    "C. Eagle",
                    "D. Dog"
                ],
                "correct_choice": "D"
            },
            3: {
                "question": "What is the largest planet in our solar system?",
                "choices": [
                    "A. Earth",
                    "B. Mars",
                    "C. Jupiter",
                    "D. Saturn"
                ],
                "correct_choice": "C"
            },
            # Add more questions here...
        }

    def generate_test(self, num_questions=5):
        question_ids = list(self.questions.keys())  # Convert keys to a list
        selected_questions = random.sample(question_ids, num_questions)
        return [self.questions[q_id] for q_id in selected_questions]

    def grade_test(self, user_answers):
        score = 0
        total_questions = len(user_answers)

        for i, (user_answer, question_info) in enumerate(zip(user_answers, self.questions.values()), start=1):
            question = question_info["question"]
            correct_choice = question_info["correct_choice"]

            print(f"\nQuestion {i}:")
            print(question)
            print(f"Your answer: {user_answer}")
            print(f"Correct answer: {correct_choice}")

            if user_answer == correct_choice:
                print("Your answer is correct!\n")
                score += 1
            else:
                print("Sorry, your answer is incorrect.\n")

        percentage_score = (score / total_questions) * 100
        print(f"Your score: {score}/{total_questions} ({percentage_score:.2f}%)")

def main():
    english_test = EnglishTest()
    
    # Generate a test sheet with 3 questions (you can change this number)
    num_questions = 3
    
    test_sheet = english_test.generate_test(num_questions)

    user_answers = []
    for i, question_info in enumerate(test_sheet, start=1):
        choices = question_info["choices"]
        print(f"\nQuestion {i}:")
        print(question_info["question"])
        for j, choice in enumerate(choices, start=1):
            print(f"{choice}")
            print(f"{j}. {choice}")
        user_answer = input(f"Select the correct choice (A/B/C/D) for Question {i}: ")
        user_answers.append(user_answer.upper())

    english_test.grade_test(user_answers)

if __name__ == "__main__":
    main()
