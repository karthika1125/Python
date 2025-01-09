# import threading
# import time
# def print_name(name,*args):
#     print(name,*args)
# name="Avenger  "
# th1=threading.Thread(target=print_name,args=(name,1))
# th2=threading.Thread(target=print_name,args=(name,1,2))
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print("Thread are finshed ....")


# import threading
# def print_sqr(num):
#     print("square : {}".format(num*num))
# def print_cube(x):
#     print("cube: {}".format(x*x*x))
# def print_sum(num1,num2):
#     print("sum : {}".format(num1+num2))
# if __name__=="__main__":
#     t1=threading.Thread(target=print_sqr,args=(5,))
#     t2=threading.Thread(target=print_cube,args=(9,))
#     t3=threading.Thread(target=print_sum,args=(5,6))
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     t2.join()
#     t3.join()
# print("This is done ....")


