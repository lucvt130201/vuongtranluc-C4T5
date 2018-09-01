yob = int(input("your year of birth?"))
age = 2018 - yob
print(age)

if age < 10:
    print("baby")
if age < 18:
    print("teenager")
else:
    print("adult")
