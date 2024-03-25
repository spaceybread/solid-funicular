class Body:
    def __init__(self, x, y, ax, ay, m):
        self.cor = [x, y]
        self.acc = [ax, ay]
        self.mass = m
        self.oldx = [x]
        self.oldy = [y]
    
    def update(self, x, y):
        self.oldx.append(x)
        self.oldy.append(y)
        
    def getXpos():
        return self.oldx
        
    def getYpos():
        return self.oldy
    
    
def r(b1, b2):
    a = b1.cor
    b = b2.cor
    summa = 0
    for i in range(len(a)):
        v = a[i] - b[i]
        summa += v**2
    
    return summa**0.5

def a(b1, other):
    G = 1
    mass = b1.mass
    
    deldelx = 0
    deldely = 0
    
    print("start body: ", b1.cor)
    for b in other:
        if b1 != b:
            rad = r(b1, b)
            
            print("body: ", b.cor ,"rad: ", rad)
            vx = (b1.cor[0] - b.cor[0])/(rad**3)
            vx *= b.mass
            vx *= -1
            
            vy = (b1.cor[1] - b.cor[1])/(rad**3)
            vy *= b.mass
            vy *= -1
            
            print(vx, vy)
        
            deldelx += vx * G
            deldely += vy * G
    
    #print(deldelx, deldely)
    
    return 0
    
p1 = Body(-0.97000436, 0.24208753, 0.4662036850, 0.4323657300, 1)
p2 = Body(0, 0, -0.933240737, -0.86473146, 1)
p3 = Body(0.97000436, -0.24208753, 0.4662036850, 0.4323657300, 1)


bodies = [p1, p2]

#print(r(p1, p2))

print(a(p1, bodies))
