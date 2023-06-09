from tkinter import Tk, Canvas

def create_root():
    root = Tk()
    root.title("GUI-Shop by vo1d.null")
    root.geometry("1280x720")
    root.resizable(False, False)


    return root



def create_frame():
    frame = Canvas(root, width=1280, height=720)
    frame.grid(row = 0, column = 0)


    return frame

root = create_root()
frame = create_frame()
