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

"""
pos = -1

def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;

    return False


list = [4,7,8,12,45,99,102,702,10987,56666]
n = 7

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not Found")
"""

"""
def binary_search(arr, ele):
    start = 0
    end = len(arr) - 1
    while start <= end:

        mid = (start + end) // 2
        if (arr[mid] == ele):
            return mid
        elif (arr[mid] > ele):
            end = mid - 1
        else:
            start = mid + 1

    return -1


print("Enter The Size Of The Array : ", end="\n")
size = int(input())
arr = []
print("Enter ", size, "Elements  In Ascending Order: ")
for i in range(size):
    ele = int(input())
    arr.append(ele)
print("Enter The Element To Do Binary Search : ", end="\n")
ele = int(input())
res = binary_search(arr, ele)
if (res == -1):
    print("The Element " , ele, "Is  Not Founded In The Array ")
else:
    print("The Element " , ele, " Is present At Index - ", res)
"""
