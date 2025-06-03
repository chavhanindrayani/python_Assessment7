# 3.	Create a function that accepts an array of floats and returns the sum of all elements in the array.

def array_in_sumall_no(number):
    float = 0.0
    for i in number:
        float = float + i
    return float
        
print(array_in_sumall_no([30.9, 88.8, 77.0, 89.0, 23.0]))

