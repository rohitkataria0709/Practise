position = 0
def binary_search(list,s):
    lower=0
    upper=len(list)-1
    
    while(lower<=upper):
        middle=(lower+upper)//2

        if(list[middle]==s):
            position=middle
        else:
            if(list[middle]<s):
                lower=middle+1
            else:
                upper=middle-1
    return False


n=int(input('Enter number of elements '))
list=[]
for i in range(n):
    print('Enter elements in the ascending order ')
    e=int(input())
    list.append(e)
    
print(list)

s=int(input('Enter element to be searched '))

if binary_search(list, s):
    print('Found at ',position+1)
else:
    print('element not found')

