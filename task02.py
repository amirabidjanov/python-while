password1 = input('parol qo\'ying:')
while True:
    password = input('parolni kiriting:')
    if password == password1:
        print('xush kelibsiz')
        break
    elif password != password1:
        print('xato qayta urunib ko\'ring')