import time 
import numpy as np

class Timer():
    def __init__(self):
        """Constructor"""
        self.tik = None # 保存一个时间戳
        self.times = [] # 记录多次运行时间
        self.start()

    def start(self):
        self.tik = time.time() 

    def stop(self):
        """停止计时并将时间记录在列表中"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self):
        """returns average time"""
        return sum(self.times) / len(self.times)

    def sum(self):
        """returns total time"""
        return sum(self.times)

    def cumsum(self):
        """returns cumulative sum"""
        return np.array(self.times).cumsum().tolist()

if __name__ == "__main__":
    timer = Timer()
    s = 0
    for i in range(10000):
        s += i
    timer.stop()
    timer.start()
    for i in range(1000000):
        s += i
    timer.stop()
    timer.start()
    for i in range(100000000):
        s += i
    timer.stop()

    print(timer.times)
    print(timer.avg())
    print(timer.sum())
    print(timer.cumsum())