# chars =  input("Enter the sentence you want to count here: ").lower()
chars = "I am a boy".lower()
order_list = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"
              , "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
true_counts ={}
letter_counts = {}
for letter in chars:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
for letter in order_list:
    for another_letter in letter_counts.keys():
        if letter == another_letter:
            true_counts[letter] = letter_counts[letter]
for letter, number in true_counts.items():
    print("{0}: {1}".format(letter, number))