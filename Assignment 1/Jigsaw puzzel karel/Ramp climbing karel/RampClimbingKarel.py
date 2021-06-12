from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""
#fuction too turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#to draw a diagonal line using beepers
def climb():
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
#main function
def main():
    put_beeper()
    while front_is_clear():
      climb()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
