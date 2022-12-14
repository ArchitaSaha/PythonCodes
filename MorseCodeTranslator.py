from tkinter import Tk, Entry, Label, Button, StringVar, Frame

morseCodeAlphabet = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def reset(entry):
    entry.delete(0, 'end')
    entry.focus_set()
    displayLabel.pack_forget()

def encrypt():
    text = message.get()
    print(text)
    encryptedMessage = ''
    for c in text.upper():
        if c in morseCodeAlphabet.keys():
            print(c, morseCodeAlphabet[c.upper()])
            encryptedMessage += morseCodeAlphabet[c] + ' '
    
    displayLabel.configure(text = encryptedMessage.strip())
    displayLabel.pack()

    # return encryptedMessage.strip()

def decrypt():
    code = message.get()
    print('code :', code)
    decryptedMessage = ''
    for c in code.split(' '):
        print(c, type(c))
        if c in morseCodeAlphabet.values():
            print(tuple(morseCodeAlphabet.keys())[tuple(morseCodeAlphabet.values()).index(c)])
            decryptedMessage += tuple(morseCodeAlphabet.keys())[tuple(morseCodeAlphabet.values()).index(c)]

    displayLabel.configure(text = decryptedMessage)
    displayLabel.pack()
    # return decryptedMessage

def switchToEncrypt():
    reset(messageEntry)
    messageFrame.pack(padx=20)
    submitButton.configure(command=encrypt, text='Convert to Morse Code')
    buttonFrame.pack()

def switchToDecrypt():
    reset(messageEntry)
    messageFrame.pack(padx=20)
    submitButton.configure(command=decrypt, text='Convert from Morse Code')
    buttonFrame.pack()

def toggleButton(*_):
    if message.get():
        submitButton['state'] = 'normal'
        resetButton['state'] = 'normal'
    else:
        submitButton['state'] = 'disabled'
        resetButton['state'] = 'disabled'

def callback(s):
    s = set(s)
    try:
        s.remove(".")
        s.remove("-")
        s.remove(" ")
    except:
        None
    if (len(s) > 0):
        return False
    else:
        return True

if __name__ == '__main__':
    width = 800
    height = 500

    root = Tk()
    root.configure(bg='white')
    root.geometry(f'{width}x{height}')
    root.title('Morse Code Translator')
    root.resizable(0, 0)
    root.eval('tk::PlaceWindow . center')

    # Navigation Bar
    navFrame = Frame(root, width=600, height=100, bg="white")
    navFrame.pack(padx=20)

    genButton = Button(navFrame, text='Encrypt to Morse Code', width=25, height=2, font=15, bg='white', bd=1, command=switchToEncrypt)
    genButton.pack(padx=20, pady=20, side='left')

    scanButton = Button(navFrame, text='Decode Morse Code', width=25, height=2, font=15, bg='white', bd=1, command=switchToDecrypt)
    scanButton.pack(padx=20, pady=20, side='right')

    message = StringVar()
    message.set('')
    message.trace_add('write', toggleButton)

    reg = root.register(callback)

    messageFrame = Frame(root, width=600, height=100, bg="white")

    messageLabel = Label(messageFrame, font=('times', 14), bg='white', fg='black', width=20, anchor='w', text='Enter text to be encoded')
    messageLabel.pack(padx=20, pady=20, side='left')

    messageEntry = Entry(messageFrame, bd=1, bg='white', width=60, font=('times', 14), justify='center', textvariable=message)
    messageEntry.focus_set()
    # messageEntry.config(validate ="key", validatecommand =(reg, '% P'), invalidcommand=lambda: print(message.get()))
    messageEntry.pack(padx=20, pady=20, side='right')

    buttonFrame = Frame(root, width=600, height=100, bg="white")

    submitButton = Button(buttonFrame, width=20, height=2, font=15, bg='white', state='disabled', bd=1)
    submitButton.pack(padx=20, pady=20, side='left')

    resetButton = Button(buttonFrame, text='Reset', width=10, height=2, font=15, bg='white', bd=1, state='disabled', command=lambda: reset(messageEntry))
    resetButton.pack(padx=20, pady=20, side='right')

    displayLabel = Label(root, font=('times', 34), wraplength=700)

    root.mainloop()