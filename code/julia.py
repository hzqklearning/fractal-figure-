import numpy as np
import matplotlib.pyplot as plt
import os #方便在文件夹中增加新文件
from tqdm import tqdm #方便查看程序运行进度
from threading import Thread #多线程 加快速度

#一些参数  a=a^2+c
c_list=[]
M=10 #上界，|a|的值超过M时认为发散
N=200 #最大迭代次数，对应收敛点
low_x=-1.5 #a的实部下界
up_x=1.5
low_y=-1.5 #a的虚部下界
up_y=1.5
num=50000  #对应图片分辨率 num x num
x=np.linspace(low_x,up_x,num)
y=np.linspace(low_y,up_y,num)

#对于给定的c，判断在x处的迭代发散情况，返回发散时对应的迭代次数
#× 小trick:当|x|>M时认为发散，由简单分析可知，当|x|>1时，肯定会发散(后面发现这个结论是错的，因为|x+c|可能又小于1了)
#迭代次数越大，意味着发散越慢，到达最大迭代次数对应收敛点
def iterateNum(x:complex,c:complex,M:int,N:int)->int:
    k=0
    while abs(x)<=M and k<=N:
        x=x*x+c
        k+=1
    return k

class DivergeSpeed(Thread):
    def __init__(self,c:complex,num_file:int):
        super().__init__()
        self.c=c
        self.num_file=num_file
        self.diverge_speed=np.zeros((num,num))

    def run(self):
        for i in range(num):
            for j in range(num):
                self.diverge_speed[i][j]=iterateNum(complex(x[num-1-j],y[i]),self.c,M,N) #好像有点问题 应该是(j,num-1-i) 不过问题不大，相当于图片中心对称
    
    def getDivergeSpeed(self):
        Thread.join(self)
        return self.diverge_speed


if __name__=='__main__':

    path='./graph/julia图形'
    if not os.path.isdir(path):
        os.makedirs(path)
    files=os.listdir(path)
    num_file=len(files)
    
    c_list=[0.28-0.01j]
    # c_list=[complex(0.45,0.1428),complex(0.38,0.25),complex(-0.74,-0.12),complex(-0.16,0.66),complex(0.31,0),complex(-0.75,0),complex(0.28,-0.01)]
    thread_list=[]
    for c in c_list:
        num_file+=1
        t=DivergeSpeed(c,num_file)
        t.start()
        thread_list.append(t)
    
    for thread in tqdm(thread_list):
        diverge_speed=(thread).getDivergeSpeed()
        plt.figure(figsize=(10,10),dpi=num/10) #创建一个新的窗口
        plt.imshow(diverge_speed,cmap='hot',extent=(low_x,up_x,low_y,up_y))
        plt.colorbar()  #显示颜色条
        plt.title(f'c={c}')
    
        num_file+=1
        plt.savefig(fname=f'./graph/julia图形/julia_curve{num_file}_{num}x{num}.png',format='png')
        # plt.show()
    
    

'''
原矩阵:ij表示(x[i],y[j])对应的发散速度(imshow显示默认也是按这个顺序的)
00 01 02 03 04...0n
10 11 12 13 14...1n
...
m0 m1 m2 m3 m4...mn

需要传入的矩阵：
0n 1n 2n ...mn
...
02 12 22 ...m2
01 11 21 ...m1
00 10 20 ...m0
(原矩阵逆时针旋转90°)

'''

'''
# 创建一个线程
t=Thread(target=func)

# 启动子线程
t.start()

# 阻塞子线程，待子线程结束后，再往下执行
t.join()

# 判断线程是否在执行状态，在执行返回True，否则返回False
t.is_alive()
t.isAlive()

# 设置线程是否随主线程退出而退出，默认为False
t.daemon = True
t.daemon = False

# 设置线程名
t.name = "My-Thread"
'''