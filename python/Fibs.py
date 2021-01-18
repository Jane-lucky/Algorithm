#斐波那契数列
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self #实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a,self.b = self.b,self .a + self.b
        if self.a > 100000:
            raise StopIteration();
        return self.a
'''
class Fib(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a + b
        return a
'''
if __name__ == "__main__":
    for n in Fib():
        print(n)