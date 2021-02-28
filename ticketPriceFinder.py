A = ("class A is $50")
B = "class B is $30"
C = "class C is $15"

question = (input("What class ticket are you enquiring about? "))
if question == "A" or "a":
    print (A)
elif question == "B" or "b":
    print(B)
elif question == "C" or "c":
    print(C)


