def calculate(str_to_parse,l):
    if len(str_to_parse) == 0 or str_to_parse[0] == ')':
        while len(l) != 1:
            res = calc_single_op(l[0], l[1], l[2])
            l = l[2:]
            l[0] = res
        return l[0]
    num_start = 0
    mul_or_div = False
    oper = ''
    for i in range(len(str_to_parse)):
        if str_to_parse[0] == '(':
            res = calculate(str_to_parse[1:], [])
            l.append(res)
        elif not str_to_parse[i].isdigit():
            num = int(str_to_parse[num_start:i])
            if len(oper) != 0:
                l[-1] = calc_single_op(l[-1], oper, num)
                oper = ''
            else:
                l.append(num)
            if (str_to_parse[i] == '/' or str_to_parse[i] == '*'):
                oper = str_to_parse[i]
            else:
                l.append(str_to_parse[i])
def calc_single_op(num1, o, num2):
    match oper:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2















