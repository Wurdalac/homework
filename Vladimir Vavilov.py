s= 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'

#Kоличество символов:107
print(len(s)) 
#Развернуть строку:!акеволеч гурд — модварпу сан у А .акеволеч гурд — акабос мат ,тежоМ .алыб ен я ,енодноЛ в мат как ,юанз еН
print(s [::-1])
#Каждое слово с большой буквы: Не Знаю, Как Там В Лондоне, Я Не Была. Может, Там Собака — Друг Человека. А У Нас Управдом — Друг Человека!
print(s.title())
#Весь текст прописными буквами:не знаю, как там в лондоне, я не была. может, там собака — друг человека. а у нас управдом — друг человека!
print(s.lower())
#Найти число вхождений "нд"-1, "ам"-2, "о"-7     в строку
print(s.count('нд'))
print(s.count('ам'))
print(s.count('о'))
#Собственные упражнения:
print(s.swapcase())
#нЕ ЗНАЮ, КАК ТАМ В лОНДОНЕ, Я НЕ БЫЛА. мОЖЕТ, ТАМ СОБАКА — ДРУГ ЧЕЛОВЕКА. а У НАС УПРАВДОМ — ДРУГ ЧЕЛОВЕКА!
print(s, end='*****')
#Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!*****
#Вывести в консоль исходную строку