sizeOfArray=int(input('How many numbers do we have in array ?\t'));
numbers=[];

print('Enter numbers in array\t');
for i in range(sizeOfArray):
    numbers.append(int(input()));
numberToCompare = int(input('Enter the number to compare\t'));
ifOutOfRange = True
low = 0;
high = sizeOfArray-1;
while low<=high:
    mid=(low+high)//2;
    if numbers[mid]== numberToCompare:
        ifOutOfRange = False;
        print('It was in index \t',mid);
        break;

    elif numberToCompare<numbers[mid]:
        high = mid-1;
    else :
        low = mid +1;

if ifOutOfRange==True:
    print("this number dosent exist in the array...\n");


