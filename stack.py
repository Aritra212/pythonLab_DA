stack=[]
def push(data):
     stack.append(data)
     display()
     
def pop():
     if len(stack)==0:
          print("Stack empty!!")
     else:
          stack.pop()
          display()
     
def display():
     i=len(stack)-1
     
     if len(stack)==0:
          print("Stack empty!!")
          
     while i>=0 :
          print(stack[i],end=' ')
          i=i-1
     print()
          
while(1):
     print("------------------------")
     print("Enter 1 to push")
     print("Enter 2 to pop")
     print("Enter 3 to display")
     print("Enter 0 to Exit")
     ch=int(input("Enter your choice:: "))
     if ch==0:
          break
     elif ch==1:
          d=int(input("Enter data:"))
          push(d)
     elif ch==2:
          pop()
     elif ch==3:
          display()
     else:
          print("Invalid choice!!")

