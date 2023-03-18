print("Initially money will be considered in INR")
n1=float(input())
currency=input()
INR=1.0
if(currency=="Euro"):
    print(n1*INR*0.01417)
elif(currency=="British_Pound"):
    print(n1*INR*0.0100)
elif(currency=="Australian_Pound"):
    print(n1*INR*0.02140)
elif(currency=="Canadian_Dollar"):
    print(n1*INR*0.02027)
else:
    print(n1*INR)
