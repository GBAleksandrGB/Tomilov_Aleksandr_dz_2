prices_list = [57.8, 46.51, 97, 48.3, 54, 69.7, 88, 100, 33.35, 27.99, 99.9, 67, 50.1]
print(prices_list, id(prices_list))

for price in prices_list:
    price = f'{price:.2f}'
    price = price.split('.')
    price = '{} руб {} коп'.format(price[0], price[1])
    print(price, end=', ')
print()

prices_list.sort()
print(prices_list, id(prices_list))

new_sort_list = sorted(prices_list, reverse=True)
print(new_sort_list, id(new_sort_list))

print(new_sort_list[:5])
