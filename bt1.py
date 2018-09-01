print("Hello, I'm a ninja ")



information = {
    "name": "My name is Kakashi",
    "def": "My defense point is: 9",
    "atk": "My atk point is: 10",
    "hp": "My hp point is: 9"
}
print(*information.keys(), sep = ", ")
# for i in information:
#     print(i, end = " ")
# print()
#     a += [i]
# print(*a, sep = ",")

ask = input("what do you want to know about me?" )


if ask in information == True:
    print(information[ask])

else:
    print("I don't have it  in me,")
    a = int(input("enter new value:"))
    print(a)
    information[ask] = a
    for key, value in enumerate(information):
        print(key, value, information[value])


    # print(information)



