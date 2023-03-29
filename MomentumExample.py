import numpy as np

def MomentumTransfer():
    sam=np.array([2.5, 0, 0])
    hed=np.array([0, 0, 0])
    for j in range(3):
        m1=1 #Mass of Fist ball in Kg
        m2=1 #Mass of Second ball in Kg
        u1= sam[j]#Initial Velocity of first ball in m/s
        u2=hed[j]#Initial Velocity of second ball in m/s
        mu1=m1/2 #Half mass used in Kinetic energy EQN
        mu2=m2/2 #Half mass used in Kinetic energy EQN
        mr=m2/m1 #Ratio of the two masses
        a=(mu2+mu1*mr**2)
        b=(-2*mr*mu1*u1-2*u2*(mr**2)*mu1*u2*mr**2)
        c=2*mr*u1*mu1*u2+mu1*(mr**2)*(u2**2)-mu2*u2
        hed[j]=(-b+np.sqrt((b**2)-4*a*c))/2*a #Quadratic forumla
        sam[j]=u1+mr*(u2-hed[j])
    return ("particle 1 ={}".format(sam),"particle 2 ={}".format(hed))
print(MomentumTransfer())

