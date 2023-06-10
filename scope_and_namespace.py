#global_var is in the global namespace
global_var = 10

def outer_function():
    #outer var in local namespace 
    outer_var = 20 
    def inner_function():
        #inner_var is a nested local namespace 
        inner_var = 30 
        print(inner_var)
    print(outer_var)    
    inner_function()
#print the value of the global variable 
print(global_var)          
# calling the outer function and print local and nested local variables 
outer_function()
