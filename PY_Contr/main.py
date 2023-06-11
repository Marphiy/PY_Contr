import json
import os
from time import strftime


def NotePrint(note):
    print(f'id:                 {note.get("id")}\nTitle:              {note.get("Title")}'
          f'\nNote:               {note.get("Body")}\nComposed:           {note.get("Time")}\n\n')


def Validation(cose):
    while True:
        try:
            edited_id = int(input(f'Enter note id to {cose}: '))
            return edited_id
        except ValueError:
            print('No such item!')
            break


def DictToJsnFile(file_name, dict_name):
    with open(file_name, 'w') as f_n:
        f_n.write(json.dumps(dict_name))


def CreateNFillFile(file_name):
    notes = [{"id": 1, "Title": "Empty", "Body": "Nothing",
              "Time": strftime("%Y-%m-%d %H:%M:%S")}]
    DictToJsnFile(file_name, notes)


def ClrScr():
    os.system('sls' if os == 'nt' else 'clear')


file_name = 'notes.json'
ClrScr()

try:
    with open(file_name) as f_n:
        notes = json.load(f_n)
except FileNotFoundError:
    CreateNFillFile(file_name)
    with open(file_name) as f_n:
        notes = json.load(f_n)

try:
    id = notes[-1].get('id')
except IndexError:
    notes = [{"id": 1, "Title": "Empty", "Body": "Nothing",
              "Time": strftime("%Y-%m-%d %H:%M:%S")}]

edited_id = 0

while True:

    menu = input('                        MENU\n'
                 '                    show -  show all\n'
                 '                    new  -  compose\n'
                 '                    edit -  edit\n'
                 '                    find -  find by title\n'
                 '                    date -  find by date\n'                                 
                 '                    del  -  remove\n'             
                 '                    esc  -  exit\n\n')

    if menu == 'new':
        id += 1
        ClrScr()
        title = input('\nEnter new note title: ')
        body = input('Enter note: ')
        notes.append({'id': id, 'Title': title, 'Body': body,
                     'Time': strftime("%Y-%m-%d %H:%M:%S")})
        ClrScr()
        print('New note composed successfully!\n')

    elif menu == 'esc':
        DictToJsnFile(file_name, notes)
        ClrScr()
        print('Buy!\n\n')
        break

    elif menu == 'show':
    
        if notes != []:
            for n in notes:
                NotePrint(n)
        else:
            print('The NoteBook is empty!\n\n')
            id = 0
        input('"Enter" - MENU')
        ClrScr()

    elif menu == 'find':
        ClrScr()
        title = input('\nEnter title: ')
        found = 0
        for n in notes:
            if n.get('Title') == title:
                NotePrint(n)
                found = 1
                input('"Enter" - MENU')
        if found == 0:
            ClrScr()
            print('No such item!\n\n')
            
    elif menu == 'date':
        ClrScr()
        date = input('\nEnter composing date (YYYY-MM-DD): ')
        found = 0
        for n in notes:
            if date in n.get('Time'):
                NotePrint(n)
                found = 1
        if found == 0:
            ClrScr()
            print('No such item!\n\n')    
        input('"Enter" - MENU')  
        ClrScr()  

    elif menu == 'edit':
        ClrScr()
        edited_id = Validation('edit')
        ClrScr()
        found = 0
        for n in notes:
            if n.get('id') == edited_id:
                found = 1
                title = input('Note title: ')
                body = input('Note: ')
                n['Title'] = title
                n['Body'] = body
                n['Time'] = strftime("%Y-%m-%d %H:%M:%S")
                ClrScr()
                print('Edited successfully!\n')
        if found == 0:
            ClrScr()
            print('No such item!\n\n')

    elif menu == 'del':
        ClrScr()
        found = 0
        edited_id = Validation('remove')
        for n in notes:
            if n.get('id') == edited_id:
                found = 1
                cnfrmtn = input('Sure? - y/n: ')
                if cnfrmtn == 'y':
                    notes.remove(n)
                    ClrScr()
                    print('Removed successfully!\n')
                else:
                    print("The note's still alive!")
        if found == 0:
            ClrScr()
            print('No such item!\n\n')

    else:
        ClrScr()
        print('Invalid command')
