from tkinter import *
from LaneLines1 import *
import threading

import multiprocessing

def init(self, master):
    self.startButton = Button(master, text='Start', command=self.start).pack()
    self.stopButton = Button(master, text='Stop', command=self.stop).pack()

def backgroundStart(start):
    global p
    p = multiprocessing.Process(target=start, args=(e,))
    #t = threading.Thread(target=start)
    p.start()

def backgroundStop(stop):
    t = threading.Thread(target=stop)
    t.start()


def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("640x480")

    # A Label widget to show in toplevel
    Label(newWindow).pack()

def start(e):
    cap1(e)
    return

def stop():
    # exit()
    e.set()
    p.join()
    quit()
    #os.close(cap1())
    window.destroy()

def exit():
    window.destroy()
    pass
    # sys.exit()
    # raise SystemExit

# def stopExit():
#     if stop() == True and exit() == True:
#         sys.exit()

# def background():
#     time.sleep(1)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    window = Tk()
    window.title("Welcome")
    window.geometry("640x480")
    lbl = Label(window, text="Hello").pack()

    #lbl.grid(column=0, row=0)


    btn1 = Button(window, text="Start", bg="green", command=lambda: backgroundStart(start)).pack()
    # btn1.grid(column=1, row=0)

    btn2 = Button(window, text='Stop', bg='red', command=lambda: backgroundStop(stop)).pack() #lambda: backgroundStop(stop)
    # btn2.grid(column=1, row=1)

    menu = Menu(window)
    menu.add_command(label = "File")
    menu.add_command(label = 'Edit')
    menu.add_command(label = 'Help')
    window.config(menu=menu)
    window.mainloop()



