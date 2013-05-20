import polynomial as p
#This imports the functions we just made, we can access them by
#typing p.whatever

#Now we can get into Newton's method

#Newton's method is defined as: x_n+1 = x_n - f(x_n)/f'(x_n).
#This repeats until a certain eplsilon, or specification is met.

#Here I am going to show you how to program this using our functions
#we've already made.

#Here I am defining a function newton with the paramaters poly, x_0
#(which represents the initial point), and epsilon
def newton(poly, x_0, epsilon):
    #Number of iterations
    numIt = 0
    #This is used only because we define x_0 as the old x_1 in the
    #upcoming while statement and you therefore need a starting x_1
    #which I set to x_0 to keep its value
    x_1 = x_0
    #Used to print initial position before iterations
    print (0,x_0)
    deriv = poly.get_derivative()
    #This or statement says that if it is the first itteration, then
    #the program will run. Also, it says to keep going until the absolute
    #value of x_0-x_1 is less than epsilon
    while numIt == 0 or abs(x_0-x_1)>epsilon:
        #Used to set x_0 to x_1 before it is changed
        x_0 = x_1
        #Newton's method in our variables
        x_1 = x_0 - poly.evaluate_at_value(x_0)/poly.get_derivative().evaluate_at_value(x_0)
        numIt +=1
        print (numIt, x_1)
    return x_1
