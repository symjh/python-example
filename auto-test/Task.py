import time

import logins
import datetime

def_time = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000,170000]

def loopMonitor():



    while True:
        now = datetime.datetime.now();
        nowTime = int(now.strftime("%H%M%S"))
        for i in range(0,24):
            if(i*10000 <= nowTime <= i*10000+100):
                print("任务开始,当前时间"+now.strftime("%Y-%m-%d %H:%M:%S"))
                logins.login()
        #2s检查一次
        time.sleep(60)

if __name__ == '__main__':
    loopMonitor()
