import qrcode
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
from tkinter import Tk, Entry, Label, Button, StringVar, Frame, filedialog

def generate():
    img = qrcode.make(message.get())
    img.save(filename.get() + '.png')

    im = Image.open(filename.get() + '.png')
    
    displayImage(im, qrFrame, qrLabel)

def displayImage(im, frame, label):
    global height
    height += im.height + 20
    root.geometry(f'{width}x{height}')

    frame.pack()
    image1 = ImageTk.PhotoImage(im)
    label.configure(image=image1)
    label.image = image1
    label.pack()

    root.eval('tk::PlaceWindow . center')

def reset():
    global height
    if height > 340:
        height = 540
        root.geometry(f'{width}x{height}')
        root.eval('tk::PlaceWindow . center')

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

def switchToGenerate():
    global height
    # height = height + 340 if height == 200 else height
    root.geometry(f'{width}x{height}')

    window.pack(fill='both', expand=1)
    screen.pack_forget()

def switchToScan():
    screen.pack(fill='both', expand=1)
    window.pack_forget()

def browse():
    file = filedialog.askopenfilename(parent=root, title='Select QR image', filetypes=(('PNG Images', '*.png'),('All Files', '*.*')))
    if file != None:
        scannedImage = Image.open(file)
        displayImage(scannedImage, displayFrame, displayLabel)

if __name__ == '__main__':
    width = 800
    height = 500

    root = Tk()
    root.configure(bg='white')
    root.geometry(f'{width}x{height}')
    root.title('QR Code Generator')
    root.resizable(0, 0)
    root.eval('tk::PlaceWindow . center')

    # The two frames
    window = Frame(root)    # Generate QR Code
    screen = Frame(root)    # Scan QR Code

    # Navigation Bar
    navFrame = Frame(root, width=600, height=100, bg="white")
    navFrame.pack(padx=20)

    genButton = Button(navFrame, text='Generate QR Code', width=25, height=2, font=15, bg='white', bd=1, command=switchToGenerate)
    genButton.pack(padx=20, pady=20, side='left')

    scanButton = Button(navFrame, text='Scan QR Code', width=25, height=2, font=15, bg='white', bd=1, command=switchToScan)
    scanButton.pack(padx=20, pady=20, side='right')

    # Scan QR Code
    browseButton = Button(screen, text='Browse QR Images', width=20, height=2, font=15, bg='white', bd=1, command=browse)
    browseButton.pack(padx=20, pady=20)

    displayFrame = Frame(screen, width=300, height=300, bg="pink")
    displayLabel = Label(displayFrame)

    # Generate QR Code
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
    
    root.mainloop()