# in python naming variable type us not requires
#eg:
x :int= 2; 
print(x);
y=2
print(y)
# both are valid 
#or we can also
x,y = 1,2
print(x,y)
# we can also do
x=y=z=4
print(x,y,z)
# we can notice that the variables value are overritten when assigned in lower lines

# we can also do unpacking(tho out of topic, but interesting )
cat=['orange','white','black','mix']
o,w,b,m= cat
print(o,w,b,m) # this is simpally called unpacking tho cat can be printed independently
print(cat) # in output of this we can observe, that its in ['',''] form this is called list in python