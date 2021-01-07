import time,threading

#使用lock的时候，启动两个线程的结果
#其中acquire和release成对出现

balance = 0
lock = threading.Lock()
def change_it(n):
        global balance
        balance = balance + n
        balance = balance - n

def run_thread(n):
        for i in range(2000000):
                lock.acquire()
                try:
                        change_it(n)
                finally:
                        lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
