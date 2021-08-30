my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)
my_list_new = []

for el in my_list:

    if el.isdigit() or (el[0] == '+' or el[0] == '-' and el[1].isdigit()):
        if el.isdigit():
            el = f'{int(el):02d}'
            my_list_new.extend(['"', el, '"'])
        else:
            el = el[0] + f'{int(el):02d}'
            my_list_new.extend(['"', el, '"'])
    else:
        my_list_new.append(el)

print(my_list_new)

s = ' '.join(my_list_new)
print(s)
