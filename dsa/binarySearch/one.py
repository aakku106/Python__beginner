numbers = [1,2,3,4,5];
low = 0;
high = 4;
ifExist=False
numberToSearch = int(input("Enter the number to search\t"));
while low <= high:
    mid = (low+high)//2
    if numberToSearch == numbers[mid]:
        ifExist=True;
        print("It was in index\t",mid);
        break;
    elif numberToSearch <= numbers[mid]:
        high = mid - 1;
    else:
        low = mid + 1;
if ifExist == False:
    print("The number do not exist in the array ");
