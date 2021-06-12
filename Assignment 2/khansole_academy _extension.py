"""
TODO: Give the answer of randomly asked addition questions.
you'll be considered as master in Addition if you'll give 3 correct answer in a row. 
"""

import random
MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    khansole_academy_extention()

def khansole_academy_extention():
    # initial score of correct answer.
    correct_score = 0
    """
    THis loop will give random addition problem until the score is 3. 
    """
    while correct_score <= 2:
        first_random = random.randint(MIN_RANDOM,MAX_RANDOM)
        second_random = random.randint(MIN_RANDOM,MAX_RANDOM)
        result = first_random + second_random
        print("What is "+str(first_random)+"+"+str(second_random)+" ?")

        # Taking input as an answer of given random addition maths         
        answer = int(input("Your answer: "))
        """
         checking answer is correct or not, if answer is correct then the score is increased by 1
            if answer is wrong then score will be become zero by multipling by 0 to the previous score.
        """
        if result == answer:
            print("Correct! 👍")
            correct_score += 1
        else:
            print("Incorrect. The expected answer is "+ str(result))
            correct_score *= 0
    print("Congratulations! You mastered addition.")
    print("Correct! You've gotten 3 correct in a row.")

if __name__ == '__main__':
    main()

