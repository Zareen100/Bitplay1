# def numberofbits(n):
#     ones=0
#     zeros=0
#     while(n):
#         if(n&1==1):
#             ones+=1
#         else:
#             zeros+=1
#         n>>=1
#     print("number of ones===",ones,"number of zeroes", zeros)
# number=int(input("Enter the number"))
# numberofbits(number)
#program to check if n is Bit or not
def setbit(num,n):
    if num&(1<<(n-1)):
        print("set")
    else:
        print("not set")
num=int(input("enter number"))
n=int(input("enter bit number"))
setbit(num,n)


