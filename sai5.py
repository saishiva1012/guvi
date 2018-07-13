s,d,f=input().split()
if s.isalpha() or d.isalpha() or f.isalpha():
    print("Invalid")
else:
    s=int(s)
    d=int(d)
    f=int(f)
    if s>=d and s>=f:
        print(s)
    elif d>=s and d>=f:
        print(d)
    elif f>=s and f>=d:
        print(f)
