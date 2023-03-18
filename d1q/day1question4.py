f=int(input())
o=int(input())
z=int(input())
if(f>=z//5 and o>=z%5):
    if(z!=f*5+o&1):
        print("five coins:",z//5)
        print("One coins:",z%5)
else:
    print("-1")
    

    
