from threading import Thread, Lock
import time

st = time.time()
class foo:

    def __init__(self, v, l):
        self.l = l
        self.l.acquire()
        self.name = "ajju"
        self.val = v
        if self.val == 1:
            self.display()
        if self.val == 2:
            self.re()
        self.l.release()
    def display(self):
        print("starting 1")
        time.sleep(3)
        print("ended 1 ")
    def re(self):
        print("starting 2")
        time.sleep(3)
        print("ended 2 ")

lock = Lock()

obj1 = Thread(target=foo, args=(1, lock))
obj2 = Thread(target=foo, args=(2, lock))
obj1.start()
obj2.start()

# obj1.join()
# obj2.join()

print("execution time:", time.time()-st)