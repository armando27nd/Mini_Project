#kumpulan modul dan library yang dipake nantinya
import os
import random
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import time

customtkinter.set_appearance_mode('dark')#buat default setting ke tema gelap, bisa diubah ke system tpi lebih bagus di mode dark 
customtkinter.set_default_color_theme('green')#buat tema warna default yang dipake 


app = customtkinter.CTk()
# bikin variable data 
database ={'admin':'admin'}#variable pake typedata dict buat simpan user dan pass akun
username = customtkinter.StringVar()#buat narik data dari entry user
password = customtkinter.StringVar()#buat narik data dari entry password


app.geometry('600x440')#ukuran window program
app.resizable(False,False)#biar ukuran window gabisa diubah(mager atur responsifnya)
app.overrideredirect(1)
#app.title('Game')#buat judul windownya

#import gambar dari folder icon
background1 = ImageTk.PhotoImage(Image.open('icon/bg.jpg').resize(size=([600,700])))
background2 = ImageTk.PhotoImage(Image.open('icon/latar_polos.jpg').resize(size=([600,440])))
gambar1 = ImageTk.PhotoImage(Image.open('icon/suhu.jpg').resize(size=([150,200])))
gambar2 = ImageTk.PhotoImage(Image.open('icon/mtk.jpg').resize(size=([150,200])))
gambar3 = ImageTk.PhotoImage(Image.open('icon/uk.jpg').resize(size=([150,200])))
gambar4 = ImageTk.PhotoImage(Image.open('icon/loby.jpg').resize(size=([600,440])))

#variabel warna
ungu = '#6b13c7'
ijo_terang = '#9fdbc6'
ijo_gelap = '#219a71'
abu = '#2b302e'
putih = '#ffffff'
tengah = '#396f8c'

#variable jenis font dan ukuran
font1 = ('Century Gothic bold',20)
font2 = ('Clap Hand', 40)
font3 = ('Arciform Sans', 72)

def keluar():
    app.destroy()
    os.system('cls')

def tampilan(): 
    global l1,frame
    l1 = customtkinter.CTkLabel(master=app, image=background1)
    l1.pack()

    frame = customtkinter.CTkLabel(master = l1, width=320, height=360, corner_radius=30)
    frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

    head = customtkinter.CTkLabel(master = frame, text = 'SELAMAT DATANG', font = ('Century Gothic bold',20), text_color='#00ffc1')
    head.place(x=75, y= 50)

    user = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='nama lu',textvariable=username)#tulisannya hilang
    #user._activate_placeholder()
    user.place(x=50, y= 110)

    sandi = customtkinter.CTkEntry(master=frame, width=220,textvariable=password,placeholder_text='password lu',show='•')#tulisannya hilang
    #sandi._activate_placeholder()
    sandi.place(x=50, y= 165)

    kata1 = customtkinter.CTkLabel(master=frame, width=220, text = '______ daftar terlebih dahulu ______', font = ('Century Gothic', 12))
    kata1.place(x=50, y= 200)

    log = customtkinter.CTkButton(master = frame, width=100, text='Login', corner_radius=6, command=loby)
    log.place(x=50, y=240)

    regiss = customtkinter.CTkButton(master = frame, width=100, text='Daftar', corner_radius=6, command=register)
    regiss.place(x=168, y=240)

    logout = customtkinter.CTkButton(master = frame, width=218, text='keluar', corner_radius=6, command= keluar)
    logout.place(x=50, y=280)


    app.mainloop()

def loby():
    if username.get() in database and database[username.get()] == password.get():
        messagebox.showinfo('inpo','anjay login')
        loading()
    
    else:
        messagebox.showwarning('inpo','gada cok')
        
def register():
    
    if username.get() == '' or password.get() == '':
        messagebox.showwarning('inpo','diisi cok')
    
    elif username.get() in database:
        messagebox.showwarning('inpo','udah ada cok')
    else:
        database[username.get()] = password.get()
        messagebox.showinfo('inpo','anjay berhasil')

