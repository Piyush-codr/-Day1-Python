'''print("Tickets Mumbai To Dubai")
Ra=37550.0
Rac=
AD=36173.25
a=int(input())
c=int(input())
if(a==5 and c==2):
    print("Total Ticket Cost= ",36173.25*5+13397.5*2)
elif(a==3 and c==1):
    print("Total Ticket Cost= ",36173.25*3+13397.5*1)
else:
    print("ab isse jada nhi")'''


print("Tickets from Mumbai to Dubai")
r=int(input())
c=int(input())
cost=(((37550*r)+(c*(37550/3)))*1.07)*0.90
print(cost)
