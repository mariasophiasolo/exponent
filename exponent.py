# write a function called exponent

def exponent(base, exp):
    # initialize first a variable
    number = exp
    result = 1

# then perform exponentiation with a while loop
    while number > 0:
        result *= base
        number -= 1  

    # return the final result
    return result

case1_base_value = 2
case1_exponent_value = 5

case2_base_value = 5
case2_exponent_value = 4

# call the exponent function with the provided base and exponent values
result1 = exponent(case1_base_value, case1_exponent_value)
result2 = exponent(case2_base_value, case2_exponent_value)

# display the result using f-string formatting
print(f"{case1_base_value} raised to the power of {case1_exponent_value} is: {result1}")
print(f"{case2_base_value} raised to the power of {case2_exponent_value} is: {result2}")
