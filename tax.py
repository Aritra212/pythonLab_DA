# Calculate Tax Input of Given Income Amount
def tax(amount):
    if amount<10000:
        return 0.0
    elif amount>=10000 and amount<50000:
        return (amount*5/100)
    elif amount>=50000 and amount<100000:
        return (amount*10/100)
    else:
        return (amount*15/100)

def main():
    while(1):
        print("------------------------------------")
        ch=int(input("\nEnter 0 to exit\nEnter 1 to calculate tax...\nEnter your choice:: "))
        if ch==0:
            break
        elif ch==1:
            income=float(input("\nEnter Your Income(Rs.): "))
            print(f"\nYour tax input is {tax(income)} Rs.")
        else:
            print("\nInvalid choice!! Try again")
main()