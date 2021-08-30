my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)

i = 0
while i < len(my_list):

    if my_list[i].isdigit() or (my_list[i][0] == '+' or my_list[i][0] == '-' and my_list[i][1].isdigit()):
        if my_list[i].isdigit():
            my_list[i] = f'{int(my_list[i]):02d}'
        else:
            my_list[i] = my_list[i][0] + f'{int(my_list[i]):02d}'
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 2
    else:
        i += 1

print(my_list)

s = ' '.join(my_list)
print(s)
