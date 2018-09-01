# item1 = 'thịt xiên'
# item2 = 'phở cuốn'
# item3 = 'bún chả'
# item4 = 'giả cầy'
# item5 = 'bún đậu'
# item6 = 'cơm rang dưa bò'
# item7 = 'tào phớ'


# empty list
# menu = []
# print(menu)

# menu =["thịt xiên"]
# print(menu)

# menu =['thịt xiên', 'phở cuốn','bún chả']
#
#
# print(menu[-1])

# item = menu[0]
# print()
# menu[1] = 'bánh bao'
# print(menu)
# index = 2
# new_value = "bánh bao"
# menu[index] = new new_value


menu =['thịt xiên', 'phở cuốn','bún chả']
no = 1
for item in menu:
    # print(no,'.',item, sep="")
    text = "{0}: {1}". format(no, item)
    print(text)
    no +=1

# menu = ["thịt xiên", "Phở cuốn", "Bánh bao"]
#
# for index, item in enumerate(menu):
#     print(index,item)

# prefixes = ["I","II","III"]
# menu = ["Thịt xiên", "Phở cuốn", "Bánh bao"]
# for p,item in zip(prefixes, menu):
#     print(p, item)

# menu.pop(1)
# # print(*menu, sep = ",")
# l = len(menu)
# print(l)