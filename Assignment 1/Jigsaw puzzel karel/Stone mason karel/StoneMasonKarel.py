from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
  while front_is_clear():
    fill_up()
    move_twice()
  if front_is_blocked():
   fill_up()

def fill_up():
  turn_left()
  while front_is_clear():
    if beepers_present():
      pass
    else:
      put_beeper()
    move()
  if front_is_blocked():
      if beepers_present():
        pass
      else:
        put_beeper()
      turn_left()
      turn_left()
      while front_is_clear():
        move() 
      turn_left()
def move_twice():
  for i in range(4):
    move()    

if __name__ == '__main__':
 run_karel_program('SampleQuad2.w')
