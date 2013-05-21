import math

def cost(length, base, height):
    return 1.4*base*height + 3.8*base*length
def volume(length,base,height):
    return .5*base*height*length
def get_specs():
    the_cost = 9001
    specification = []
    base = 0.0001
    while base < 4.4:
        height = (math.sqrt(3)/2)*base
        length = (8.8/math.sqrt(3))/(base**2)
        temp_cost = cost(length,base,height)
        if temp_cost < the_cost:
            the_cost = temp_cost
            specification = [round(length,2),round(base,2),round(height,2)]
        base+=.0001
    return specification

specs = get_specs()
print specs
print round(cost(specs[0],specs[1],specs[2]),2)
print round(volume(specs[0],specs[1],specs[2]),2)

    
    
