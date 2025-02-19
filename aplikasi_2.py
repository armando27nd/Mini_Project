import random
import tkinter as tk
import customtkinter # type: ignore
from PIL import ImageTk, Image # type: ignore
from tkinter import messagebox
from tkinter import ttk
import time

customtkinter.set_appearance_mode('light')#buat default setting ke tema gelap, bisa diubah ke system tpi lebih bagus di mode dark 
customtkinter.set_default_color_theme('blue')#buat tema warna default yang dipake 


app = customtkinter.CTk()
# bikin variable data

database ={'nama':'',
            'skor1':'',
            'skor2':'',
            'skor3':''}
#variable pake typedata dict buat simpan user dan pass akun



username = customtkinter.StringVar()#buat narik data dari entry user


app.geometry('870x430')#ukuran window program
app.resizable(False,False)#biar ukuran window gabisa diubah(mager atur responsifnya)
app.overrideredirect(1)

#import gambar dari folder icon

utama = ImageTk.PhotoImage(Image.open('icon/utama.png').resize(size=([870,480])))
bgkredit = ImageTk.PhotoImage(Image.open('icon/bgkredit.png').resize(size=([870,430])))
nanyak = ImageTk.PhotoImage(Image.open('icon/nanyak.png').resize(size=([870,450])))
masuk = ImageTk.PhotoImage(Image.open('icon/masukk.png').resize(size=([30,30])))
credit = ImageTk.PhotoImage(Image.open('icon/credit.png').resize(size=([30,30])))
statis = ImageTk.PhotoImage(Image.open('icon/stat.png').resize(size=([30,30])))
lagi = ImageTk.PhotoImage(Image.open('icon/retry.png').resize(size=([30,30])))
udah = ImageTk.PhotoImage(Image.open('icon/udah.png').resize(size=([30,30])))
cek = ImageTk.PhotoImage(Image.open('icon/cek.png').resize(size=([50,30])))
play = ImageTk.PhotoImage(Image.open('icon/mulai_menu.png').resize(size=([70,70])))
daftar = ImageTk.PhotoImage(Image.open('icon/daftar.png').resize(size=([100,30])))
teka = ImageTk.PhotoImage(Image.open('icon/susun huruf.png').resize(size=([180,100])))
emteka = ImageTk.PhotoImage(Image.open('icon/kuis emteka.png').resize(size=([180,100])))
uji = ImageTk.PhotoImage(Image.open('icon/uji_emosi.png').resize(size=([180,100])))
kedua = ImageTk.PhotoImage(Image.open('icon/kedua.png').resize(size=([870,480])))
menu = ImageTk.PhotoImage(Image.open('icon/menu.png').resize(size=([870,480])))
Tg = ImageTk.PhotoImage(Image.open('icon/latar_game.png').resize(size=([870,480])))

#variabel warna
kuning = '#ff8212'
oren = '#db4b00'
oren_samar = '#dd7944'
abu = '#2b302e'
putih = '#ffffff'
ijo_papan = '#49795d'
putih_kebiruan = '#d1d8d2'
biru_muda = '#8dc6d5'

#variable jenis font dan ukuran
font1 = ('Century Gothic bold',20)
font2 = ('Comicbon', 40)
font3 = ('Comicbon', 18)

def keluar():
    app.destroy()

def statistik():
    l1.destroy()
    l5 = customtkinter.CTkLabel(text= '',master=app, image=utama)
    l5.pack()
    def kembali():
        l5.destroy()
        tampilan()
    end = customtkinter.CTkButton(master = l5, width=26, height=26, text='X', fg_color=kuning, text_color=oren, command=kembali)
    end.place(x=20, y=20)
    label = customtkinter.CTkLabel(text= '',master=l5, fg_color=putih_kebiruan, width=510, height=440)
    label.place(relx= 0.45)
    label2 = customtkinter.CTkLabel(text= '',master=label, fg_color=putih_kebiruan, text_color='#000000')
    label2.place(relx= 0.1, rely=0.1)
    nama = database['nama']
    game1 = database['skor1']
    game2 = database['skor2']
    game3 = database['skor3']
    a=0
    b = 'statistik'+ nama +'\nskor game emteka:'+game2+'\nskor game susun huruf :'+game1+'\nskor game uji emosi:'+ game3
    
    label2.configure(text=b, justify = tk.LEFT)
    
    


