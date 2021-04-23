import tkinter


root = tkinter.Tk()
root.maxsize(300, 300)
root.minsize(300, 300)
root.configure(bg='#212121')
root.title('Account App')

username_input = tkinter.Text(root)
username_input.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.07)
username_input.insert('1.0', 'Username')

password_input = tkinter.Text(root)
password_input.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.07)
password_input.insert('1.0', 'Password')


def create(file, username, password):
    with open(file, 'a') as File:
        insert = username + ':' + password
        insert = insert.replace('\n', '')
        File.write('\n' + insert)


def remove(file, username, password):
    found = False

    with open(file, 'r') as File:
        text = File.read()
        username = username.replace('\n', '')
        password = password.replace('\n', '')

        if username in text:
            text = text.split('\n')
            for string in text:
                if string == username + ':' + password:
                    found = True

    if found:
        with open(file, 'r') as File:
            text = File.read()
        with open(file, 'w') as File:
            text = text.replace(username + ':' + password, '')
            File.write(text)


def login(file, username, password):
    found = False

    with open(file, 'r') as File:
        text = File.read()
        username = username.replace('\n', '')
        password = password.replace('\n', '')

        if username in text:
            text = text.split('\n')
            for string in text:
                if string == username + ':' + password:
                    found = True

    if found:
        print('logged in successfully!')


def createbutton():
    create('usernames.txt', str(username_input.get('1.0', 'end')).lower(), password_input.get('1.0', 'end'))


def removebutton():
    remove('usernames.txt', str(username_input.get('1.0', 'end')).lower(), password_input.get('1.0', 'end'))


def loginbutton():
    login('usernames.txt', str(username_input.get('1.0', 'end')).lower(), password_input.get('1.0', 'end'))


create_but = tkinter.Button(root, text='Create', command=createbutton)
create_but.place(relx=0.1, rely=0.35, relwidth=0.2)

remove_but = tkinter.Button(root, text='Remove', command=removebutton)
remove_but.place(relx=0.4, rely=0.35, relwidth=0.2)

login_but = tkinter.Button(root, text='Login', command=loginbutton)
login_but.place(relx=0.7, rely=0.35, relwidth=0.2)

root.mainloop()
