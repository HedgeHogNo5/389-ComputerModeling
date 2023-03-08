import numpy as np
def MomentumTransfer():
    m1=1
    m2=1
    u1=2.5
    u2=0
    mu1=m1/2
    mu2=m2/2
    mr=m2/m1
    a=(mu2+mu1*mr**2)
    b=(-2*mr*mu1*u1-2*u2*(mr**2)*mu1*u2*mr**2)
    c=2*mr*u1*mu1*u2+mu1*(mr**2)*(u2**2)-mu2*u2
    x=(-b+np.sqrt((b**2)-4*a*c))/2*a
    y=(-b-np.sqrt((b**2)-4*a*c))/2*a
    o=u1+mr*(u2-x)
    p=u1+mr*(u2-y)
    return (x,o),(y,p)
print (MomentumTransfer())