def tampilan(): 
    global l1,user
    l1 = customtkinter.CTkLabel(text= '',master=app, image=utama)
    l1.pack()
    versi = customtkinter.CTkLabel(text= 'versi 1.1',master=l1,font=('arial bold-italic', 12), text_color='white', fg_color='#a3d1dd')
    versi.place(relx=0.93,rely=0.03)

    
    user = customtkinter.CTkEntry(master=l1, width=300,placeholder_text='Nama lu cok', state=tk.NORMAL,text_color='black',fg_color='light grey', corner_radius=10,border_color=oren, textvariable=username)#tulisannya hilang
    user.place(x=640, y= 270, anchor = tk.CENTER)

    end = customtkinter.CTkButton(master = l1, width=26, height=26, text='X', corner_radius=0, fg_color=kuning, text_color=oren, command=keluar)
    end.place(x=20, y=20)
    stat = customtkinter.CTkButton(master = l1, width=70, height=45, text='', image=statis, anchor='center', corner_radius=0, fg_color=kuning, border_width=2, border_color=oren, command=statistik )
    stat.place(x=490, y=300)
    play = customtkinter.CTkButton(master = l1, width=120, height=45, text='', image=masuk,anchor='center', corner_radius=0, fg_color=kuning, border_width=2, border_color=oren, command=loby )
    play.place(x=580, y=300)
    cred = customtkinter.CTkButton(master = l1, width=70, height=45, text='',image=credit,anchor='center', corner_radius=0, fg_color=kuning, border_width=2, border_color=oren , command=kredit)
    cred.place(x=720, y=300)



    app.mainloop()

def asal():#dah kelar
    global l3
    def kembali():
        
        l3.destroy()
        tampilan()

    l2.destroy()
    l3 = customtkinter.CTkLabel(text='',master=app, image=menu)
    l3.pack()
    user = username.get()
    
    text0 = customtkinter.CTkLabel(master = l3, text='',height=26, width=300,fg_color='grey')
    text0.place(x=23,y=23)
    text = customtkinter.CTkLabel(master = l3, text='',height=26, width=300,fg_color=putih_kebiruan)
    text.place(x=20,y=20)
    end = customtkinter.CTkButton(master = text, width=26, height=26, text='X', fg_color=kuning, text_color=oren, command=kembali)
    end.place(relx=0)
    text = customtkinter.CTkLabel(master = text, text=f'Welkom {user}',text_color=oren, font = font1)
    text.place(relx=0.1)
    play11 = customtkinter.CTkLabel(master = l3, image=teka, text='')
    play11.place(x=680,y=210, anchor= tk.CENTER)
    play1 = customtkinter.CTkButton(master = l3, width=70, height=70, text='',anchor='center', corner_radius=0,image=masuk, fg_color=kuning, border_width=3, border_color=oren, command=Game1 )
    play1.place(x=570,y=210, anchor= tk.CENTER)
    play12 = customtkinter.CTkLabel(master = l3, image=emteka, text='')
    play12.place(x=680,y=100, anchor= tk.CENTER)
    play2 = customtkinter.CTkButton(master = l3, width=70, height=70, text='',anchor='center', corner_radius=0,image=masuk, fg_color=kuning, border_width=3, border_color=oren, command=Game2 )
    play2.place(x=570,y=100, anchor= tk.CENTER)
    play13 = customtkinter.CTkLabel(master = l3, image=uji, text='')
    play13.place(x=680,y=320, anchor= tk.CENTER)
    play3 = customtkinter.CTkButton(master = l3, width=70, height=70, text='',anchor='center', corner_radius=0,image=masuk, fg_color=kuning, border_width=3, border_color=oren, command=Game3 )
    play3.place(x=570,y=320, anchor= tk.CENTER)
    
def loading():#dah kelar
    global l2
    l1.destroy()
    l2 = customtkinter.CTkLabel( text='loading...',font=font1,text_color=oren,master=app, image=kedua)
    l2.pack()
    
    Proses = ttk.Style()
    Proses.theme_use('clam')
    Proses.configure('red.Horizontal.TProgressbar', background = '#108cff')

    proses =ttk.Progressbar(l2, orient='horizontal',length=400,style='red.Horizontal.TProgressbar', mode='determinate')
    proses.place(relx=0.5,rely=0.7, anchor=tk.CENTER)

    x=0
    for i in range(100):
        proses['value'] = x
        l1.update_idletasks() 
        time.sleep(0.1)
        x+=5
    
    asal()

