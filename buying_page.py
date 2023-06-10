from json import load, dump
from tkinter import Button

from canvas import frame, root
from helpers import clean_screen

from PIL import ImageTk, Image


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    global info

    with open('db/products_data.json', 'r') as stock:
        info = load(stock)

    x, y = 250, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info['image']))
        images.append(item_img)

        frame.create_text(x, y, text=item_name, font='Unispace-Bold 12 ', fill='black', anchor='n')
        frame.create_image(x, y + 150, image=item_img)

        if item_info['quantity'] > 0:
            color = 'green'
            text = f'In stock: {item_info["quantity"]}'
            item_button = Button(
                root,
                text='Buy',
                bg='green',
                fg='white',
                font='Unispace-Bold 12 ',
                bd=0,
                width=10,
                command=lambda x=item_name, y=item_info: buy_product(x, y)
            )

            frame.create_window(x, y + 300, window=item_button)

        else:
            color = 'red'
            text = 'Out of stock'

        frame.create_text(x, y + 255, text=text, font='Unispace-Bold 12 ', fill=color, anchor='n')

        x += 250

        if x > 1050:
            x = 200
            y += 150


def buy_product(product_name, item_info):
    info[product_name]['quantity'] -= 1

    with open('db/products_data.json', 'w') as stock:
        dump(info, stock)

    display_stock()


info = {}
images = []
