global_var = 10

def my_function():
    #define local var
    local_var = 20 
     
    #modify global var value 
    global global_var 
    global_var = 30 
#print globla var
print(global_var)  
 #calling function to modify the global variable 
my_function()

print(global_var)


