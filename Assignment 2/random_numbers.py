"""
Prints out 10 random numbers between 0 and 100.
"""
MIN_RANDOM=0
MAX_RANDOM =100
NUM_RANDOM=10
import random
def RANDOM():
    
    for i in range(NUM_RANDOM):
       x=random.randint(MIN_RANDOM,MAX_RANDOM)
       print(x)
def main():
    RANDOM()

if __name__ == '__main__':
    main()
