Q1

import random

def display_scenario():
    print("welcome to the treasure hunt")
    scenario = random.choice(['forest', 'quiz'])
    if scenario == 'forest':
        forest_scenario()
    else:
        quiz_scenario()  

def forest_scenario():
    print("\nyou have been assigned to the forest")

    fruits = ['banana', 'apple', 'strawberry', 'blueberry', 'orange']
    guessed_fruits = set()
    while len(guessed_fruits) < 5:
        guess = input("guess a fruit: ").lower()
        if guess in fruits:
            guessed_fruits.add(guess)
            print(f"correct! You have guessed {len(guessed_fruits)} fruit(s).")
        else:
            print("Incorrect. Try again.")

        print(f"Guessed fruits: {', '.join(guessed_fruits)}")
    print("you have guessed all the fruits correctly, you may proceed.")
    

    height = int(input("\nenter your height: "))
    if height <= 160:
        print("you drowned in the river. game over!")
        return
    elif height > 180:
        print("the tiger spotted you too easily. game over!")
        return
    else:
        print("you crossed the river safely. you may proceed.")
    

    password = [random.randint(0, 9) for _ in range(4)]
    attempts = 10
    print("\na door is locked with a 4 digit password. you have 10 chances to guess it.")
    
    while attempts > 0:
        guess = input("enter your 4-digit guess: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. please enter exactly 4 digits.")
            continue
        
        guess_list = [int(d) for d in guess]
        correct_count = sum(g == p for g, p in zip(guess_list, password))
        
        if correct_count == 4:
            print("congratulations! You've guessed the password correctly. you win!")
            break
        
        print(f"you have {correct_count} correct numbers.")
        attempts -= 1
        print(f"you have {attempts} attempts left.")
    
    if attempts == 0:
        print("sorry, you've run out of attempts. the correct password was:", ''.join(map(str, password)))

def quiz_scenario():

    print("You are in the quiz scenario. This part is not implemented yet.")
    
if __name__ == "__main__":
    display_scenario()

Q 2:

print("\nwelcome to the python quiz!")

questions = [
    {
        'question': "What is the keyword used to define a function in Python?",
        'options': ['function', 'def', 'func', 'define'],
        'answer': 'def'
    },
    {
        'question': "How do you insert comments in Python?",
        'options': ['#', '//', '--', '/*'],
        'answer': '#'
    },
    {
        'question': "Which of the following is a mutable data type?",
        'options': ['tuple', 'list', 'str', 'int'],
        'answer': 'list'
    },
    {
        'question': "What symbol is used for exponentiation in Python?",
        'options': ['^', '**', '//', '%'],
        'answer': '**'
    },
    {
        'question': "Which function is used to get the length of a list in Python?",
        'options': ['len()', 'length()', 'size()', 'count()'],
        'answer': 'len()'
    },
    {
        'question': "How do you write a conditional statement in Python?",
        'options': ['if condition:', 'if condition then:', 'condition if:', 'when condition:'],
        'answer': 'if condition:'
    }
]

score = 0

for q in questions:
    print("\n" + q['question'])
    for i, option in enumerate(q['options']):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            answer = int(input("Enter the number of your choice: ")) - 1
            if 0 <= answer < len(q['options']):
                if q['options'][answer] == q['answer']:
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect.")
                break
            else:
                print("Invalid choice. Please choose a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

total_questions = len(questions)
incorrect_answers = total_questions - score
percentage = (score / total_questions) * 100

print("\nQuiz Results:")
print(f"Questions answered correctly: {score}")
print(f"Questions answered incorrectly: {incorrect_answers}")
print(f"Percentage: {percentage:.2f}%")

if score == 6:
    print("Congratulations! You got a perfect score!")
elif score >= 4:
    print("Great job! You did very well.")
elif score >= 2:
    print("Good effort! You got a few right.")
else:
    print("You could do better. Keep practicing! (noob) ")
