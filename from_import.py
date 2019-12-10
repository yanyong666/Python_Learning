# 案例1
from math import sqrt
print("square root of 16 is", sqrt(16))

# 案例2
"""
Ping发送一个ICMP(Internet Control Messages Protocol,因特网信报控制协议)；
回声请求消息给目的地并报告是否收到所希望的ICMPecho （ICMP回声应答）
例如：
    ping ip -n -r -w  (-n表示测试发送N个数据包 -r表示经过多少个路由 -w表示响应时间)  还可以有一堆参数
"""
import os
#import sys   这种方法导入sys模块，需使用sys.argv
from sys import argv  #这种方法导入sys模块，可直接使用argv
def ping(net,start=1,end=85,n=1,r=3,w=3):
    for i in range(start,end+1):
        ip=net+"."+str(i)
        command="ping %s -n %d -r %d -w %d"%(ip,n,r,w)
        print(ip,("通","不通")[os.system(command)])  #os.system(command)：运行command命令
if len(argv) not in [2,4,6]:
    print("参数输入错误！")
    print("运行示例：")
    print("from_import.py 121.194.14")
    print("from_import.py 121.194.14 80 90")
    print("from_import.py 121.194.14 80 90 3 1")
    print("语法：from_import.py net startip endip count routs timeout")
elif len(argv)==2:
    net=argv[1]
    ping(net)
elif len(argv)==4:
    net=argv[1]
    ping(net,start=int(argv[2]),end=int(argv[3]))
else:
    net=argv[1]
    ping(net,start=int(argv[2]),end=int(argv[3]),n=int(argv[4]),w=int(argv[5]))




