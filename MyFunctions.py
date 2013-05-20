#Colm Gallagher and TJ Corely
#Functions.py

#So here, a polinomial is going to be in the format of a list,
#where each new element is to the power of whatever number in
#the list it is. For example, [1,4,3] would represent y=3x^2+4x+1.
#It is essentially a list of coefficients
polynomial = [1,4,3]

#Now we have to make a basic function that evaluates the function
#at a specific value of x
def evalPoly(poly,x):
    #We have to define the total at zero and then add to it
    total = 0
    #Here we are using listnum to put the variables to a power
    listnum = 0
    #This finds the length of the list/polynomial
    length = len(poly)
    #Now here is the fun stuff, here we calculate the value at x
    while length > 0:
        #Here we are multiplying the coefficient (poly[listnum])
        #by the value of x to the power of the function (listnum)
        total += poly[listnum] * x**listnum
        #Here we subtract the length to tell the program to stop
        #when we've reached the end of the list
        length -= 1
        #Here we add to listnum to go through the list and raise
        #the power of the exponent
        listnum += 1
    #Finally, here we return a float (or a decimal answer) of the
    #total sum of the evaluation
    return float(total)

#Now, we can do hard stuff like differentiation!

#So, let's define a function called derivPoly and give it a paramater
#for the polynomial.
def derivPoly(poly):
    #First we are going to define some variables.
    Length = len(poly)
    Derivative = []
    Number = 1
    #Here we are basically saying that the derivative of a constant is 0.0
    if Length == 1:
        Derivative = [0.0]
    #Here is where we get the derivative, which is quite simple by using the
    #power rule.
    while Number < Length:
        #Here, we are adding the the list Derivative the coefficients
        #multiplied by the exponent which is the basic power rule.
        #We start at Number=1 because when the 0th term of the list
        #is always a constant which's derivative is 0.
        Derivative.append(poly[Number]*Number)
        Number += 1
    #This now returns the derivative in a format consistent with that
    #of our original polynomial
    return Derivative

#To make it easier to see, I am going to write a small function here that
#prints out the polynomial in a nicer format, but it is not needed
def printPoly(poly):
    string = ''
    length = len(poly)
    num = 0
    for item in poly:
        if float(num) == 0.0:
            string = str(item)
        else:
            string = str(item)+'x^'+str(num)+' + ' + string
        num += 1
    print string
        

