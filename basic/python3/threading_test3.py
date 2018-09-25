import queue
import threading
import time

exit_flag = 0


class my_thread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("start:" + self.name)
        process_data(self.name, self.q)
        print("end:" + self.name)


def process_data(thread_name, q):
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print("%s processing %s" % (thread_name, data))
        else:
            queue_lock.release()
        time.sleep(1)


thread_list = ["thread-1", "thread-2", "thread-3"]
name_list = ["one", "two", "three", "four", "five"]
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
thread_id = 1

for t_name in thread_list:
    thread = my_thread(thread_id, t_name, work_queue)
    thread.start()
    threads.append(thread)
    thread_id += 1

queue_lock.acquire()
for word in name_list:
    work_queue.put(word)
queue_lock.release()

while not work_queue.empty():
    pass

exit_flag = 1

for t in threads:
    t.join()

print("end")
