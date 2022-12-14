import gtts
import PyPDF2
from tkinter import Tk, filedialog, StringVar, Label, Button, Checkbutton

def browse():
    global pdfReader
    file = filedialog.askopenfilename(parent=root, title='Select a book', filetypes=(('PDF Files', '*.pdf'), ('Text Files', '*.txt'), ('All Files', '*.*')))

    pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))
    pathlabel.config(text=file)

def save():
    pass

if __name__ == '__main__':
    width = 800
    height = 500

    root = Tk()
    root.geometry(f'{width}x{height}')
    root.configure(bg='white')
    root.title('Audiobook')
    root.resizable(0, 0)
    root.eval('tk::PlaceWindow . center')

    m = StringVar()
    f = StringVar()

    Label(root, text="AUDIOBOOK",font="Arial 15",bg='green').pack()
    pathlabel = Label(root)
    pathlabel.pack()

    Button(root,text="Browse a File",command=browse).pack()
    Button(root,text="Create and Save the Audio File ",command=save).pack()

    Checkbutton(root,text="Male Voice",onvalue=0,offvalue=10,variable=m).pack()
    Checkbutton(root,text="Female Voice",onvalue=1,offvalue=10,variable=f).pack()

    root.mainloop()