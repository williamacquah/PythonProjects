def calculate_love_score(name1, name2):
    total1 = 0
    total2 = 0
    string1 = "true"
    string2 = "love"
    combined_names = (name1 + name2).lower()
    for char in string1:
        count1 = combined_names.count(char)
        total1 += count1
    for char in string2:
        count2 = combined_names.count(char)
        total2 += count2
    combined = int(str(total1) + str(total2))
    print(combined)

calculate_love_score("Kanye West", "Kim Kardashian")

