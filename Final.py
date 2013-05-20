import math

def derivative(function):
    def dfunction(x,epsilon=0.01):
        slope1 = 1
        slope2 = 2
        h = 0.1
        while abs(slope2-slope1) > epsilon:
            h /= 3
            slope1=slope2
            slope2 = (function(x+h)-function(x-h))/(2*h)
        return slope2
    return dfunction

def newton(function, x_0, epsilon):
    numIt = 0
    x_1 = x_0
    print (0,x_0)
    
    while numIt == 0 or abs(x_0-x_1)>epsilon:
        x_0 = x_1
        x_1 = x_0 - function(x_0)/derivative(function)(x_0)
        numIt += 1
        print (numIt, round(x_1,4))
    return round(x_1,4)

def euler(function, x_0,y_0, h, num):
    numIt = 0
    while numIt < num:
        print (round(x_0,3),round(y_0,4))
        x_1 = x_0 + h
        y_1 = y_0 + h*function(x_0,y_0)
        x_0 = x_1
        y_0 = y_1
        numIt +=1
    return (round(x_1,3),round(y_1,4))

def taylor(function, nth, center):
    poly = [str(round(function(center),3))]
    i = 1
    d = function
    while i < nth+1:
        d = derivative(d)
        poly.append(' + '+str(round(d(center),3))+'*(x-'+str(center)+')^'+str(i)+'/'+str(i)+'!')
        i+=1
    string = ''
    for value in poly:
        stringval = str(value)
        if stringval.find('0.0*') == -1:
            stringval = stringval.replace('--','+')
            string += stringval
    return string

def riemann(function, n, bounds, LorR='l'):
    '''function is the function you are lookin
g at
n is the number of rectangles to split up
bounds is represented by a list with hard brackets such as [0,2]
LorR is a string which provides wheter it starts at the left or right endpoint'''
    i = float(bounds[1]-bounds[0])/n
    a = bounds[0]
    b = bounds[1]
    area = 0
    if LorR.lower() == 'l':
        while a < b:
            area += function(a)*i
            a += i
        return area
    elif LorR.lower() == 'r':
        a+=i
        while a <= b:
            area += function(a)*i
            a += i
        return area
