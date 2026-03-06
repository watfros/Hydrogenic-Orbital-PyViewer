import numpy as np  # Library for working with arrays
from math import factorial
pi=np.pi
a = 5.291772108e-11

#Calculate Legendre polynomial
def legendre_polynomial(l,m,x):
    pmm = 1.0
    if m > 0:
        sign = 1.0 if m % 2 == 0 else -1.0
        pmm = sign*pow(factorial(2*m-1)*(1.0-x*x),((m/2)))

    if l == m:
        return pmm

    pmm1 = x*(2*m+1)*pmm
    if l == m+1:
        return pmm1

    for n in range(m+2,l+1):
        pmn = (x*(2*n-1)*pmm1-(n+m-1)*pmm)/(n-m)
        pmm = pmm1
        pmm1 = pmn

    return pmm1

#Convert r,Theta,Phi to x,y,z
def sph2cart(r,Theta,Phi):

    x = r*np.sin(Theta)*np.cos(Phi)
    y = r*np.sin(Theta)*np.sin(Phi)
    z = r*np.cos(Theta)
    
    return x, y, z

#Convert x,y,z to r,Theta,Phi
def cart2sph(x,y,z):
    phi = np.arctan2(y,x)
    theta = np.arctan2(np.sqrt(x**2 + y**2),z)
    r = np.sqrt(x**2 + y**2 + z**2)
    return r, theta, phi
    
#Calculate associated Laguerre polynomial
def associatedLaguerre(l, n, x):
    coeffs = []
    for k1 in range(n-l-1+1):
        c = (-1)**k1*factorial(n+l)**2/factorial(n-l-k1-1)/factorial(2*l+1+k1)/factorial(k1)
        coeffs.append(c)
        
    out = [0.0 for z in range(len(x))] # output
    for m in range(len(coeffs)):
        #print m, " ", coeffs[m], "jgfk"
        out = out + coeffs[m]*(x**m)
    return out

#Calculate wave function value
def calc_psi(r,Theta,Phi,n, l, m):

    A = np.sqrt(((2*l+1)*factorial(l-abs(m)))/(4*pi*factorial(l+abs(m))))

    rho = 2.0*r/n/a
    
    if m>0:
            
        scalars = np.sqrt(2)*np.cos(m*Phi)*legendre_polynomial(l,m,np.cos(Theta))*np.exp(-rho/2)*rho**l*associatedLaguerre(l, n, rho)
            
    elif m < 0:
            
        scalars = np.sqrt(2)*np.sin(abs(m)*Phi)*legendre_polynomial(l,abs(m),np.cos(Theta))*np.exp(-rho/2)*rho**l*associatedLaguerre(l, n, rho)
            
    else:
            
        scalars = legendre_polynomial(l,0,np.cos(Theta))*np.exp(-rho/2)*rho**l*associatedLaguerre(l, n, rho)
    
    #Normalization constant for angular part
    A = np.sqrt(((2*l+1)*factorial(l-abs(m)))/(4*pi*factorial(l+abs(m))))
    #Normalization constant for radial part
    B = np.sqrt((2.0/n)**3*factorial(n-l-1)/(2*n*factorial(n+l)**3))
    #Wave function normalization
    scalars = scalars * A * B

    return scalars

#Calculate wave function value and check if it is zero
def calc_psi_prof(r,Theta,Phi,n, l, m):

    
    rho = 2.0*r/n/a
    
    if m>0:
            
        scalars = np.sqrt(2)*np.cos(m*Phi)*legendre_polynomial(l,m,np.cos(Theta))*np.exp(-rho/2)*rho**l*associatedLaguerre(l, n, rho)
            
    elif m < 0:
            
        scalars = np.sqrt(2)*np.sin(abs(m)*Phi)*legendre_polynomial(l,abs(m),np.cos(Theta))*np.exp(-rho/2)*rho**l*associatedLaguerre(l, n, rho)
            
    else:
            
        scalars = legendre_polynomial(l,0,np.cos(Theta))*np.exp(-rho/2)*rho**l*associatedLaguerre(l, n, rho)
    
    #Normalization constant for angular part
    A = np.sqrt(((2*l+1)*factorial(l-abs(m)))/(4*pi*factorial(l+abs(m))))
    #Normalization constant for radial part
    B = np.sqrt((2.0/n)**3*factorial(n-l-1)/(2*n*factorial(n+l)**3))
    #Wave function normalization
    scalars = scalars * A * B

    #Whether the wave function is zero in a certain plane. It cannot be shielded by angle because 0^0 may occur
    if np.max(abs(scalars)) < 0.01: scalars = scalars * 0

    return scalars

#Calculate spherical harmonic function
def calc_Y(Theta,Phi,l, m):


    #print('cos(m*Phi)')
    #print(np.cos(m*Phi))
    #print('cos(Theta)')
    #print(np.cos(Theta))
    #print('sin(abs(m)*Phi)')
    #print(np.sin(abs(m)*Phi))
    if m>0:
        #print("m>0")
        scalars = np.sqrt(2)*np.cos(m*Phi)*legendre_polynomial(l,m,np.cos(Theta))

    elif m < 0:
        #print("m<0")
        scalars = np.sqrt(2)*np.sin(abs(m)*Phi)*legendre_polynomial(l,abs(m),np.cos(Theta))

    else:
        #print("m=0")
        scalars = legendre_polynomial(l,0,np.cos(Theta))

    #Normalization constant for angular part
    A = np.sqrt(((2*l+1)*factorial(l-abs(m)))/(4*pi*factorial(l+abs(m))))
    #Wave function normalization
    scalars = scalars * A 
    #Whether the wave function is zero. It cannot be shielded by angle because 0^0 may occur
    if np.max(abs(scalars)) < 0.01: scalars = scalars * 0

    return scalars