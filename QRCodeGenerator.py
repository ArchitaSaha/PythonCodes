import qrcode
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
from tkinter import Tk, Entry, Label, Button, StringVar, Frame

def generate():
    img = qrcode.make(message.get())
    img.save(filename.get() + '.png')

    im = Image.open(filename.get() + '.png')

    global height
    height += im.height
    window.geometry(f'{width}x{height}')

    qrFrame.pack()
    image1 = ImageTk.PhotoImage(im)
    qrLabel.configure(image=image1)
    qrLabel.image = image1
    qrLabel.pack()

    window.eval('tk::PlaceWindow . center')

def reset():
    global height
    if height > 340:
        height = 340
        window.geometry(f'{width}x{height}')
        window.eval('tk::PlaceWindow . center')

    messageEntry.delete(0, 'end')
    filenameEntry.delete(0, 'end')
    qrLabel.pack_forget()
    qrFrame.pack_forget()

    messageEntry.focus_set()

def toggleButton(*_):
    if message.get() and filename.get():
        generateButton['state'] = 'normal'
    else:
        generateButton['state'] = 'disabled'

if __name__ == '__main__':
    width = 800
    height = 340

    window = Tk()
    window.configure(bg='white')
    window.geometry(f'{width}x{height}')
    window.title('QR Code Generator')
    window.resizable(0, 0)
    window.eval('tk::PlaceWindow . center')

    message = StringVar()
    filename = StringVar()
    message.set('')
    filename.set('')

    message.trace_add('write', toggleButton)
    filename.trace_add('write', toggleButton)

    topLabel = Label(window, font=('broadway', 14), bg='black', fg='white', text='QR Code Generator')
    topLabel.pack(padx=20, pady=20)

    messageFrame = Frame(window, width=600, height=100, bg="white")
    messageFrame.pack(padx=20)

    messageLabel = Label(messageFrame, font=('times', 14), bg='white', fg='black', width=20, anchor='w', text='Enter text to be encoded')
    messageLabel.pack(padx=20, pady=20, side='left')

    messageEntry = Entry(messageFrame, bd=1, bg='white', width=60, font=('times', 14), justify='center', textvariable=message)
    messageEntry.focus_set()
    messageEntry.pack(padx=20, pady=20, side='right')

    filenameFrame = Frame(window, width=600, height=100, bg="white")
    filenameFrame.pack(padx=20)
    
    filenameLabel = Label(filenameFrame, font=('times', 14), bg='white', fg='black', width=20, anchor='w', text='Save file as')
    filenameLabel.pack(padx=20, pady=20, side='left')

    filenameEntry = Entry(filenameFrame, bd=1, bg='white', width=60, font=('times', 14), justify='center', textvariable=filename)
    filenameEntry.pack(padx=20, pady=20, side='right')

    buttonFrame = Frame(window, width=600, height=100, bg="white")
    buttonFrame.pack(padx=20)

    generateButton = Button(buttonFrame, text='Generate', width=10, height=2, font=15, bg='white', bd=1, state='disabled', command=generate)
    generateButton.pack(padx=20, pady=20, side='left')

    resetButton = Button(buttonFrame, text='Reset', width=10, height=2, font=15, bg='white', bd=1, command=reset)
    resetButton.pack(padx=20, pady=20, side='right')

    qrFrame = Frame(window, width=300, height=300, bg="pink")
    qrLabel = Label(qrFrame)
    
    window.mainloop()