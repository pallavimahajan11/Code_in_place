"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 


def main():
    num1=random.randint(10,99)
    num2=random.randint(10,99)
    print("What is "+str(num1)+"+"+str(num2)+"?")
    sum=num1+num2
    x=int(input())
    if sum==x:
        print("correct answer!",sum)
    else:
        print("Your answer:",x)
        print("Incorrect.","The expected answer is",sum)

if __name__ == '__main__':
    main()
