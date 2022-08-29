from __future__ import unicode_literals
import youtube_dl
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

class Downloader(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=310, height=200)

        self.options = IntVar()
        self.options.set(value=0)

        self.save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        os.chdir(self.save_path)
        self.download_page()


    def download_page(self):
        self.url_label = Label(text="Video / URL:")
        self.url_label.grid(column=1, row=0, pady=10)
        self.url_entry = Entry(width=48)
        self.url_entry.grid(column=0, row=1, columnspan=3, padx=5, pady=5)
        self.location_label = Label(text="Location:")
        self.location_label.grid(column=1, row=3)
        self.location_entry = Entry(width=35)
        self.location_entry.grid(column=0, row=4, columnspan=2, padx=5, pady=10)
        self.location_entry.insert(0, str(self.save_path))
        self.location_button = Button(text="Set", command=self.set_path)
        self.location_button.grid(column=2, row=4)
        self.download_button = Button(text="Download", command=self.download)
        self.download_button.grid(column=1, row=5, pady=15)

    def download(self):
        url = self.url_entry.get()
        ydl = youtube_dl.YoutubeDL(self.get_opts())
        ydl.download([url])
        messagebox.showinfo("HECHO",
                            "DESCARGADO\n")

    def set_path(self):
        self.path = fd.askdirectory()
        self.location_entry.delete(0, END)
        self.location_entry.insert(0, str(self.path))

    def get_opts(self):
        save = self.location_entry.get()
        filetype = self.options.get()
        if filetype == 0:
            opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                }],
                'extractaudio': True,
                'outtmpl': save + '/%(title)s.%(ext)s',
                'noplaylist': True
            }
            return opts

if __name__ == "__main__":
    root = Tk()
    root.title("Youtube Downloader")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    icon = PhotoImage(file='icon.png')
    root.iconphoto(False, icon)
    root.resizable(False, False)
    Downloader(root)
    root.mainloop()
