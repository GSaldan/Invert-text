# instruction: type a word or phrase and the computer will invert it

text = input('type a text here: ')

lista = []
string = ''

# string to inverted list
for i in text:
    lista.insert(0, i)

# inverted list to string
for i in lista:
    string += i

print(string)
