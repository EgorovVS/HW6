# #Калькулятор   работает если есть только одна пара скобок ((

# OPERATORS = {'+': (lambda x,y: float(x)+float(y)), 
#             '-': (lambda x,y: float(x)-float(y)),
#             '*': (lambda x,y: float(x)*float(y)),
#             '/': (lambda x,y: float(x)/float(y)) 
#             }

# def user_expression():
#     user_expression = input('Введите выражение ')
#     return user_expression


# def exp_to_list(expression):
#     expression_list = []
#     for i in expression:
#         expression_list.append(i)
#     # print(expression_list)
#     new_expression_list = []
#     value = ''
#     for i in range(len(expression_list)):
#         if expression_list[i].isdigit():
#             value+= expression_list[i]
#         else:
#             new_expression_list.append(value)
#             new_expression_list.append(expression_list[i])
#             value = ''
#         if(i == len(expression_list)-1):
#             new_expression_list.append(value)
#             expression_list = []
#     for i in range(len(new_expression_list)):
#         if new_expression_list[i]!='':
#             expression_list.append(new_expression_list[i])     
#     # print(expression_list)
#     return expression_list

# def calculation(expression, OPERATORS):
#     result = []
#     for el in expression:
#         for key in OPERATORS.keys():
#             if key in expression:
#                 index = expression.index(key)
#                 result.append(expression[index-1])
#                 result.append(expression[index])
#                 result.append(expression[index+1])
#                 res = OPERATORS[key](float(result[0]),float(result[2]))
#                 result.pop(index+1)
#                 result[index] = res
#                 result.pop(index-1)
#                 return result

# def calc_if_par(expression):
#     for el in range(len(expression)):
#         if expression[el] == ')':
#             index2 = el
#             while expression[el]!= '(':
#                 el-=1
#             index1 = el
#             temp = expression[index1+1:index2]
#             res = calculation(temp,OPERATORS)
#             expression[index1:index2+1]=res
#             return expression
       
# user_exp = user_expression()
# user_exp = exp_to_list(user_exp)
# pre_answer = calc_if_par(user_exp)
# print(pre_answer)
# answer = calculation(pre_answer,OPERATORS)
# print(f'Ваше выражение равно {answer}')

#  Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из 
# какой-то книги, а втором файлике — сжатая версия этого текста). 



# def after_encoding(text):
#     encoded_list = []
#     count = 1
#     for el in range(len(text)):       # не проверяется последний набор символов, я не знаю как исправить
#         if el == len(text)-1:
#             encoded_list.append(str(count))
#             encoded_list.append(text[el])
#         elif text[el] == text[el+1]:
#             count+=1
#         else:
#             encoded_list.append(str(count))
#             encoded_list.append(text[el])
#             count = 1
#             encoded_str = ''.join(encoded_list)
#     return encoded_str

# def before_decoding(text):
#     decoded_list = []
#     value = 0
#     for el in range(len(text)):
#         if text[el].isdigit():
#             value = value*10+int(text[el])
#         else:
#             decoded_list.append(value*text[el])
#             value = 0
#     decoded_list ="".join(decoded_list) 
#     return decoded_list      

# with open('list1.txt', 'r') as doc:
#     text = doc.read()
#     print(text)
# encoded_str = after_encoding(text)
# print(encoded_str)
# decoded_str = before_decoding(encoded_str)
# print(decoded_str)
# with open('list2.txt', 'w') as doc:
#     doc.write(encoded_str)


# # 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 
# # 13 букв после нее в алфавите. 
# # ROT13 является примером шифра Цезаря.
# # Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# # Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# # Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# # Не использовать функцию encode.

# alphabeth = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"

# text = input('Write some text...')
# text = text.upper()
# encoded_text =''.join([alphabeth[(alphabeth.find(i)+13)%26] for i in text])
# print(encoded_text)
# decoded_text=''.join([alphabeth[(alphabeth.find(i)-13)%26] for i in encoded_text])
# print(decoded_text)
