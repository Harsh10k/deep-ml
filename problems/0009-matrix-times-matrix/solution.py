def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
        if len(a[0]) != len(b):
                return -1
        
        c = []
        s = 0
        for i in range(len(a)):
                c.append([])
                for j in range(len(b[0])):
                        for k in range(len(b)):
                                # a[i][k], b[k][j]
                                s += a[i][k] * b[k][j]
                        c[i].append(s)
                        s = 0
        return c

    
    