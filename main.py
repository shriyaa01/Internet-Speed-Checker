from tkinter import *
import speedtest


def test():
    s = speedtest.Speedtest()
    s.get_servers()

    # Download speed
    down = round(s.download() / (10 ** 6), 3)
    downld = str(down) + " Mbps"
    lab_download.config(text=downld)

    # Upload speed
    up = round(s.upload() / (10 ** 6), 3)
    upld = str(up) + " Mbps"
    lab_upload.config(text=upld)


# Create the GUI window
sp = Tk()
sp.title("Check Your Internet Speed")
sp.geometry("500x550")
sp.config(background='black')

# Labels
lab = Label(sp, text="Your Internet Speed", font=("Times New Roman", 20, "bold"), background="black", fg="white")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Downloading Speed", font=("Times New Roman", 18), background="black", fg="white")
lab.place(x=60, y=130, height=50, width=380)

lab_download = Label(sp, text="00", font=("Times New Roman", 18), background="black", fg="white")
lab_download.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Uploading Speed", font=("Times New Roman", 18), background="black", fg="white")
lab.place(x=60, y=290, height=50, width=380)

lab_upload = Label(sp, text="00", font=("Times New Roman", 18), background="black", fg="white")
lab_upload.place(x=60, y=360, height=50, width=380)

# Button to check speed
button = Button(sp, text="Check Speed", font=("Times New Roman", 16), relief=RAISED, background="red", command=test)
button.place(x=60, y=460, height=50, width=380)

# Start the GUI application
sp.mainloop()
