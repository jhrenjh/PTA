def myf(f):
    def inner(*args,**kwargs):
        print("myf start\n")
        ret=f(*args,**kwargs)
        print("myf end\n")
        return ret
    return inner
@myf #index=myf(index)
def index(m,n):
    print("from index function %d %d\n"%(m,n))
    return (m+n)
print(index(1,2))