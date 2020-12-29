import random
import PIL
from PIL import Image
from PIL import ImageDraw
global size
i_size = input("Map size: ")
if i_size == 'd':
    size = 100
else:
    size = int(i_size)
#Expand number min/max
global e_n_mim
global e_n_min
i_e_min = input("Expand min: ")
if i_e_min == "d":
    e_n_min = 5
else:
    e_n_min = int(i_e_min)
i_e_max = input("Expand max: ")
if i_e_max == "d":
    e_n_max = 20
else:
    e_n_max = int(i_e_max)
global pixel
i_pixel = input("Grid size: ")
if i_pixel == "d":
    pixel = 10
else:
    pixel = int(i_pixel)
global num_v
i_v = input("Number of Volcanos: ")
if i_v == "d":
    num_v = 4
else:
    num_v = int(i_v)
i_name = input("File name: ")
global f_name
if i_name == 'd':
    f_name = "Cano.png"
else:
    f_name = i_name + '.png'
global blue
blue = (0,0,255)
def make_map():
    global y
    global x
    y = []
    x = []
    y_cnt = 0
    x_cnt = 0
    while y_cnt < size:
        while x_cnt < size:
            v = 0
            x += [v]
            x_cnt += 1
        #print(y_cnt," percent")
        y += [x]
        x = []
        x_cnt = 0
        y_cnt += 1
def cano():
    expand_num = random.randint(e_n_min,e_n_max)
    p = random.randint(expand_num+1,size-expand_num-1)
    y[p][p] = expand_num
    expand = True
    n = 1
    e = expand_num-1
    #print("Volcano Fired!")
    global m
    m = []
    while expand:
        # idea for chance of value
        # 1 has 1/2 chance [0,1]
        # 2 has 1/3 chance [0,1,2]
        # 3 has 1/4 chance [0,1,2,3]
        # 4 has 1/5 chance [0,1,2,3,4]
        # 5 has 1/6 chance [0,1,2,3,4,5]
        # 6 has 1/5 chance [2,3,4,5,6]
        # 7 has 1/4 chance [4,5,6,7]
        # 8 has 1/3 chance [6,7,8]
        # 9 has 1/2 chance [8,9]
        if e > 1:
            h = round(int(e/2),0)
            #print(h)
            e = random.randint(h,e)
        k = random.randint(0,e)
        y[p+n][p]   = y[p+n][p]+e
        y[p-n][p]   = y[p-n][p]+e
        y[p][p+n]   = y[p][p+n]+e
        y[p][p-n]   = y[p][p-n]+e
        y[p+n][p+n] = y[p+n][p+n]+e
        y[p-n][p-n] = y[p-n][p-n]+e
        y[p+n][p-n] = y[p+n][p-n]+e
        y[p-n][p+n] = y[p-n][p+n]+e
        #    Pl Ps Ng
        global c
        c = [p,p+n,p-n]
        t = 0
        raize(p,e,n,h,c,t)
        r = n-1
        m += [y[p+n][p],y[p-n][p],y[p][p+n],y[p][p-n],y[p+n][p+n],y[p-n][p-n],y[p+n][p-n],y[p-n][p+n]]
        while r > 0:
            c = [p+r,p+n,p-n,p-r]
            y[p+r][p+n] = y[p+r][p+n]+e
            y[p+r][p-n] = y[p+r][p-n]+e
            y[p+n][p+r] = y[p+n][p+r]+e
            y[p-n][p+r] = y[p-n][p+r]+e
            y[p+n][p-r] = y[p+n][p-r]+e
            y[p-n][p-r] = y[p-n][p-r]+e
            y[p-r][p-n] = y[p-r][p-n]+e
            y[p-r][p+n] = y[p-r][p+n]+e
            t = 1
            c = [p+r,p+n,p-n,p-r]
            raize(p,e,n,h,c,t)
            m += [y[p+r][p+n],y[p+r][p-n],y[p+n][p+r],y[p-n][p+r],y[p+n][p-r],y[p-n][p-r],y[p-r][p-n],y[p-r][p+n]]
            r -= 1
        n += 1
        if e == 1:
            expand = False
            c = 0
            #Debug
            #while c < size:
            #    print(y[c])
            #    c += 1
        e -= 1
def make_img():
    img=Image.new("RGBA",(size*pixel,size*pixel),(100,100,100))
    draw = ImageDraw.Draw(img)
    i_x = 0
    i_y = 0
    e_x = 0
    e_y = 0
    while i_y < size:
        while i_x < size:
            u = y[i_y][i_x]
            if u != 0:
                l = max(m)
                clr_conv = 255-l
                cst = u+clr_conv
                clr = (0,cst,0)
            if u == 0:
                clr = blue
            draw.rectangle((e_x,e_y,e_x+pixel,e_y+pixel), fill=clr, width=pixel)
            i_x += 1
            e_x += pixel
        i_x = 0
        e_x = 0
        i_y += 1
        e_y += pixel
    draw = ImageDraw.Draw(img)
    img.save(f_name) 
    print(l)
    print("Image Done")
def array_view():
    c = 0
    while c < size:
        print(y[c])
        c += 1
def raize(p,e,n,h,c,t):
    if t == 0:
        #Center
        #y[c[0]][c[0]] = y[c[0]][c[0]]+e
        #raise
        rz = True
        k = 0
        o = 1
        while k < 3:
            while o < 3:
                y[c[k]][c[o]] = y[c[k]][c[o]]+e
                o += 1
            o = 1
            k += 1
        k = 0
        o = 1
        while k < 3:
            while o < 3:
                #center
                cen = y[c[k]][c[o]]
                #else
                y[c[k]-1][c[o]]     = y[c[k]-1][c[o]]+h
                y[c[k]+1][c[o]]     = y[c[k]+1][c[o]]+h
                y[c[k]][c[o]-1]     = y[c[k]][c[o]-1]+h
                y[c[k]][c[o]+1]     = y[c[k]][c[o]+1]+h
                y[c[k]-1][c[o]-1]   = y[c[k]-1][c[o]-1]+h
                y[c[k]+1][c[o]+1]   = y[c[k]-1][c[o]-1]+h
                y[c[k]-1][c[o]+1]   = y[c[k]-1][c[o]-1]+h
                y[c[k]+1][c[o]-1]   = y[c[k]-1][c[o]-1]+h
    if t == 1:
        k = 0
        o = 1
        while k < 5:
            while o < 5:
                y[c[k]][c[o]] = y[c[k]][c[o]]+e
print("Start")
make_map()
while num_v > 0:
    print("Firing Volcano")
    cano()
    num_v -= 1
#array_view()
make_img()