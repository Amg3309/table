def program():
    a= int(input("Enter a number: "))
    print("Table of ", a, " till 10")
    for i in range(10):
        i+=1
        ans=i*a
        print(a, "x", i, "=", ans)

FakeVariable = 1

while FakeVariable == 1:
    program()
