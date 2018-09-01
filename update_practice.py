item_fav = ['chó','pepsi','bóng đá']
print(*item_fav, sep=",")
frefixes = ["I","II", "III", "IV"]
i = 0
for item in item_fav:
    p = frefixes[i]
    index = "{0}. {1}". format(p, item)
    print(index)

    i += 1

update_pos = int(input("position is:")) - 1
update_fav = input('new favorite is:')
item_fav[update_pos] = update_fav

print(*item_fav, sep=",")
for item in  item_fav:
    index = "{0}. {1}". format(no, item)
    print (index)
    no += 1