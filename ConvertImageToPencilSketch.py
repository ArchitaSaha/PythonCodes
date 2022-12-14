import cv2
from tkinter import Tk, filedialog, Frame, Label, Button
from PIL import ImageTk, Image

def browse():
    file = filedialog.askopenfilename(parent=root, title='Select an image', filetypes=(('JPEG Images', '*.jpeg'), ('PNG Images', '*.png'), ('All Files', '*.*')))
    # return file
    
    if len(file) > 0:
        pencilImage = convertImageToPencilSketch(file)
        displayImage(pencilImage, frame, label, file)

def convertImageToPencilSketch(file):
    image = cv2.imread(file)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred_image
    pencil_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return pencil_image

def displayImage(pencil_image, frame, label, file):
    final_image = Image.fromarray(pencil_image)

    fixed_width = 480 if final_image.width < final_image.height else 1024

    final_image = final_image.resize((fixed_width, final_image.height * fixed_width // final_image.width), Image.Resampling.NEAREST)
    final_image.save(file.split('.')[0] + '_pencil.png')

    root.geometry(f'{final_image.width + 20}x{final_image.height + 120}')

    frame.pack()
    image1 = ImageTk.PhotoImage(final_image)
    label.configure(image=image1)
    label.image = image1
    label.pack()

    root.eval('tk::PlaceWindow . center')

def reset():
    frame.pack_forget()
    root.geometry(f'{width}x{height}')
    root.eval('tk::PlaceWindow . center')

if __name__ == '__main__':
    width = 800
    height = 150

    root = Tk()
    root.geometry(f'{width}x{height}')
    root.configure(bg='white')
    root.title('Pencil Image Converter')
    root.resizable(0, 0)
    root.eval('tk::PlaceWindow . center')

    buttonFrame = Frame(root, width=600, height=100, bg="white")
    buttonFrame.pack(padx=20, anchor='center')

    browseButton = Button(buttonFrame, text='Browse Images', width=10, height=2, font=15, bg='white', bd=1, command=browse)
    browseButton.pack(padx=20, pady=20, side='left')

    resetButton = Button(buttonFrame, text='Reset', width=10, height=2, font=15, bg='white', bd=1, command=reset)
    resetButton.pack(padx=20, pady=20, side='right')

    frame = Frame(root, width=300, height=300, bg="pink")
    label = Label(frame)

    root.mainloop()