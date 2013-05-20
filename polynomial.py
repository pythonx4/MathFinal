#Colm Gallagher and TJ Corely
#Poly.py

class Polynomial(object):
    
    def __init__(self, coefficents):
        self.coefficents = coefficents

    def evaluate_at_value(self,x):  
    #We have to define the total at zero and then add to it
        total = 0
        #Here we are using listnum to put the variables to a power
        listnum = 0
        #This finds the length of the list/polynomial
        length = len(self.coefficents)
        #Now here is the fun stuff, here we calculate the value at x
        while length > 0:
            #Here we are multiplying the coefficient (poly[listnum])
            #by the value of x to the power of the function (listnum)
            total += self.coefficents[listnum] * x**listnum
            #Here we subtract the length to tell the program to stop
            #when we've reached the end of the list
            length -= 1
            #Here we add to listnum to go through the list and raise
            #the power of the exponent
            listnum += 1
        #Finally, here we return a float (or a decimal answer) of the
        #total sum of the evaluation
        return float(total)
    
    def get_derivative(self):
        #First we are going to define some variables.
        Derivative = []
        index = 1
        #Here we are basically saying that the derivative of a constant is 0.0
        if len(self.coefficents) == 1:
            Derivative = [0.0]
        #Here is where we get the derivative, which is quite simple by using the
        #power rule.
        for coefficent in self.coefficents[1:]:
            #we include everything but first term, since it will be constant and at 0
            #Here, we are adding the the list Derivative the coefficients
            #multiplied by the exponent which is the basic power rule.
            #We start at Number=1 because when the 0th term of the list
            #is always a constant which's derivative is 0.
            Derivative.append(coefficent * index)
            index += 1
        #This now returns the derivative in a format consistent with that
        #of our original polynomial
        return Polynomial(Derivative)
    
    def get_integral(self):
        integral = []
        integral.append('C')
        index = 0
        #add the C to the end of the integral
        for coefficent in self.coefficents:
            if index == 0:
                integral.append(coefficent)
            else:
                integral.append(float(coefficent) / (index + 1) )
            index += 1
        return Polynomial(integral)
        
    def __str__(self):
        string = ''
        #start with blank string so we can add on to it.
        index = len(self.coefficents) - 1
        for item in self.coefficents[::-1]:
            #This makes it start in backwards order so we can print out
            #the coefficients from lowest degree to highest
            #this is where the coefficients is in the list
            if index == 0:
                string += str(item)
            #if the index = 0 that means that there will be no power to it
            #we also will not be putting a '+' after it.
            elif index == 1:
                string += str(item) + 'x + '
            #if index = 1 there will be no power to it, but we will add '+'
            else:
                string += str(item)+'x^'+str(index)+ ' + '
            index -= 1
            #if the index is not 1 or 0 we can and add power sign and '+'
        return string
            #now if we do 'print poly', a nice formatted string will display
#ex        
poly = Polynomial([3,4,5,6])
#print poly
#print poly.get_derivative()
#print poly.get_integral()
