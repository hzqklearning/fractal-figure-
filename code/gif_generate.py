import imageio

gif_images=[]
for i in range(1,11,1):
    gif_images.append(imageio.v2.imread(f'./graph/mendelbrot图形/mendelbrot一组17 1000 x 1000 {i} .png'))
imageio.v2.mimsave('./graph/mendelbrot图形/1000 x 1000.gif',gif_images,duration=500)
