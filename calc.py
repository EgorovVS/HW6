#Калькулятор   работает если есть только одна пара скобок ((

OPERATORS = {'+': (lambda x,y: float(x)+float(y)), 
            '-': (lambda x,y: float(x)-float(y)),
            '*': (lambda x,y: float(x)*float(y)),
            '/': (lambda x,y: float(x)/float(y)) 
            }

def user_expression():
    user_expression = input('Введите выражение ')
    return user_expression


def exp_to_list(expression):
    expression_list = []
    for i in expression:
        expression_list.append(i)
    # print(expression_list)
    new_expression_list = []
    value = ''
    for i in range(len(expression_list)):
        if expression_list[i].isdigit():
            value+= expression_list[i]
        else:
            new_expression_list.append(value)
            new_expression_list.append(expression_list[i])
            value = ''
        if(i == len(expression_list)-1):
            new_expression_list.append(value)
            expression_list = []
    for i in range(len(new_expression_list)):
        if new_expression_list[i]!='':
            expression_list.append(new_expression_list[i])     
    # print(expression_list)
    return expression_list

def calculation(expression, OPERATORS):
    result = []
    for el in expression:
        for key in OPERATORS.keys():
            if key in expression:
                index = expression.index(key)
                result.append(expression[index-1])
                result.append(expression[index])
                result.append(expression[index+1])
                res = OPERATORS[key](float(result[0]),float(result[2]))
                result.pop(index+1)
                result[index] = res
                result.pop(index-1)
                return result

def calc_if_par(expression):
    for el in range(len(expression)):
        if expression[el] == ')':
            index2 = el
            while expression[el]!= '(':
                el-=1
            index1 = el
            temp = expression[index1+1:index2]
            res = calculation(temp,OPERATORS)
            expression[index1:index2+1]=res
            return expression
       
user_exp = user_expression()
user_exp = exp_to_list(user_exp)
pre_answer = calc_if_par(user_exp)
print(pre_answer)
answer = calculation(pre_answer,OPERATORS)
print(f'Ваше выражение равно {answer}')
  