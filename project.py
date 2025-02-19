import os
import random


class Gameapp:
    global user, sandi, log, regiss, u, s, lanjut
    def __init__(self):
        self.database = {}  # tempat simpan akun
        self.nama = ""
        self.lanjut = False

    def header(self):
        os.system("cls")
        print(f"{'PROGRAM LOGIN APLIKASI':^40}")
        

    def sekat(self):
        print('='*30,'\n')
    
    def login(self):
        self.sekat()
        
        username = self.tombol(u)#input('Nama lu\t: ')
        password = self.tombol(s)#input('Pw lu\t: ')

        if username in self.database and self.database[username] == password:
            print('Anjay login!')
            self.lanjut = True
        else:
            print('Anjay login!')
            self.lanjut = False

        nama = username

    def register(self):
        self.sekat()
        username = input('Nama lu: ')
        password = input('Pw lu: ')

        if username in self.database:
            print('Udah ada cuy')
        else:
            self.database[username] = password
            print('Anjay berhasil!')

    def asal(self):
        while True:
            print('met dateng', self.nama)
            print('pilih cuy')
            print('1. game\n2. kuis mtk\n3. kuis umum\n4.kembali')

            pilih2 = input('no berapa cok : ')
            if pilih2 == '1':
                print('masuk ke game')
                game1 = Game1()
                game1.main()
            elif pilih2 == '2':
                print('masuk ke game')
                game2 = Game2()
                game2.main()
            elif pilih2 == '3':
                print('masuk ke game')
                game3 = Game3()
                game3.main()
            elif pilih2 == '4':
                return
            else:
                print('ngadi ngadi lu!')
    
    def loby(self):

        self.header()
        print()
        while True:
            print()
            print('pilih cuy')
            self.sekat()
            print('1. login\n2. daftar\n3. keluar')
            self.sekat()
            pilih1 = input('no berapa cok : ')

            if pilih1 == '1':
                self.login()
                if self.lanjut:
                    self.asal()
                else:
                    pass
            elif pilih1 == '2':
                self.register()
                print(self.database)
            elif pilih1 == '3':
                print('Arigatou')
                break
            else:
                print('yang lain napa')


        def tombol(self):
            self.u = self.user.get()
            self.s = self.sandi.get()

class Game1:
    def __init__(self):
        self.kata1 = ['Rusa', 'Kucing', 'kambing', 'kuda', 'babi', 'anjing', 'kelinci', 'monyet', 'kudanil', 'ayam', 'singa']
        self.kata2 = ""
        self.skor = 0
    
    def acak_kata(self):
        for i in range (5):

            self.kata2 = random.choice(self.kata1).lower()
            #self.kata1.remove(self.kata2)
            acak_kata = ''.join(random.sample(self.kata2, len(self.kata2))).lower()
            #return acak_kata
        ##def tebak_kata(self, kata):
            tebak = ""
            kesempatan = 3
                    
            while tebak != acak_kata:
                            
                print("\nPertanyaan", i+1, ":")   
                print("Tebak nama hewan: ", acak_kata)
                tebak = input("Tebak kata: ").lower()

                if tebak == self.kata2:
                    print('anjay!')
                    self.skor += 1    
                    break
                            
                else:
                    kesempatan -= 1
                    print('nyawalu tinggal', kesempatan)
                    print('pea lu!')
                    if kesempatan  <=0:
                        print('noob lu! , yang bener', self.kata2)
                        self.nanyak()

        self.nanyak()
        return acak_kata               
    def nanyak(self):
        while True:
            print('main lagi gak?', end='')
            main_lagi = input()
            if main_lagi.lower() == 'ya':  
                self.main() 
                break
            elif main_lagi.lower() == 'gak':
                print('skor lu nih: ', self.skor)
                return
            else:
                print('gak ngerti gua')
        return           
    def main(self):
        self.acak_kata()

class Game2:
    def __init__(self):
        self.skor = 0

    def mtk_game(self):
        print("permainan Matematika!")
        print("jawab yang bener.")

        for i in range(5):
            no1 = random.randint(1, 50)
            no2 = random.randint(1, 50)
            operator = random.choice(["+", "-", "*", "/"])

            soal = str(no1) + " " + operator + " " + str(no2)
            periksa = eval(soal)
            periksa2 = round(periksa,2)

            print("\nPertanyaan", i+1, ":")
            print(soal)

            jawaban =(input("Jawabanlu: "))
            
            try:
                if float(jawaban) == periksa2:
                    print("Anjay!")
                    self.skor += 1
                else:
                    print("salah cok. yang bener ", periksa)
            except:
                print('mana ada cok')
        print("\nSelesai!")
        print("Skorlu:", self.skor, "dari 5")

    def main(self):
        self.mtk_game()

class Game3:
    def __init__(sooal):
        sooal.skor = 0
    def soal_game(sooal):
        print("masuk ke game")
        print("jawab yang bener")

        soal = [
            {
                "soal": "berapa kaki pada hewan kaki seribu?",
                "pilihan": ["1000", "1001", "1010", "2100"],
                "jawaban": 0
            },
            {
                "soal": "Siapakah penemu kunci motor yang hilang di rumah?",
                "pilihan": ["bapak", "ibu", "adek", "Nikola Tesla"],
                "jawaban": 1
            },
            {
                "soal": "tebak apa aja hayo?",
                "pilihan": ["7", "8", "9", "10"],
                "jawaban": 1
            }
        ]

        for i, soal in enumerate(soal):
            print("\nPertanyaan", i+1, ":")
            print(soal["soal"])
            for j, pilihan in enumerate(soal["pilihan"]) :
                print(j+1, ".", pilihan)

            user_answer = int(input("Jawabanlu: "))

            if user_answer == soal["jawaban"] + 1:
                print("anjay!")
                sooal.skor += 1
            else:
                print("salah cok.")

        print("\nPermainan selesai!")
        print("Skorlu:", sooal.skor, "dari", len(soal))
    def main(sooal):
        sooal.soal_game()

class admin:
    def __init__(adm):
        adm.masukan = input()

game = Gameapp()
game.loby()
