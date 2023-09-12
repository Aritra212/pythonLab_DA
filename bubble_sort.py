
def display(arr):
    print("Array Elements ::",end=" ")
    for i in arr:
        print(i,end=" ")

def bubble_sort(arr,n):
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)

def swap(arr,x,y):
    temp=arr[x]
    arr[x]=arr[y]
    arr[y]=temp

if __name__=='__main__':
    n1=int(input("Enter Number Of Elements:: "))
    a=[]
    for i in range(n1):
        a.append(int(input(f"Enter value for array[{i}]: ")))
    bubble_sort(a,n1)
    print("\n====Applying Bubble Sort=====\n")
    display(a)

    