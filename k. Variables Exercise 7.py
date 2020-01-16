# Exercise:
# Insert the correct keyword to make the variable x belong to the global scope.
# def myfunc():
#    ___ x
#    x = "fantastic"

# Solution:
def myfunc():
    global x
    x = "fantastic"
