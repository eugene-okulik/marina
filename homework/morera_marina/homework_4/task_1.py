my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': [1, 3, 5, 7, 9],
           'dict': '{"language": "python", "size": "small", "color": "blue", "animal": "cat", "month": "may"}',
           'set': {'hello!', 'Bye', 'Good', 'Bad', 'Great'}}

print('Последний элемент', my_dict['tuple'][-1])
my_dict['list'].append(0)
my_dict['list'].pop(2)
new_dict = eval(my_dict['dict'])
new_dict['i am a tuple'] = 'nope'
new_dict.pop("size", "small")
my_dict['dict'] = str(new_dict)
my_dict['set'].add("Night")
my_dict['set'].pop()
print('Весь словарь', my_dict)
