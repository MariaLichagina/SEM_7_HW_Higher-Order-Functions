
# # Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм 
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из 
# одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def count_as(str):
    dictionary_vowels = {}
    for i in 'а, у, о, ы, э, я, ю, ё, и, е'.split(', '):
        dictionary_vowels.update({i: 'vowels_rus'})
    count = 0
    for i in list(str):
        if i in dictionary_vowels.keys():
                count += 1 
    return count
    
txt = list(map(str, input("Введите кричалку: ").lower().split()))
print(txt)

count_first_el = count_as(txt[0])
print(count_first_el)

theSame = True
i = 1
while i < len(txt) and theSame == True:
    count_next_el = count_as(txt[i])
    print(count_next_el)
    if count_next_el != count_first_el:
        theSame = False
    else: 
        i += 1
        
if theSame == False:
    print('Пам парам')
else:
    print('Парам пам-пам')

        
 




