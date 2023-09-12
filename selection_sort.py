def selection_sort(arr,n):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        if min!=i:
            swap(arr,i,min)

def swap(arr,x,y):
    temp=arr[x]
    arr[x]=arr[y]
    arr[y]=temp

def display(arr):
    print("Array Elements ::",end=" ")
    for i in arr:
        print(i,end=" ")

if __name__=='__main__':
    n1=int(input("Enter Number Of Elements:: "))
    a=[]
    for i in range(n1):
        a.append(int(input(f"Enter value for array[{i}]: ")))
    selection_sort(a,n1)
    print("\n====Applying Selection Sort=====\n")
    display(a)