x, y, w, h = map(int,input().split())
if y > h/2:
    b = h-y
else:
    b = y
if x > w/2:
    a = w-x
else:
    a = x
print(min(a,b))
