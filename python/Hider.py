import threading,time

#捉迷藏游戏，使用notify、wait等线程函数
def Seeker(cond,name):
        time.sleep(2)
        cond.acquire()
        print('%s : 我已经把眼睛蒙上了！' % name)
        cond.notify()
        cond.wait()
        for i in range(3):
                print('%s is finding!!!' % name)
                time.sleep(2)
        cond.notify()
        cond.release()
        print('%s : 我赢了！！' % name)

def Hider(cond,name):
        cond.acquire()
        cond.wait()
        for i in range(2):
                print('%s is hiding' % name)
                time.sleep(3)
        print('%s : 我已经开始藏了！' % name)
        cond.notify()
        cond.wait()
        cond.release()
        print('%s:被你找到了~' % name)

if __name__ == '__main__':
        cond = threading.Condition()
        seeker = threading.Thread(target=Seeker,args=(cond,'seeker'))
        hider = threading.Thread(target=Hider,args=(cond,'hider'))
        seeker.start()
        hider.start()
