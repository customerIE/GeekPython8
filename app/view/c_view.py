# тут будет жить CLI
from app.controller import ctrl
def menu():
    print('\nГлавное меню'
          '\n1.Показать все контакты\n'
          '2.Поиск контакта\n'
          '3.Добавить контакт\n'
          '4.Удалить контакт\n'
          '0.Выход')
    return(int(input('->> ')))
def main_loop():
    while True:
        choise = menu()
        match choise:
            case 1:
                data = ctrl.get_data_from_database('')
                for record in data:
                    print(f'{record[0]} \t {record[1]}')
                input('нажмите enter для продолжения')
            case 2:
                print('find')
            case 3:
                print('add')
            case 4:
                ctrl.remove_data_from_database(data)
                print('delete')
            case 0:
                break
                
def init():
    main_loop()
  