from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen
from json import loads, dump
from buying_page import display_products

def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg='black',
        fg='white',
        font='Unispace-Bold 12 ',
        width=20,
        height=2,
        borderwidth=0,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg='green',
        fg='white',
        font='Unispace-Bold 12 ',
        width=20,
        height=2,
        borderwidth=0,
        command=login
    )

    frame.create_window(640, 320, window=register_button)
    frame.create_window(640, 380, window=login_button)


def get_user_data():
    info_data = []

    with open("db/user_info", "r") as users_file:
        info_data.extend(loads(line) for line in users_file)
    return info_data

def login():
    clean_screen()
    frame.create_text(400,
                      250,
                      text="Username:",
                      font='Unispace-Bold 12 ',
                      fill='black',
                      anchor='e'
                      )
    frame.create_text(400,
                      350,
                      text="Password:",
                      font='Unispace-Bold 12 ',
                      fill='black',
                      anchor='e'
                      )

    frame.create_window(510, 250, window=username_box)
    frame.create_window(510, 350, window=password_box)

    login_button = Button(
        root,
        text="Login",
        bg='green',
        fg='white',
        font='Unispace 14 ',
        borderwidth=0,
        command=logging_in
    )

    frame.create_window(670, 440, window=login_button)

def logging_in():
    if check_logging_in():
        frame.create_text(
            470,
            520,
            text="Successfully logged in!Ready to buy?",
            font='Unispace-Bold 18 ',
            fill='green',
            tags='error'
        )
        display_products()
    else:
        frame.create_text(
            470,
            520,
            text="Wrong username or password!Try again!",
            font='Unispace-Bold 18 ',
            fill='red',
            tags='error'
        )

def check_logging_in():
    info_data = get_user_data()

    for record in info_data:
        if record['Username'] == username_box.get() and\
                record['Password'] == password_box.get():
            return True

    return False


def register():
    clean_screen()


    frame.create_text(400, 250, text="First Name:", font='Unispace-Bold 12 ', fill='black', anchor='e')
    frame.create_text(400, 300, text="Last Name:", font='Unispace-Bold 12 ', fill='black', anchor='e')
    frame.create_text(400, 350, text="Username:", font='Unispace-Bold 12 ', fill='black', anchor='e')
    frame.create_text(400, 400, text="Password:", font='Unispace-Bold 12 ', fill='black', anchor='e')

    frame.create_window(510, 250, window=first_name_box)
    frame.create_window(510, 300, window=last_name_box)
    frame.create_window(510, 350, window=username_box)
    frame.create_window(510, 400, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg='black',
        fg='white',
        font='Unispace 14 ',
        borderwidth=0,
        command=registration
    )


    frame.create_window(670, 440, window=register_button)

def registration():
    info_dict = {
        "First Name": first_name_box.get(),
        "Last Name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get()
    }


    if check_registration(info_dict):
        with open("db/user_info", "a") as users_file:
            dump(info_dict, users_file)
            users_file.write("\n")
            display_products()

def check_registration(info_dict):
    frame.delete('error')
    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                470,
                520,
                text=f"{key} cannot be empty!",
                font='Unispace-Bold 18 ',
                fill='red',
                tags='error'
            )

            return False
    info_data = get_user_data()

    for record in info_data:
        if record['Username'] == info_dict['Username']:
            frame.create_text(
                470,
                520,
                text=f"{info_dict['Username']} already exists!Choose another username!",
                font='Unispace-Bold 18 ',
                fill='red',
                tags='error'
            )

            return False

    return True




first_name_box = Entry(root,bd=0,font='Unispace-Bold 12 ', justify='center')
last_name_box = Entry(root,bd=0,font='Unispace-Bold 12 ', justify='center')
username_box = Entry(root,bd=0,font='Unispace-Bold 12 ', justify='center')
password_box = Entry(root,bd=0,font='Unispace-Bold 12 ', justify='center', show='*',)

