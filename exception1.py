l=[1,2,3,4,5,6]
try:
    for i in range(10):
        print(l[i])
except IndexError:
    print("index error")
else:
    print("no error")
