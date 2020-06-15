from tkinter import Tk, Button, Label, StringVar,Entry
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube


window = Tk()
window.title("Youtube Video Downloader")
window.configure(background = "white")
window.geometry("550x100")
window.resizable(width="False", height="False")


def open_folder():
    global directory
    directory = askdirectory()
    print(directory)


def download():
    if len(link.get())==0:
        messagebox.showerror("Link Empty", "Link can not be empty")
    else:
        YouTube(link.get()).streams.first().download(directory)
        messagebox.showinfo("Complete", "Video downloaded successfully")
        link_entry.delete(0, 'end')


lbl = Label(window, text="Enter Link", bg="red", fg="white", font='Helvetica 15')
lbl.grid(column = 0, row =1, padx=10, pady=10)

link = StringVar()
link_entry = Entry(window, textvariable = link, width = 50, borderwidth=4)
link_entry.grid(row=1, column=1)

btn_dir = Button(window, text="Select folder", width = 15, command=open_folder)
btn_dir.grid(row=1, column=2)

btn_download = Button(window, text = "Download", width = 15, command = download)
btn_download.grid(row=2, column=1)



window.mainloop()
