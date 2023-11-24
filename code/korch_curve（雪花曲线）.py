'''
通过迭代画线
点+方向+长度 可确定一次落笔
第k次迭代可以由第k-1次迭代组合而成(4个) 
先画k-1次迭代的图案,此时将笔的方向逆时针旋转60°,
再画k-1次迭代的图案,再将笔的方向顺时针旋转120°,
再画k-1次迭代的图案,再将笔的方向逆时针旋转60°,
最后再画k-1次迭代的图案
'''

from turtle import *

angle_list=(('left',60),('right',120),('left',60))

def destination_string_to_function(dst:str):
    if dst=='left':
        return left
    else:
        return right

def k_move(k:int,length:float):
    if k==0:
        forward(length)
    else:
        length1=length/3
        k_move(k-1,length1)
        for dst,angle in angle_list:
            destination_string_to_function(dst)(angle)
            k_move(k-1,length1)

if __name__=='__main__':
    setup(width=1000,height=800)
    setworldcoordinates(0,-400,1000,600)
    speed(0)
    k_move(6,1000)
    mainloop()
