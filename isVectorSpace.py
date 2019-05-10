from sympy import *


'''
u+v is closed
u+v = v+u
u+(v+w) = (u+v)+w
u+0 = 0+u = u
u+(-)u = 0

c.u is closed
c.(u+v)= c.u + c.v
(c _+_ d).u = c.u + c.d
c.d.u = (cd).u
1.u = u
_+_ is ordinary addition
'''

def plus(p1, p2):
    return p1[0]+p2[0], p1[1]+p2[1]

def plus(u,v):
    return Matrix([ u[0]/v[0],u[1]/v[1] ])


x1,x2,y1,y2,x3,y3,c,x,y = symbols('x1,x2,y1,y2,x3,y3,c,x,y')
c = Symbol('c', positive=True)
x2 = x1 + c
y2 = y1 +c
X = [x1,x2,x3]
Y = [y1,y2,y3]

u = Matrix([x1, y1])
v = Matrix([x2,y2])
w = Matrix([x3,y3])

##print('Property Alpha')
##print('Commutative:', plus(u,v) == plus(v,u) )
##print('Assocoative:', plus(u ,plus(v,w)) == plus(plus(u,v),w))


class VectorSpace():
    def __init__(self):
        self.c_plus = '+'
        self.c_dor = '.'
        self.Xconstraint = []
        self.Yconstraint = []
        self.assume = [self.Xconstraint,self.Yconstraint]
        self.global_constraint = []

    def constraints(self, assume):
        self.global_constraint = assume
        for Xconstraint in assume[0]:
           for sym in X:
               self.Xconstraint.append(Xconstraint(sym))
        for Yconstraint in assume[1]:
           for sym in Y:
               self.Yconstraint.append(Yconstraint(sym))

    def is_closed(self, u,v,operator):
        if len(self.global_constraint) != 0:
            w = operator(u,v)
            C = []
            with assuming(*self.Xconstraint):
                for constraint in self.global_constraint[0]:
                    closed_x = ask( constraint(w[0]) )
                    C.append(closed_x)
                
            with assuming(*self.Yconstraint):
                for constraint in self.global_constraint[1]:
                    closed_y = ask( constraint(w[1]) )
                    C.append(closed_y)
            #print(C)
            return closed_x and closed_y
        return True

    def commutative(self,u,v, operator):
        return operator(u,v) == operator(v,u)

    def associative(self, u,v,w, operator):
        return plus(u ,plus(v,w)) == plus(plus(u,v),w)

z = VectorSpace()
#z.constraints([ [Q.positive], [Q.positive]])

print(z.is_closed(u,v,plus))
print(z.commutative(u,v,plus))
print(z.associative(u,v,w,plus))
