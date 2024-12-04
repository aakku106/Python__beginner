x = 'ccn'#global
def function():
    print(x)#calling global var
print(x)

def function2():
    x = 4# overiting global var with local var
    print(x)

def function3():
    global a;# Declearing global var inside functions/methods 
    a = 'rat'
    print(a)

function();function2();function3()
print(a)#calling global var outside functions
a=3#reassinging valure for global var inside function3()
print(a)