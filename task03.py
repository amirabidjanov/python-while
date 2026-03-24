ball = 0
while True:
    password = input('+ yoki stop kiriting:')
    if password == '+':
        ball += 10
    elif password == 'stop':
        break
    elif password != '+ stop':
        print("+ yoki stop kiriting")
   
print(ball)