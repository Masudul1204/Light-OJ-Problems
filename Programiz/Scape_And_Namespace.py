# global_var = 10

# def outer_function():
#     outer_var = 20

#     def inner_function():
#         inner_var = 30

#         print(inner_var)
    
#     print(outer_var)

#     inner_function()

# print(global_var)

# outer_function()

# Use of global keyword

global_var = 10

def my_function():
    local_var = 20

    global global_var
    global_var = 30

print(global_var)

my_function()
print(global_var)