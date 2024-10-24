def example_function():
    a = 1
    b = 2
    c = 3
    
    
    local_variables = locals()
    return len(local_variables)

# Call the function and print the number of local variables
num_locals = example_function()
print('local variavles:\n', (num_locals))