def loading():
    global l2
    
    #l1.configure(image=background2, text='')#mengubah background
    
    l1.destroy()
    l2 = customtkinter.CTkLabel(text='',master=app, image=background2)
    l2.pack()
    load_label = customtkinter.CTkLabel(l2, text='loading...',text_color='#ffffff',image=background2)
    
    '''def titik (t=0):
        if t < 12:
            load_label.config(text='loading'+'.' *(t % 3 + 1))
            #l2.after(500, titik, t+1)
    titik()'''
    
    
    load_label.place(relx=0.5,rely=0.6, anchor=tk.CENTER)
    load_label.configure(font=font1)

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

def asal():
    global l3
    def kembali():
        l3.destroy()
        tampilan()

    l2.destroy()
    l3 = customtkinter.CTkLabel(text='',master=app, image=gambar4)
    l3.pack()

    

    user = username.get()
    text = customtkinter.CTkLabel(master = l3, text=f'welkom {user}',text_color=putih, font = font2, bg_color= ungu)
    text.place(x=300,y=50, anchor=tk.CENTER)
    #balik = customtkinter.CTkButton(master = l3, width=30, height=30, border_width=0, text='back',text_color='#fff000', border_spacing=0, bg_color='#03412a',fg_color='#03412a', command=kembali)
    #balik.place(relx=0.01,rely=0.01)#tombol kembali
    label1_0 = customtkinter.CTkFrame(master= l3, width=150, height=240, bg_color='transparent', fg_color= abu)
    label1_0.place(x=57, y= 157)
    label1 = customtkinter.CTkFrame(master= l3, width=150, height=240,  bg_color='transparent', fg_color=ijo_terang)
    label1.place(x=50, y= 150)
    label1_1 = customtkinter.CTkLabel(label1, text='', image=gambar1, bg_color=ijo_terang)
    label1_1.place( rely=0)
    btn1 = customtkinter.CTkButton(master = label1, width=100, text='mulai', corner_radius=10,fg_color=ungu, command= Game1)
    btn1.place(relx=0.15, rely=0.7)

    label2_0 = customtkinter.CTkFrame(master= l3, width=150, height=240, bg_color='transparent', fg_color=abu)
    label2_0.place(x=232, y= 157)
    label2 = customtkinter.CTkFrame(master= l3, width=150, height=240,  bg_color='transparent', fg_color=ijo_terang)
    label2.place(x=225, y= 150)
    label2_1 = customtkinter.CTkLabel(label2, text='', image=gambar2, bg_color=ijo_terang)
    label2_1.place( rely=0)
    btn2 = customtkinter.CTkButton(master = label2, width=100, text='mulai', corner_radius=10,fg_color=ungu)
    btn2.place(relx=0.15, rely=0.7)

    label3_0 = customtkinter.CTkFrame(master= l3, width=150, height=240, bg_color='transparent', fg_color= abu)
    label3_0.place(x=407, y= 157)
    label3 = customtkinter.CTkFrame(master= l3, width=150, height=240,  bg_color='transparent', fg_color=ijo_terang)
    label3.place(x=400, y= 150)
    label3_1 = customtkinter.CTkLabel(label3, text='', image=gambar3, bg_color=ijo_terang)
    label3_1.place( rely=0)
    btn1 = customtkinter.CTkButton(master = label3, width=100, text='mulai', corner_radius=10,fg_color=ungu)
    btn1.place(relx=0.15, rely=0.7)


