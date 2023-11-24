import numpy as np
import matplotlib.pyplot as plt
import os
import math
# from tqdm import tqdm
import imageio #生成gif动图

#x=x^2+c
x0=0
num=2048 #对应分辨率
multiple=0.5
x_extent_list=[(-2,1)]
y_extent_list=[(-1.5,1.5)]
images_num=15 #生成图片数量
for i in range(images_num-1):
    x_extent_list.append((-0.25-math.pow(multiple,i+1),-0.25+math.pow(multiple,i+1)))
    y_extent_list.append((0.64-math.pow(multiple,i+1),0.64+math.pow(multiple,i+1)))

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
    dir_path='./graph/mendelbrot图形'
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    files=os.listdir(dir_path)
    num_file=len(files)
    k=0
    for x_extent,y_extent in (zip(x_extent_list,y_extent_list)):
        c_x=np.linspace(x_extent[0],x_extent[1],num)
        c_y=np.linspace(y_extent[0],y_extent[1],num)

        for i in range(num):
            for j in range(num):
                diverge_speed[i][j]=getDivergeSpeed(complex(c_x[j],c_y[num-1-i]),M,N)
    
        plt.figure(figsize=(10,10))
        plt.imshow(diverge_speed,'hot',extent=(min(c_x),max(c_x),min(c_y),max(c_y)))
        # plt.colorbar()
        plt.axis('off')
        plt.subplots_adjust(0,0,1,1) 


        k+=1
        plt.savefig(fname=dir_path+f'/mendelbrot一组{num_file} {num} x {num} {k} .png',format='png',dpi=num/10,bbox_inches='tight', pad_inches = 0)
        # plt.show()
        print(f'{k}/15 ok')
    
    gif_images=[]
    for i in range(1,images_num+1,1):
        gif_images.append(imageio.v2.imread(dir_path+f'/mendelbrot一组{num_file} {num} x {num} {i} .png'))
    imageio.v2.mimsave(dir_path+f'/{num}x{num}.gif',gif_images,duration=500)