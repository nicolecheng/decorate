import time
# time.time()

#closure = wrapper(foo)
#closure( -2, 3, 'hello' ) #will run foo with the arguments -2, 3, 'hello' through wrapper

def time_fxn(f):
    def inner (*arg):
        start = time.time()
        f(*arg)
        return "run time: " + str(time.time()-start)
    return inner

def fxn_info(f):
    def inner( *arg ):
        return f.func_name + str(arg)
    return inner 

@fxn_info
def foo(a, b, c):
    return str(a)+str(b)+c

@time_fxn
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

#c = fxn_info(foo)
print foo(3,4,"a")
print fib(30)
