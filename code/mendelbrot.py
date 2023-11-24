import numpy as np
import matplotlib.pyplot as plt
import os

#x=x^2+c
x0=0
num=1000
c_x=np.linspace(-2,1,num)
c_y=np.linspace(-1.5,1.5,num)
M=10
N=100 #对应收敛点 收敛点和发散点的区分程度

def getDivergeSpeed(c:complex,M:int,N:int)->int:
    k=0
    x=x0
    while abs(x)<=M and k<=N:
        x=x*x+c
        k+=1
    return k

if __name__=='__main__':
    diverge_speed=np.zeros((num,num))
    for i in range(num):
        for j in range(num):
            diverge_speed[i][j]=getDivergeSpeed(complex(c_x[j],c_y[num-1-i]),M,N)
    
    plt.figure(figsize=(10,10))
    plt.imshow(diverge_speed,'hot',extent=(min(c_x),max(c_x),min(c_y),max(c_y)))
    plt.colorbar() #显示颜色条
    # plt.axis('off') #显示坐标轴
    # plt.subplots_adjust(0,0,1,1)

    dir_path='./graph/mendelbrot图形'
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    files=os.listdir(dir_path)
    num_file=len(files)
    plt.savefig(fname=dir_path+f'/mendelbrot{num_file+1} {num} x {num}.png',dpi=num/10,format='png')
    # plt.show()