def code():    
    start=['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю',' ']
    main = [start]
    for i in range(len(start)):
        dop = []
        for j in range(1, len(start)):
            dop.append(start[j])
        dop.append(start[0])
        start = dop
        main.append(start)
    key = input('Put the key>> ')
    message = input('Put the message>> ')
    if len(message) > len(key):
        print('key must be longer than message')
    else:
        result = ''
        for i in range(len(message)):
            for j in range(len(main)):
                if main[j][0] == key[i]:
                    ind = 0
                    for k in range(len(main[0])):
                        if main[0][k] == message[i]:
                            ind = k
                    result += main[j][ind]
        return result
def decode():
    start=['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю',' ']
    main = [start]
    for i in range(len(start)):
        dop = []
        for j in range(1, len(start)):
            dop.append(start[j])
        dop.append(start[0])
        start = dop
        main.append(start)
    key = input('Put the key>> ')
    message = input('Put the message>> ')
    result = ''
    for i in range(len(message)):
        ind = 0
        for j in range(len(main)):
            if main[j][0] == key[i]:
                for k in range(len(main[j])):
                    if main[j][k] == message[i]:
                        ind = k
                        result += main[0][ind]
    return result
print('Welcome to the SpecialCoder!')
password=input('Put the password>> ')
if password != 'омега':
    print('Password is incorrect')
else:
    print('Password is right')
    name = input('Put your name>> ')
    print('Hello, mr. '+name)
    command = input('code or decode (к/д)>> ')
    if command == 'к':
        print(code())
    else:
        print(decode())
a=input()
