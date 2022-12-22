import threading
import random
import time
from inputimeout import inputimeout, TimeoutOccurred
import keyboard


class Rand:
  def __init__(self):
    self.number = 0
    self.cond = threading.Condition()

  # Performs thread communication
  # Also blocks user numbers on a keyboard, so it can't type if
  # guessed a wrogn number, unblocks after pause. Doesnt block letters tho cus its a little bit
  # overkill for this tiny project
  def block(self):
    self.cond.acquire()
    for i in range(10):
      keyboard.block_key(i)
    self.cond.wait()
    for i in range(10):
      keyboard.unblock_key(i)
    self.cond.release()

  def changer(self):
    while True:
      self.cond.acquire()
      self.number = random.randint(1, 5)
      print(f'\n~~~Number\'s changed~~~ (Press "q" to quit)')
      self.cond.notify()
      self.cond.release()
      time.sleep(3)

  def user(self):
    while True:
      try:
        # terminates user input thread after given anoun of time
        inp = inputimeout(prompt='Guess: ', timeout=2.95)
        if inp == 'q':
          print('Terminated')
          quit()
        else:
          inp = int(inp)
      except (TimeoutOccurred, ValueError):
          print('Session expired or wrong input!')
          self.block()
      else:
        if inp == self.number:
          print(f'Number was: {self.number}, congrats!')
          quit()
        else:
          print('Almost...')
          self.block()

obj1 = Rand()

x = threading.Thread(target=obj1.changer, daemon=True)
y = threading.Thread(target=obj1.user)

print('Guess a random number from 1 up to 5. You will be given a new random number per iteration')

x.start()
y.start()
