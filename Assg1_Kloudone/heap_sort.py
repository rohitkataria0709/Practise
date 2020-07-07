
def heapify(arr, x, j):
   largest = j 
   left = 2 * j + 1
   right = 2 * j + 2 
   
   if left < x and arr[j] < arr[left]:
      largest = left
   
   if right < x and arr[largest] < arr[right]:
      largest = right
   
   if largest != j:
      arr[j],arr[largest] = arr[largest],arr[j] 
      # root.
      heapify(arr, x, largest)

def heapSort(arr):
   x = len(arr)
   
   for j in range(x, -1, -1):
      heapify(arr, x, j)
   
   for j in range(x-1, 0, -1):
      arr[j], arr[0] = arr[0], arr[j]
      heapify(arr,j, 0)

arr = [10,20,80,90,70,60,50]
heapSort(arr)
x = len(arr)
print ("Sorted array is")
for j in range(x):
   print (arr[j],end=" ")
