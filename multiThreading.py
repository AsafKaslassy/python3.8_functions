import threading
import time


def dance(text, sema):
  """
  Calling this method a loop that prints out the name of the dancer
  together with the 'is dancing' text should execute 20 iterations.
  Create a list of 20 Dancer objects and simulate a scenario in which
  at any given time there no more than 3 dancers dancing in our club.
  Use the Semaphor class to ensure that.
  """
  sema.acquire()
  i = 1
  while i<20:
    print(threading.current_thread().getName(),text,"is dancing")
    time.sleep(1)
    i += 1
  sema.release()

semaphore = threading.Semaphore(3)
number_of_threads = 20
for dancer_name in [
                    'Dancer1','Dancer2','Dancer3','Dancer4','Dancer5',
                    'Dancer6','Dancer7','Dancer8','Dancer9','Dancer10',
                    'Dancer11','Dancer12','Dancer13','Dancer14','Dancer15',
                    'Dancer16','Dancer17','Dancer18','Dancer19','Dancer20'
                    ]:
 dancer_thread = threading.Thread(target=dance, args=(dancer_name, semaphore))
 dancer_thread.name = ''
 # dancer_thread.start()

# __________________________________________________________________________________ #


def printTxt(txt):
    """
    simple application that prints out 20 times the word 'Bonga'
    and 20 times the word 'Kaponga'. The printing of these two words
    should be performed using the same method. It should be a method that
    will be concurrently invoked using two separated Timer objects.
    """
    for i in range(20):
        print(txt)
# timer1thread = threading.Timer(1,printTxt,args=['Bonga'])
# timer1thread.start()
# timer2thread = threading.Timer(2,printTxt,args=['Kaponga'])
# timer2thread.start()



#________________________________

"""
Develop a simple application that uses three separated threads for creating the three strings: 'We', 'Love' and 'Python' using the following lists:

['w','e']
['l','o','v','e']
['p','y','t','h','o','n']

When the three threads end one of them should sum up the three words into a single string.
"""

from functools import reduce

def concat():
    word1 = ['w','e']
    word2 = ['l','o','v','e']
    word3 = ['p','y','t','h','o','n']
    out_str = str(reduce(lambda x,y: x+""+y, word1+word2+word3))
    print(out_str)

concat()

#
# barrier = threading.Barrier(3)
#
# class thread(threading.Thread):
#     def __init__(self, thread_ID):
#         threading.Thread.__init__(self)
#         self.thread_ID = thread_ID
#
#
#     def run(self):
#         word1 = ['w','e']
#         word2 = ['l','o','v','e']
#         word3 = ['p','y','t','h','o','n']
#
#         print(word1,word2,word3)
#         barrier.wait()
#
#
#     def sum_words(self):
#
#
# thread1 = thread(100)
# thread2 = thread(101)
#
# thread1.start()
# thread2.start()
# barrier.wait()
#
# print("Exit\n")