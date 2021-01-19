# coding=utf-8

import threading
from time import ctime, sleep


class SimpleThread(threading.Thread):

    def __init__(self,func,args={}):
        super(SimpleThread,self).__init__()
        self.func = func # 执行函数
        self.args = args # 执行参数，其中包含切分后的数据块，字典类型

    def run(self):
        self.result = self.func(**self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None

def add(a, b):
	#print ('a+b:', a+b)
	return a+b

if __name__ == '__main__':
    threads = []
    loops = 10
    for i in range(loops):
        t = SimpleThread(add, {'a':i,'b':i})
        threads.append(t)
    for i in range(loops):   # start threads 此处并不会执行线程，而是将任务分发到每个线程，同步线程。等同步完成后再开始执行start方法
        threads[i].start()
    for i in range(loops):   # jion()方法等待线程完成
        threads[i].join()
        print(threads[i].get_result())