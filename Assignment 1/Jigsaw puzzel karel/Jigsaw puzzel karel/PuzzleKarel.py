from karel.stanfordkarel import *
def move_3blocks():
 move()
 move()
 move()
def turn_right():
 turn_left()
 turn_left()
 turn_left()
def turn_back():
 turn_left()
 turn_left()
def move_twice():
    move()
    move()

def main():
 move_twice()
 pick_beeper()
 move()
 turn_left()
 move_twice()
 put_beeper()
 turn_back()
 move_twice()
 turn_right()
 move_3blocks()
 turn_back()
 
if __name__ == '__main__':
    run_karel_program('Puzzle.w')
