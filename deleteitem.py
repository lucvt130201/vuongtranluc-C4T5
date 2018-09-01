# menu = ["thịt chó", "phở cuốn", "ốc luộc", "bánh bao"]
# #
# # for index, item in enumerate(menu):
# #     print (index, item)
# #
# # remove = input("which item do you want to remove?")
# # menu.remove(remove)
# #
# # for index, item in enumerate(menu):
# #     print(index, item)

favs = ["thịt chó", "phở cuốn", "ốc luộc", "bánh bao"]

for index, fav in enumerate (favs):
    text = "{0}. {1}". format(index+1,fav)
    print(text)

position_remove = int(input('which pistion do you want to remove?'))
favs.pop(position_remove)

for index, fav in enumerate (favs):
    text = "{0}. {1}". format(index+1,fav)
    print(text)

