import time

#-----------------------------------------beta1-------------------------------------------
# def index():
#     time.sleep(2)
# start_time=time.time()
# index()
# end_time=time.time()
# print(end_time-start_time)
#-----------------------------------------beta2------------------------------------------
# def index():
#     time.sleep(2)
# def calculate_time():
#     start_time=time.time()
#     index()
#     end_time=time.time()
#     print(end_time-start_time)
# calculate_time()
#-----------------------------------------beta3-------------------------------------------
# def index():
#     time.sleep(2)
# def calculate_time(f):
#     start_time=time.time()
#     f()
#     end_time=time.time()
#     print(end_time-start_time)
# calculate_time(index)
#-----------------------------------------beta4-------------------------------------------
# def index():
#     time.sleep(2)
# def calculate_time(f):
#     def inner():
#         start_time=time.time()
#         f()
#         end_time=time.time()
#         print(end_time-start_time)
#     return inner
# #calculate_time(index) equal inner
#calculate_time(index)()
#-----------------------------------------beta5-------------------------------------------
# def index():
#     time.sleep(2)
# def calculate_time(f):
#     def inner():
#         start_time=time.time()
#         f()
#         end_time=time.time()
#         print(end_time-start_time)
#     return inner
# #calculate_time(index) equal inner
# index=calculate_time(index)
# index()
#-----------------------------------------beta6-------------------------------------------
# @calculate_time # equal index=calculate_time(index)
# #NameError: name 'calculate_time' is not defined
# def index():
#     time.sleep(2)
# def calculate_time(f):
#     def inner():
#         start_time=time.time()
#         f()
#         end_time=time.time()
#         print(end_time-start_time)
#     return inner
# #calculate_time(index) equal inner
# index()
#-----------------------------------------beta7-------------------------------------------
# def calculate_time(f):
#     def inner():
#         start_time=time.time()
#         f()
#         end_time=time.time()
#         print(end_time-start_time)
#     return inner
# @calculate_time # equal index=calculate_time(index)
# def index():
#     time.sleep(2)
# #calculate_time(index) equal inner
# #index=calculate_time(index)
# index()
#-----------------------------------------beta9-------------------------------------------
# def calculate_time(f):
#     def inner():
#         start_time=time.time()
#         ret=f()
#         end_time=time.time()
#         print(end_time-start_time)
#         return ret
#     return inner
# @calculate_time # equal index=calculate_time(index)
# def index():
#     time.sleep(2)
# #calculate_time(index) equal inner
# #index()
# print(index())
#-----------------------------------------beta10-------------------------------------------
# def calculate_time(f):
#     def inner():
#         start_time=time.time()
#         ret=f()
#         end_time=time.time()
#         print(end_time-start_time)
#         return ret
#     return inner
# @calculate_time # equal index=calculate_time(index)
# def index():
#     time.sleep(2)
#     return "rjh"
# #calculate_time(index) equal inner
# #index()
# print(index())
#-----------------------------------------beta11-------------------------------------------
def calculate_time(f):
    def inner(*args,**kwargs):
        start_time=time.time()
        ret=f(*args,**kwargs)
        end_time=time.time()
        print(end_time-start_time)
        return ret
    return inner
@calculate_time # equal index=calculate_time(index)
def add(m,n):
    time.sleep(2)
    return m+n
#calculate_time(index) equal inner
#index()
print(add(1,2))