import time,threading
#练习线程的semaphore函数
def run (n):
        semaphore.acquire()
        time.sleep(1)
        print("run the thread:%s" % n)

        semaphore.release()

if __name__ == '__main__':
        num = 0
        semaphore = threading.Semaphore(2)
        for i in range(20):
                t = threading.Thread(target=run,args=(i,))
                t.start()

while threading.active_count() != 1:
        pass
else:
        print('---all threads.active_count---')
        print(num)

#运行结果
'''
run the thread:0
run the thread:1
run the thread:2
run the thread:3
run the thread:4
run the thread:5
run the thread:6
run the thread:7
run the thread:8
run the thread:9
run the thread:10
run the thread:11
run the thread:12
run the thread:13
run the thread:14
run the thread:15
run the thread:16
run the thread:17
run the thread:18
run the thread:19
---all threads.active_count---
0
'''
