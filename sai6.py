s=input()
if s.isalpha():
    print("invalid")
else:
    s=int(s)
    if s%4==0:
        print("yes")
    else:
        print("no")
