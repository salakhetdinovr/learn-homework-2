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
sum_2 = 0
for x in sentence.split(' '):
    sum_2 += 1
print(sum_2)



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for x in sentence.split(' '):
    print(x[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
for x in sentence.split(' '):
    print(len(x) / 2)