#threading
from random import randint, random
import threading
import time
from unittest import result

def thread_function(name, times, results, i):
    time.sleep(times)
    print(randint(0,10))
    results[i] = randint(0,10)

def main():
    t = []
    results = [0] * 10
    for i in range(10):
        t.append(threading.Thread(target=thread_function, args=("Thread "+str(i),2,results,i)))
        t[-1].start()
    # when all threads are done, join them
    for i in range(10):
        t[i].join()
    # get the return value from the threads
    for i in range(10):
        print(t[i])
    print("Done!")

main()