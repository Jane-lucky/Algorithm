'''def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print("[DEBUG]:enter {} []".format(caller_name))

def say_hello():
    debug()
    print ("Hello!")

def say_goodbye():
    debug()
    print ("Hello!")

if __name__ == "__main__":
    say_hello()
    say_goodbye()
'''
def debug(func):
    def wrapper():
        print("DEBUG:enter {}()".format.__name__)
        return func()
    return wrapper

@debug
def say_hello():
    print ("Hello")

if __name__ == "__main__":
    say_hello()