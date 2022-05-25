import ui


def get_input(req):
    answer = []
    for i in req:
        print(f'\nВведите {i}:')
        answer.append(input())
    return answer


def get_add():
    request = ['Фамилию:', 'Имя:', 'Отчество:', 'номер телефона:', 'принадлежность телефона (рабочий/личный):',
               'тип телефона (сотовый/стационарный):', 'описание:']
    data = get_input(request)
    with open('people.csv', 'a') as file:
        file.writelines(
            f'{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}\n')


def get_remove():
    request = ['в строку уникальные данные содержащиеся в строке подлежащей удалению:']
    data = (','.join((''.join((get_input(request)))).split(' '))).split(',')
    db_remove = []
    db_new = []
    with open('people.csv', 'r') as file:
        for line in file:
            match = True
            for key in data:
                if key not in line:
                    match = False
            if match:
                db_remove.append(line.replace('\n', ''))
            else:
                db_new.append(line.replace('\n', ''))
    print('По указанным параметрам подобраны строки:')
    [print(line) for line in db_remove]
    if input('Y - если вы хотите удалить указанные строки:\n') == 'Y':
        with open('people.csv', 'w') as file:
            [file.writelines(f'{line}\n') for line in db_new]


def get_find():
    request = ['в строку уникальные данные содержащиеся в строке подлежащей поиску:']
    data = (','.join((''.join((get_input(request)))).split(' '))).split(',')
    db_remove = []
    with open('people.csv', 'r') as file:
        for line in file:
            match = True
            for key in data:
                if key not in line:
                    match = False
            if match:
                db_remove.append(line.replace('\n', ''))
    print('По указанным параметрам подобраны строки:')
    [print(line) for line in db_remove]


def get_out():
    file_name = input('Введите имя файла для выгрузки данных: ')+'.csv'
    request = [
        'Все данные построчно, разделитель - пустая строка; Один контакт - одна строка. Разделители - точка с запятой']
    choice = ui.get_choice(request[0])
    if choice == 1:
        pattern = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n\n'
    elif choice == 2:
        pattern = '{0};{1};{2};{3};{4};{5};{6}\n'
    with open('people.csv', 'r') as file:
        temp = [line.replace('\n','').split(',') for line in file]
    with open(file_name,'w') as output:
        [output.writelines(pattern.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]) for x in temp)]