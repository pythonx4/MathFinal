import math

def f(x):
    if type(x) == str:
        return 'math.e**x'
    else:
        return math.e**x
def g(x,y):
    return math.e**x-math.e**y
def derivative(function):
    def dfunction(x,h=0.1e-5):
        return (function(x+h/2)-function(x-h/2))/h
    return dfunction

def taylor(function, nth, center):
    poly = [str(round(function(center),3))]
    i = 1
    d = function
    while i < nth+1:
        d = derivative3(d)
        poly.append(' + '+str(round(d(center),3))+'*(x-'+str(center)+')^'+str(i)+'/'+str(i)+'!')
        i+=1
    string = ''
    for value in poly:
        stringval = str(value)
        if stringval.find('0.0*') == -1:
            stringval = stringval.replace('--','+')
            string += stringval
    return string

def derivative2(function):
    dtrig = {math.sin(u):math.cos(u)*derivative2(u),math.cos(u):-math.sin(u)*derivative2(u),math.tan(u):1/(math.cos(u))**2*derivative2(u)}
    lfunc = function.split('+')
    for func in lfunc:
        lfunc[lfunc.index(func)] = func.replace(' ','')
    for func in lfunc:
        lfunc[lfunc.index(func)] = func.replace('**','^')
    print lfunc
    deriv = []
def split(function):
    '''Imports a string and splits it up into a list that can be used to solve the derivative of a function'''
    if type(function) != str:
        return 'Input a string of the function!'
    else:
        function = function.replace('**','^')
        function = function.replace(' ','')
        function = function.replace(')(',')*(')
        oldfunction = function
        paren = [[],[]]
        for i in range(len(function)):
            if function[i] == '(':
                paren[0].append(i)
            if function[i] == ')':
                paren[1].append(i)
        print paren
        final = []
        a=0
        b=0
        while a < len(paren[0]):
            while paren[0][a+1] > paren[1][b]
            
                
             
                
        
        
        
def derivative3(function):
    def dfunction(x,epsilon=0.1):
        slope1 = 1
        slope2 = 2
        h = 0.1
        while abs(slope2-slope1) > epsilon:
            h /= 3
            slope1=slope2
            slope2 = (function(x+h)-function(x-h))/(2*h)
            #print slope2
        return slope2
    return dfunction

def newton(function, x_0, epsilon):
    numIt = 0
    x_1 = x_0
    print (0,x_0)
    
    while numIt == 0 or abs(x_0-x_1)>epsilon:
        x_0 = x_1
        x_1 = x_0 - function(x_0)/derivative3(function)(x_0)
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


