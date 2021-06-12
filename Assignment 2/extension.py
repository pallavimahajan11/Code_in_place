"""
TODO: Write a description here
"""

import random 

def main():
 count=0
 num=int(input("Enter a num: "))
 while num!=1:
    if num%2!=0:
        print(num,"is odd , so I make 3n+1:",3*num+1)
        num=3*num+1
        count+=1
    else:
        print(num,"is even , so I take half",num//2)
        num=num//2
        count+=1
 print("The process took "+str(count)+" steps to reach 1")
if __name__ == "__main__":
    main()
