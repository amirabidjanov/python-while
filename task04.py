while True:
    sorash = input('boshlaymizmi:')
    if sorash == 'yoq':
        print('salomat bo\'ling')
        break
    while sorash == 'ha':
        num1 = int(input('son kiriting:'))
        ishora = input('+ - * / kiriting:')
        num2 = int(input('son kiriting:'))
        if  ishora == '+':
            print(num1 + num2)
        elif  ishora == '-':
            print(num1 - num2)    
        elif  ishora == '/':
            if num1 == 0 or num2 == 0:
                print('sonni 0 ga bo\'lish mumkin emas.')
                break    
            print(num1 / num2)
        elif  ishora == '*':
            print(num1 * num2)
        sorash = input('yana ishlaymizmi:')
        if sorash == 'yoq':
            print('salomat bo\'ling')
            break

