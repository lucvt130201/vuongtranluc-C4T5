no = 1
like = ["bóng đá", "pepsi", "marvel"]
for item in like:
    text = "{0}. {1}". format(no, item)
    print(text)
    no+=1



update = input("cần thêm:")
like.append(update)
for item in like:
    text = "{0}. {1}". format(no, item)
    print(text)
    no += 1


