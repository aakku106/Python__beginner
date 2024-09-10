#for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence
# lest see a simple example of for loop
# which print the values of list number 


number: list = [1,2,3,4,5]
for n in number:
    print(n);
# output
1
2
3
4
5
# if we dont want our output to change line, then
number: list = [1,2,3,4,5]
for n in number:
    print(n,end=' ');
# OUTPUT --->  1 2 3 4 5
#end="", puts the entered value after the value is printed, or simply it stops changing line

# MORE  Example
# num: int = 3;
# for num in num:
#     print(num); 
        #Will throws the error cause 3 or int is not iterable;

print('\n')
# let us try with a string
words: list = ['cat','rat',number]
for i in words:
    print(words);
#OUTPUT 
# ['cat','rat',[1,2,3,4,5]]
# ['cat','rat',[1,2,3,4,5]]
# ['cat','rat',[1,2,3,4,5]]


# Here list of words<can be anything>  ['cat','rat',number] has 3 members, so we got 3 outputs in different lines
# from above examples we can conclude that (number of for loop iterates) = length of list or sets or tuple or ...

for i in words:
    print(len(i),i)