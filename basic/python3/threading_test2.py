import threading
import time

"""
线程同步
"""

class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程:" + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print('end')