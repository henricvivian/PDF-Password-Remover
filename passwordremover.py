import PyPDF2
import tkinter as tk
from tkinter import filedialog

class PDFPasswordRemover:
    def __init__(self, master):
        self.master = master
        master.title('PDF Password Remover')

        # Create widgets
        self.label = tk.Label(master, text='Select an encrypted PDF file:')
        self.label.pack()

        self.button = tk.Button(master, text='Browse', command=self.browse_file)
        self.button.pack()

        self.password_label = tk.Label(master, text='Enter the password:')
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack()

        self.submit_button = tk.Button(master, text='Remove Password', command=self.remove_password)
        self.submit_button.pack()

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('PDF files', '*.pdf'),))
        self.label.config(text='Selected file: ' + self.file_path)

    def remove_password(self):
        with open(self.file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            if pdf_reader.isEncrypted:
                pdf_reader.decrypt(self.password_entry.get())
                pdf_writer = PyPDF2.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    pdf_writer.addPage(page)
                with open('unlocked_file.pdf', 'wb') as unlocked_file:
                    pdf_writer.write(unlocked_file)
                self.label.config(text='Password removed and PDF file saved as unlocked_file.pdf')
            else:
                self.label.config(text='PDF file is not password protected')

root = tk.Tk()
pdf_password_remover = PDFPasswordRemover(root)
root.mainloop()
