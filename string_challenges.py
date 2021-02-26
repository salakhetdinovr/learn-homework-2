# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
sum = 0
word_dict = ('а','у','о','ы','и','э','я','ю','ё','е')
for x in word.lower():
    if x in word_dict:
        sum += 1
print(sum)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
z = sentence.split(' ')
print(len(z))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for x in sentence.split(' '):
    print(x[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sum_2 = 0
z = sentence.split(' ')
for x in z:
    sum_2 += len(x)
y = sum_2 / len(z)
print(y)