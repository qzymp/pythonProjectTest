import time
def outp(func):
    def warp(*args,**kwargs):
        start = time.time()
        print(*args)
        res = func(*args , **kwargs)
        print(res)
        end = time.time()
        print(end - start)
        return res
    return warp

@outp
def indise(x,y):
    print(f'{x}的数值')
    time.sleep(y)
    print(f'sleep {y}的数值')
@outp
def indise2(num,test):
    print(f'{num}的数值')
    time.sleep(test)
    print(f'sleep{test}的数值')

indise(1,2)
# indise2(2,1)

# print(indise(1, 2))
# print(outp)

#*args   （[1,2,3]）   (1,2,3)