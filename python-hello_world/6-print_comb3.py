combo_list = []
for num in range(90):
    stringed_num = "{:02d}".format(num)

    if (sorted(list(stringed_num)) not in combo_list) and (num != 89):
        combo_list.append(sorted(list(stringed_num)))
        print(stringed_num, end=", ")
    elif (sorted(list(stringed_num)) not in combo_list) and (num == 89):
        print(stringed_num)
    else:
        continue
            

# print(combo_list)