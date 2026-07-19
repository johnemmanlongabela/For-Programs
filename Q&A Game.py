import random
from termcolor import cprint

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"

def ask_question(index, question,options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)

    return input('Your answer: ').upper().strip()

def run_quiz(quiz):
    random.shuffle(quiz)

    score = 0

    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION],item[OPTIONS])

        if answer == item[ANSWER]:
            cprint("Correct!", "green")
            score += 1
        else:
            cprint("Wrong! The correct answer is {item[ANSWER]}", "red")

        print()

    print(f'total score: {score} out of {len(quiz)}')

def main():
    quiz = [
        { QUESTION: 'What is the tallest mountain in the world above sea level?',
          OPTIONS:['A. K2, B. Mount Everest, C. Mount Kilimanjaro, D. Mount Fuji'],
          ANSWER:'B'},

        {QUESTION: 'Mayon Volcano, known for its perfectly symmetrical cone, is located in which province near you?',
         OPTIONS: ['A. Albay, B. Sorsogon, C. Camarines Sur, D. Catanduanes'],
         ANSWER: 'A' },

        {QUESTION: ' What is the chemical symbol for water?',
         OPTIONS: ['A. O₂, B. CO₂, C. H₂O, D. NaCl'],
         ANSWER: 'C'},

        {QUESTION: 'Who is considered the national hero of the Philippines?',
         OPTIONS:  ['A. Andres Bonifacio, B. Emilio Aguinaldo, C. Jose Rizal, D. Apolinario Mabini'],
         ANSWER: 'C'},

        {QUESTION: 'Which planet is commonly known as the Red Planet?',
         OPTIONS: ['A. Venus, B. Mars, C. Jupiter, D. Saturn'],
         ANSWER: 'B'},

        {QUESTION: 'Which date is celebrated as Philippine Independence Day?',
         OPTIONS: ['A. June 12, B. July 4, C. April 9, D. November 30'],
         ANSWER: 'A'},

        {QUESTION: 'What is the hardest natural substance on Earth?',
         OPTIONS: ['A. Gold, B. Iron, C. Quartz, D. Diamond'],
         ANSWER: 'D'},

        {QUESTION: 'What is the official residence of the President of the Philippines?',
         OPTIONS: ['A. Malacañang Palace, B. The White House, C. Fort Santiago, D. Quezon City Hall'],
         ANSWER: 'A'},

        {QUESTION: 'Which gas do plants primarily absorb from the atmosphere?',
         OPTIONS: ['A. Oxygen, B. Hydrogen, C. Carbon dioxide, D. Nitrogen'],
         ANSWER: 'C'},

        {QUESTION: ' What is the largest ocean on Earth?',
         OPTIONS: ['A. Atlantic Ocean, B. Indian Ocean, C. Pacific Ocean, D. Arctic Ocean'],
         ANSWER: 'C'}
    ]
    run_quiz(quiz)

if __name__ == '__main__':
    main()