'''def acak_kata():
    global acak_kata
    current_round = 1
    kata1 = ['Rusa', 'Kucing', 'kambing', 'kuda', 'babi', 'anjing', 'kelinci', 'monyet', 'kudanil', 'ayam', 'singa']
    skor = 0

    l3.destroy()
    lgame1 = customtkinter.CTkLabel(text='',master=app, image=background2)
    lgame1.pack()

    #lgame1 = customtkinter.CTkFrame(lgame0, image=background2)
    #lgame1.pack()
    question_label = customtkinter.CTkLabel(lgame1, text="Tebak nama hewan: ", font=font1)
    question_label.place()
    answer_entry = customtkinter.CTkEntry(lgame1, font=font1)
    answer_entry.place()
    
    submit_button = customtkinter.CTkButton(lgame1, text="Submit", command=check_answer)
    submit_button.place()
    
    score_label = customtkinter.CTkLabel(lgame1, text="Skor: 0", font=font1)
    score_label.place()
    
        
    def scramble_word(word):
        return ''.join(random.sample(word, len(word))).lower()

    
    current_round = 1
    def display_question():
        global correct_answer
        kata2 = random.choice(kata1).lower()
        question_label.config(text="Tebak nama hewan: " + scramble_word(kata2))
        correct_answer = kata2

    #def play_game():
        
     #   global answer_entry,submit_button,score_label
        
        
        
        
        
        
        
       # play_game()
    if current_round <= 5:
            
        question_label.config(text="Tebak nama hewan: ")
        
        display_question()
        answer_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Selesai", "Game Selesai!\nSkor Anda: " + str(skor))
        quit()
    
    
        
    
    
    
    def check_answer():
        
        tebak = answer_entry.get().lower()
        
        if tebak == correct_answer:
            messagebox.showinfo("Jawaban Benar", "Anda benar!")
            skor += 1
        else:
            messagebox.showinfo("Jawaban Salah", "Anda salah!")
        
        score_label.config(text="Skor: " + str(skor))
        current_round += 1
    #self.play_game()'''
    
class Game1(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #self.title("Tebak Kata")
        #self.geometry("600x440")
        l3.destroy()
        self.selff = customtkinter.CTkLabel(app,width=600, height=440,text='', image=background2)
        self.selff.pack()
        
        self.kata1 = ['Rusa', 'Kucing', 'kambing', 'kuda', 'babi', 'anjing', 'kelinci', 'monyet', 'kudanil', 'ayam', 'singa']
        self.skor = 0
        
        self.question_label = customtkinter.CTkLabel(self.selff, text="Tebak nama hewan: ", font=("Arial", 12))
        self.question_label.place(x=50,y=10)
        
        self.answer_entry = customtkinter.CTkEntry(self.selff, font=("Arial", 12))
        self.answer_entry.place(x=50,y=110)
        
        self.submit_button = customtkinter.CTkButton(self.selff, text="Submit", command=self.check_answer)
        self.submit_button.place(x=50,y=210)
        
        self.score_label = customtkinter.CTkLabel(self.selff, text="Skor: 0", font=("Arial", 12))
        self.score_label.place(x=50,y=320)
        
        self.current_round = 1
        self.play_game()
    
    def play_game(self):
        if self.current_round <= 5:
            self.question_label.configure(text="Tebak nama hewan: ")
            self.answer_entry.delete(0, tk.END)
            self.display_question()
        else:
            messagebox.showinfo("Selesai", "Game Selesai!\nSkor Anda: " + str(self.skor))
            asal()
    
    def display_question(self):
        kata2 = random.choice(self.kata1).lower()
        self.question_label.configure(text="Tebak nama hewan: " + self.scramble_word(kata2))
        self.correct_answer = kata2
    
    def scramble_word(self, word):
        return ''.join(random.sample(word, len(word))).lower()
    
    def check_answer(self):
        tebak = self.answer_entry.get().lower()
        
        if tebak == self.correct_answer:
            messagebox.showinfo("Jawaban Benar", "Anda benar!")
            self.skor += 1
        else:
            messagebox.showinfo("Jawaban Salah", "Anda salah!")
        
        self.score_label.configure(text="Skor: " + str(self.skor))
        self.current_round += 1
        self.play_game()


    
    

tampilan()