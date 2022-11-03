from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
from gtts import gTTS

#constants
BG_COLOR = "#3F3B6C"
COLOR_FONT = "#A3C7D6"
FONT = ("Helvatica", 16)

pdf_text = ""


def open_file():
    global pdf_text
    #file explorer to choose file to open
    file = filedialog.askopenfilename(filetype=[("PDF", "*.pdf")])
    #read opened file
    reader = PdfReader(file)
    #show number of pafes
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    page_label.config(text=f"Number of Pages: {number_of_pages}")
    #loop through pages and added text in global variable
    for n in range(number_of_pages):
        page = reader.pages[n]
        pdf_text += page.extract_text()
    print(pdf_text)


def save():
    global pdf_text
    # Convert to Audiobook
    save_types = [('MP3 Files', '*.mp3')]
    save_folder = filedialog.asksaveasfilename(title="Where do you want to save the Audiobook?",
                                               filetypes=save_types, defaultextension=save_types
                                               )
    # text to convert and save
    tts = gTTS(pdf_text)
    tts.save(save_folder)


window = Tk()
window.title("Convert PDF to AUDIOBOOK")
window.config(padx=50, pady=50, bg=BG_COLOR)

#labels
welcome_label = Label(text="Convert your PDF to AUDIOBOOK", font=FONT, fg=COLOR_FONT, bg=BG_COLOR)
welcome_label.grid(column=0, row=0, columnspan=2, pady=50)

page_label = Label(text="Number of Pages: Not Loaded", fg=COLOR_FONT, bg=BG_COLOR)
page_label.grid(column=0, row=3, pady=20, padx=80, columnspan=2)

#buttons
open_button = Button(text="OPEN", command=open_file)
open_button.grid(column=0, row=2, pady=20)

convert_button = Button(text="Convert and Save", command=save)
convert_button.grid(column=1, row=2, pady=20)

window.mainloop()

