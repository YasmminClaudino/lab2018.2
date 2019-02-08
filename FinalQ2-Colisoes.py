def colisoes(x,y,x0,y0,x1, y1, x2, y2):
    if (x1 > x0) or (x2 < x):
        return(0)
    else:
        if (y1 > y0) or (y2 < y):
           return(0)
        else:
            return(1)
#elementos retangulo 1
x, y, x0,y0 = [int(x) for x in input().split()]
#elementos do retangulo 2
x1, y1, x2, y2 = [int(x1) for x1 in input().split()]
#para não haver colisão x1 > x0 ou x2 < x
print(colisoes(x,y,x0,y0,x1, y1, x2, y2))
