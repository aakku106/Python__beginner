# In python if, else and elif can manipulate the flow of our code <According to the given conditions>

#In the example below we compare the value of x to determine if it is positive or not
x = int(input("Please enter an number: ")) 
if x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
elif x>0:
    print('positive')

# In this example y takes a string from user <1st three letters of a week> and compared the conditions..
# (Like a switch case statement in c or C++)
y = input("Please enter an week: ")
if y== 'sun':
    print('Sunday')
elif y== 'mon':
        print('Monday')
elif y== 'tue':
        print('Tuesday')
elif y== 'wed':
        print('Wednesday')
elif y== 'thu':
        print('Thursday')
elif y== 'fri':
        print('Friday')
elif y== 'sat':
        print('Saturday')
else:
        print('Invalid input')




# This code example cakes if the time given by user is AM or PM  😁 
z = int(input("Enter the time "))
if z<24  and z < 12:  
       print("Morning CCN");
elif z > 11 and z < 24:
       print('Evening, CCN');
else :
       print('you seems to be a ghost 💀☠️')
       