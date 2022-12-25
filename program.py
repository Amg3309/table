def program():
    a= int(input("Enter a number: "))
    val = int(input("Print the table till? "))
    print("Table of ", a, " till ", val)
    for i in range(val):
        i+=1
        ans=i*a
        print(a, "x", i, "=", ans)

FakeVariable = 1

while FakeVariable == 1:
    program()
