# Run the program to see the results!
import matplotlib.pyplot as plt
import numpy as np
from math import *

def euler(r,theta): # Euler's formula: z = e^i(theta). Used for the scatter plot visual; wraps the naturals around a spiral
    j = (-1)**.5
    pt = r*(e**(theta*j))
    global a
    a = np.real(pt)
    global b
    b = np.imag(pt)
    
def isPrime(num): # Algorithm that checks if a number is prime; returns a boolean
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True      

def listPrimes(n,m): # Checks for primes up to n, appends them into a list and provides data. Iterates up to m for the scatterplot.
    count = 0
    primes = []
    colour = ['black', 'black']

    for i in range(2,n):
        if isPrime(i):
            count += 1
            primes.append(i)
            colour.append('yellow')
        else:
            colour.append('black')
            
    print()
    print('There are', count,'primes up to a million!')
    print()
    print('The biggest prime:',primes[count-1])
    print()
    sump = sum(primes)
    print('The sum of all the primes:', sump)
     
    sizes = [1]*m
    x = []
    y = []
    r = 1
    theta = pi
    for i in range(0,m):
        euler(r,theta)
        r += .01
        theta += .01
        x.append(a)
        y.append(b)

    ax = plt.axes()
    ax.set_facecolor('black')
    plt.scatter(x, y, sizes, c=colour[0:m])
    plt.title('Distribution of Primes')
    plt.show()
  
listPrimes(1*10**6,1*10**4) # We call the function here so the user can simply run the program for the results.




