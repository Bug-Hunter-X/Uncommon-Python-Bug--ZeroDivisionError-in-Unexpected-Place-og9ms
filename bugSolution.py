def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None  # Or raise a custom exception

result = my_function(10, 0) 

#Improved version with input validation:
def my_function_improved(a,b):
    if b == 0:
        print("Error: Division by zero. Please provide a non-zero denominator.")
        return None
    else:
        return a/b
result2 = my_function_improved(10,0)
result3 = my_function_improved(10,2)