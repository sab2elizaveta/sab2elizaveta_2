books = [
    {'genre': 'поэзия', 'number': '978-5-1000-1234-7', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
    {'genre': 'фэнтези', 'number': '88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
    {'genre': 'детектив', 'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'} ]

directories = {
    '1': ['978-5-1000-1234-7', '88006'],
    '2': ['D-1122'],
    '3': []
}



# Пункт 1. Пользователь по команде “book_info” может найти название книги и её автора

def info_book():

    num = input('Введите номер книги:' + '\n')

    for i in books:
        if i['number'] == num:
            print(f'Название книги : "{i['title']}"', f'Автор: {i['author']}', sep = '\n')
            return
      
    print('Книга не найдена в базе')
    return

# Пункт 2. Пользователь по команде “shelf” может по названию книги узнать, на какой полке она хранится
                  
def shelf():

    name = input('Введите название книги :' + '\n')
    num = 0

    for i in books:
        if i['title'] == name:
            num = i['number']
            break
        
    if num == 0:
        print('Книга не найдена в базе')
        return
        
    for i, j in directories.items():
        if num in j:
            print('Книга хранится на полке -', i)
            return
# Пункт 3. Пользователь по команде “all” может увидеть полную информацию по всем книгам

def all():

    for book in books:
        book_num = book['number']
        
        shelf_id = 0
        for i, j in directories.items():
            if book_num in j:
                shelf_id = i
                break  
        
        print(f'№: {book_num}, жанр: {book["genre"]}, название: "{book["title"]}", автор: {book["author"]}, полка хранения: {shelf_id}')

# Пункт 4. Пользователь по команде “add_shelf” может добавить новую полку

def add_shelf():
    shelf = input('Введите номер полки:')

    if shelf in directories.keys():
        print(f'Такая полка уже существует. Текущий перечень полок: {', '.join(directories.keys())} ')
    else:
        directories.setdefault(shelf, [])
        print(f'Полка добавлена. Текущий перечень полок: {' ,'.join(directories.keys())}')
        return

# Пункт 5. Пользователь по команде “del_shelf” может удалить существующую полку из данных (только если она пустая)

def del_shelf():
    shelf = input('Введите номер полки:' + '\n')

    if shelf not in directories.keys():
        print(f'Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}')
        return
    elif directories[shelf] != [] and shelf in directories.keys():
        print(f'На полке есть книги, удалите их перед удалением полки. Текущий перечень полок: {' ,'.join(directories.keys())}')
        return
    else:
        answer = input('Полку можно удалить. Вы уверены?' + ' да/нет' + '\n')
        if answer == 'да':
           del directories[shelf]
           print(f'Полка удалена. Текущий перечень полок: {', '.join(directories.keys())}')
        else:
           print(f'Полка не удалена. Текущий перечень полок: {', '.join(directories.keys())}')
        return


while True:
  command = input('Введите команду:' + ' ' + '1. book_info, 2. shelf, 3. all, 4. add_shelf, 5. del_shelf, 6. q ' + '- закончить ввод' + '\n').lower().strip()
  match command:
    case 'book_info':
        info_book()
    case 'shelf':
        shelf()
    case'all':
        all()
    case 'add_shelf':
        add_shelf()
    case 'del_shelf':
        del_shelf()
    case 'q':
          print("До свидания!")
          break
    case _:
        print('Нет такой команды')

