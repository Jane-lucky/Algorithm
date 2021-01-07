import time,threading
import random

#红绿灯的例子，即起动一个线程做交通指挥灯，生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则
def light():
    if not event.isSet():
        event.set()
    count=0
    while True:
        if count < 10:
            print('\033[42;1m---green light on---\033[0m')
        elif count < 13:
            print('\033[43;1m---yellow light on---\033[0m')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('\033[41;1m---red light on---\033[0m')
        else:
            count = 0
            event.set() #打开绿灯
        time.sleep(1)
        count+=1

def car(n):
    while 1:
        time.sleep(random.randrange(3,10))
        if event.isSet():
            print("car [%s] id running..." % n)
        else:
            print("car [%s] is waiting for red light..." % n)
            event.wait() #红灯状态下wait阻塞，汽车等待状态

if __name__ == '__main__':
    car_list = ['BMW','AUID',"SANTANA"]
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in car_list:
        t = threading.Thread(target=car,args=(i,))
        t.start()