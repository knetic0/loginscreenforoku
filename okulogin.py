from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msj
import webbrowser
from tkinter import simpledialog

gui = Tk()
gui.title('Deneme')
gui.geometry('900x350')

gui.configure(background='')
#temel-basic kavramlar
'''
def outMessage():
    msj.showinfo(title='Basarili!',message='Giris Basarili!')

kAdi = Label(gui, text='Kullanici adiniz', fg='black')
kAdi.grid()

kAdiEntry = StringVar()
soyAdi = StringVar()
ad = Entry(gui,text='Adiniz',textvariable=kAdiEntry)
ad.grid()

sAdi = Label(gui, text='Soyadinizi Giriniz', fg='black')
sAdi.grid()

inSoyAdi = Entry(gui,text='Soyadiniz',textvariable=soyAdi)
inSoyAdi.grid(padx=180,pady=5)

if len(kAdiEntry) > 1 and len(soyAdi) > 1:

    login = Button(gui,text='Giris Yap', bg='black',fg='white',command=outMessage)
    login.grid()
else:
    msj.showinfo(gui,title='Basarisiz',message='Kullanici adinizi veya sifrenizi giriniz!')
    
#temel-basic kavramlar


#dosya yolu
foldername = ''
def folderr():
    global foldername
    foldername = filedialog.askdirectory()

    if len(foldername) > 1:

        folder.configure(text='Dosya yolunu degistirmek icin basiniz!',command=folderr)
        cikti.config(text=foldername,fg='green')

folder = Button(gui, text='Dosya yolunu seciniz ',command=folderr)
folder.grid()
cikti = Label(gui, fg='green',text='{}'.format(foldername))  # pack() kullanilirsa .grid kullanilamaz. Pack ise ortalamayi saglar.
cikti.grid()

#dosya yolu


#fotograf ekleme

foto = PhotoImage(file='mermivetahtamomentum.png')
Button(gui,image=foto,command=None).pack(pady=10)


#fotograf ekleme
'''
bg = PhotoImage(file="download.png")

# Show image using label
label1 = Label(gui, image=bg)
label1.place(x=0, y=0)


#fotograf
#photo = PhotoImage(file='download.png')
#Label(gui,image=photo,text='ogrNo',command=None).pack()

def login():
    Label(gui,text='Ogrenci Numaranizi Giriniz:',font=('Arial', 16)).grid(row=3, column=0,pady=15)
    no = StringVar()
    ogrNo = Entry(gui, text='Ogrenci Numaraniz',textvariable=no,font=('Arial', 20)).grid(row=3, column=2, sticky="ew")

    Label(gui,text='Sifrenizi Giriniz:',font=('Arial', 16)).grid(row=4, column=0,pady=10)
    passw = StringVar()
    password = Entry(gui,text='Sifreniz',show='*',textvariable=passw,font=('Arial', 20)).grid(row=4, column=2, sticky="ew")

    Label(gui,text='Dogrulama : 2 + 2 = ?', font=('Arial',16)).grid(row=5, column=0,pady=10)
    patch = StringVar()
    patchV = Entry(gui,text='Sonuc',textvariable=patch,font=('Arial',12)).grid(row=5, column=2, sticky="ew")

    Button(gui,text='Giris Yap',bg='white',fg='black',font=('Arial',18),command=success).grid(row=6, column=1,pady=10)
    Button(gui,text='Kapat',bg='white',font=('Arital',18),command=quit).grid(row=6, column=2,pady=10)

    Label(gui,text='E-Devlet',font=('Arial',16)).grid(row=7,column=0)
    Button(gui,text='E-Devlet Ile Giris Yap',font=('Arial',10),command=register).grid(row=8,column=0,pady=10)
    gui.wm_attributes("-transparentcolor", '')

def success():
    msj.showinfo(title='Basarili',message='Giris Basarili!')
    webbrowser.open_new_tab('https://osmaniye.edu.tr/')

def quit():
    msj.showinfo(title='Cikis',message='Cikis Basarili!')
    gui.destroy()

def register():
    msj.showinfo(title='Kayit', message='Yonlendiriliyorsunuz!')
    webbrowser.open_new_tab('https://obs.osmaniye.edu.tr/oibs/ogrenci/login.aspx')

login()

gui.mainloop()