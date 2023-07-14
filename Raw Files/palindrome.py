s1=input("Enter String to check Plaidrome :")
print("Converting string to lower case")

s1=s1.lower()
print(s1)



def checkPalidrome() :
    s2=s1[::-1]
    print("Reverse of String",s1," is ", s2)
    if s1 == s2 : 
        print(s1," Is plaidrome of ",s2)
    else :
        print("Not a palidrome")
checkPalidrome()


# print(s2)