"""
TODO: Write a description here
"""

import random

def main():
   stones=20
   print("There are 20 stones left")
   while stones !=0:
    num=int(input("Player 1 would you like to remove 1 or 2 stones? "))
    if num==1:
        stones=stones-1
    elif num==2:
        stones=stones-2
    else:
        num=int(input("Please enter 1 or 2: "))
        if num==1:
         stones=stones-1
        elif num==2:
         stones=stones-2
    if stones==0:
        print()
        print("Player 2 wins!")
        break
    print()    
    print("There are "+str(stones)+" stones left")
    if stones !=0:
     num=int(input("Player 2 would you like to remove 1 or 2 stones? "))
     if num==1:
        stones=stones-1
     elif num==2:
        stones=stones-2
     else:
        num=int(input("Please enter 1 or 2: "))
        if num==1:
         stones=stones-1
        elif num==2:
          stones=stones-2
     if stones==0:
        print()
        print("Player 1 wins!")
        break
     print()
     print("There are "+str(stones)+ " stones left")
if __name__ == '__main__':
    main()