def loby():#dah kelar
    if user.get() == '':    
        messagebox.showinfo('inpo','diisi cok')
        user.configure(border_color='red')
    
    else:
        database['nama'] = username.get()
        user.configure(border_color='green')
        time.sleep(0.3)
        loading()

def kredit():
    l1.destroy()
    bg_kredit = customtkinter.CTkLabel( text='',master=app, image=bgkredit)
    bg_kredit.pack()

    def kembali():
        bg_kredit.destroy()
        tampilan()
    end = customtkinter.CTkButton(master = bg_kredit, width=26, height=26, text='X', fg_color='red', text_color=putih, command=kembali)
    end.place(x=20, y=20)

class Game1(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        l3.destroy()
        self.selff = customtkinter.CTkLabel(app,width=600, height=440,text='', image=Tg)
        self.selff.pack()
        
        self.kata1 = ['rusa', 'kucing', 'kambing', 'kuda', 'babi', 'anjing', 'kelinci', 'monyet', 'kudanil', 'ayam', 'singa']
        self.skor = 0

        
        def kembali():
            time.sleep(0.2)
            self.selff.destroy()
            asal()
        
        end = customtkinter.CTkButton(self.selff, width=26, height=26, text='X', corner_radius=0, fg_color=kuning, text_color=oren, command=kembali)
        end.place(x=20, y=20)

        self.soal = customtkinter.CTkLabel(self.selff, text="Tebak nama hewan: ", font=font2,text_color='light grey', fg_color=ijo_papan)
        self.soal.place(x=435,y=100, anchor = tk.CENTER)

        self.jawaban = customtkinter.CTkEntry(self.selff, font=font2, fg_color=ijo_papan,justify= tk.CENTER,text_color='light grey', height=60, width=360, bg_color=ijo_papan, border_width=0, border_color=ijo_papan)
        self.jawaban.place(x=480,y=230, anchor = tk.CENTER)
        
        self.text_jawab = customtkinter.CTkLabel(self.selff, text="jawab :", font=font2,text_color='light grey', fg_color=ijo_papan, height=60)
        self.text_jawab.place(x=220,y=225, anchor = tk.CENTER)
        
        self.enter = customtkinter.CTkButton(self.selff,image=cek,width= 70,height=60, fg_color=ijo_papan, text='', command=self.cek_hasil)
        self.enter.place(x=680,y=230, anchor = tk.CENTER)
          
        
        self.jalan = 1
        self.play_game()
    
    def tanya(self):#masih pr
        def udahan():
            time.sleep(0.3)
            self.bgtanya.destroy()
            asal()
        def lagih():
            time.sleep(0.3)
            self.bgtanya.destroy()
            Game1()
        
    
        self.bgtanya = customtkinter.CTkLabel(app,text='', image=nanyak)
        self.bgtanya.pack()
        self.text_skor = customtkinter.CTkLabel(self.bgtanya,text='USAI SUDAH\nSkor: ' + str(self.skor),text_color='light grey', image=nanyak, font=font2)
        self.text_skor.place(x=435, y=220, anchor=tk.CENTER)
        self.udah = customtkinter.CTkButton(master = self.bgtanya, width=100, height=40,  text='', image=udah, anchor='center',  text_color=oren, fg_color=kuning, border_width=2, border_color=oren, command=udahan )
        self.udah.place(x=350,y=340, anchor= tk.CENTER)
        self.lagi = customtkinter.CTkButton(master = self.bgtanya, width=100, height=40,  text='', image=lagi, anchor='center',  text_color=oren, fg_color=kuning, border_width=2, border_color=oren, command=lagih )
        self.lagi.place(x=520,y=340, anchor= tk.CENTER)
        
    def play_game(self):
        
        if self.jalan <= 5:
            self.soal.configure(text="Tebak nama hewan: ")
            self.jawaban.delete(0, tk.END)
            time.sleep(0.3)
            self.display_soal()
        else:
            #messagebox.showinfo("Selesai", "Game Selesai!\nSkor Anda: " + str(self.skor))
            database['skor1'] = str(self.skor)
            time.sleep(0.3)
            self.selff.destroy()
            self.tanya()

    def display_soal(self):
        kata2 = random.choice(self.kata1).lower()
        self.soal.configure(text="Tebak nama hewan: " + self.acak_acak(kata2))
        self.jwb_benar = kata2
    
    def acak_acak(self, word):
        return ''.join(random.sample(word, len(word))).lower()
    
    def cek_hasil(self):
        tebak = self.jawaban.get().lower()
        
        if tebak == self.jwb_benar:
            #messagebox.showinfo("Jawaban Benar", "Anda benar!")
            self.skor += 1
        else:
            pass
            #messagebox.showinfo("Jawaban Salah", "Anda salah!")
        
        self.jalan += 1
        self.play_game()

class Game2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        l3.destroy()
        self.selff = customtkinter.CTkLabel(app,width=600, height=440,text='', image=Tg)
        self.selff.pack()  

        def kembali():
            time.sleep(0.2)
            self.selff.destroy()
            asal() 
        end = customtkinter.CTkButton(self.selff, width=26, height=26, text='X', corner_radius=0, fg_color=kuning, text_color=oren, command=kembali)
        end.place(x=20, y=20)

        self.soal = customtkinter.CTkLabel(self.selff, text="Hitung : ", font=font2,text_color='light grey', fg_color=ijo_papan)
        self.soal.place(x=435,y=100, anchor = tk.CENTER)

        self.jawaban = customtkinter.CTkEntry(self.selff, font=font2,text_color='light grey', fg_color=ijo_papan,justify= tk.CENTER, height=60, width=360, bg_color=ijo_papan, border_width=0, border_color=ijo_papan)
        self.jawaban.place(x=480,y=230, anchor = tk.CENTER)
        
        self.text_jawab = customtkinter.CTkLabel(self.selff, text="jawab :", font=font2,text_color='light grey', fg_color=ijo_papan, height=60)
        self.text_jawab.place(x=220,y=225, anchor = tk.CENTER)
        
        self.enter = customtkinter.CTkButton(self.selff,image=cek,width= 70,height=60, fg_color=ijo_papan, text='', command=self.cek_hasil)
        self.enter.place(x=680,y=230, anchor = tk.CENTER)

        self.skor = 0
        self.jalan = 1
        self.play_game()
        
    def tanya(self):
        def udahan():
            time.sleep(0.3)
            self.bgtanya.destroy()
            asal()
        def lagih():
            time.sleep(0.3)
            self.bgtanya.destroy()
            Game2()
    

        self.bgtanya = customtkinter.CTkLabel(app,text='', image=nanyak)
        self.bgtanya.pack()
        self.text_skor = customtkinter.CTkLabel(self.bgtanya,text='USAI SUDAH\nSkor: ' + str(self.skor),text_color='light grey', image=nanyak, font=font2)
        self.text_skor.place(x=435, y=220, anchor=tk.CENTER)
        self.udah = customtkinter.CTkButton(master = self.bgtanya, width=100, height=40,  text='', image=udah, anchor='center',  text_color=oren, fg_color=kuning, border_width=2, border_color=oren, command=udahan )
        self.udah.place(x=350,y=340, anchor= tk.CENTER)
        self.lagi = customtkinter.CTkButton(master = self.bgtanya, width=100, height=40,  text='', image=lagi, anchor='center',  text_color=oren, fg_color=kuning, border_width=2, border_color=oren, command=lagih )
        self.lagi.place(x=520,y=340, anchor= tk.CENTER)
        
    def play_game(self):
        
        if self.jalan <= 5:
            self.soal.configure(text="Hitung : ")
            self.jawaban.delete(0, tk.END)
            time.sleep(0.5)
            self.display_soal()
        else:
            database['skor2'] =str(self.skor)
            #messagebox.showinfo("Selesai", "Game Selesai!\nSkor Anda: " + str(self.skor))
            time.sleep(0.5)
            self.selff.destroy()
            self.tanya()

    def display_soal(self):
        self.no1 = random.randint(1, 50)
        self.no2 = random.randint(1, 50)
        self.operator = random.choice(["+", "-", "*", "/"])

        
        self.soal.configure(text="Hitung : "+ str(self.no1) + " " + self.operator + " " + str(self.no2))

    def cek_hasil(self):
        self.soall = str(self.no1) + " " + self.operator + " " + str(self.no2)
        self.tebak = self.jawaban.get()
        self.periksa = eval(self.soall)
        self.periksa2 = round(self.periksa,2)
        try:
            if float(self.tebak) == self.periksa2:
                self.skor += 1
            else:
                pass
        except:
            pass
        self.jalan += 1
        self.play_game()

class Game3(customtkinter.CTk):
    def __init__(self):
        
        self.skor = 0
        self.ssoal = 0

        self.soal = [
        {
            "soal": "Berapa kaki pada hewan kaki seribu?",
            "pilihan": ["1000", "1001", "1010", "2100"],
            "jawaban": 0
        },
        {
            "soal": "Siapakah penemu kunci motor yang hilang di rumah?",
            "pilihan": ["Bapak", "Ibu", "Adek", "Nikola Tesla"],
            "jawaban": 1
        },
        {
            "soal": "Tebak apa saja, hayo?",
            "pilihan": ["7", "8", "9", "10"],
            "jawaban": 1
        }]

        l3.destroy()
        self.selff = customtkinter.CTkLabel(app,width=600, height=440,text='', image=Tg)
        self.selff.pack() 
        self.soal_label = customtkinter.CTkLabel(self.selff, text="", font=font3, text_color='light grey',fg_color=ijo_papan )
        self.soal_label.place(relx=0.2, rely=0.2)
        def kembali():
            time.sleep(0.2)
            self.selff.destroy()
            asal() 
        end = customtkinter.CTkButton(self.selff, width=26, height=26, text='X', corner_radius=0, fg_color=kuning, text_color=oren, command=kembali)
        end.place(x=20, y=20)

        self.buttons = []
        self.tombol_jawaban()
        self.next_soal()
    
    def tanya(self):
        def udahan():
            time.sleep(0.3)
            self.bgtanya.destroy()
            asal()
        def lagih():
            time.sleep(0.3)
            self.bgtanya.destroy()
            Game2()
    

        self.bgtanya = customtkinter.CTkLabel(app,text='', image=nanyak)
        self.bgtanya.pack()
        self.text_skor = customtkinter.CTkLabel(self.bgtanya,text='USAI SUDAH\nSkor: ' + str(self.skor),text_color='light grey', image=nanyak, font=font2)
        self.text_skor.place(x=435, y=220, anchor=tk.CENTER)
        self.udah = customtkinter.CTkButton(master = self.bgtanya, width=100, height=40,  text='', image=udah, anchor='center',  text_color=oren, fg_color=kuning, border_width=2, border_color=oren, command=udahan )
        self.udah.place(x=350,y=340, anchor= tk.CENTER)
        self.lagi = customtkinter.CTkButton(master = self.bgtanya, width=100, height=40,  text='', image=lagi, anchor='center',  text_color=oren, fg_color=kuning, border_width=2, border_color=oren, command=lagih )
        self.lagi.place(x=520,y=340, anchor= tk.CENTER)
        
    def tombol_jawaban(self):
        for i in range(4):
            a = f'0.{3+i}'
            self.button = customtkinter.CTkButton(self.selff,font=font3,fg_color=ijo_papan,text_color='light grey',border_color='light grey',border_width=2, text="", command=lambda idx=i: self.cek_jawaban(idx))#idk=index, buat variabel biar gampang diinget
            self.button.place(relx=0.2, rely=float(a))
            self.buttons.append(self.button)

    def load_soal(self):
        self.soal_label.configure(text=self.soal[self.ssoal]["soal"])
        for i, pilihan in enumerate(self.soal[self.ssoal]["pilihan"]):
            self.buttons[i].configure(text=pilihan)

    def cek_jawaban(self, jawaban):
        if jawaban == self.soal[self.ssoal]["jawaban"]:
            self.skor += 1
        self.ssoal += 1
        if self.ssoal < len(self.soal):
            self.load_soal()
        else:
            
            time.sleep(0.5)
            self.selff.destroy()
            self.tanya()

    def next_soal(self):
        if self.ssoal < len(self.soal):
            self.load_soal()
        else:
            database['skor3'] = str(self.skor)
            time.sleep(0.5)
            self.selff.destroy()
            self.tanya()
            


tampilan()