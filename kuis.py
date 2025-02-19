'''import tkinter as tk

class Game3:
    def __init__(self):
        self.skor = 0
        self.current_soal = 0

        self.window = tk.Tk()
        self.window.title("Game")
        self.soal_label = tk.Label(self.window, text="")
        self.soal_label.pack()

        self.buttons = []
        for i in range(4):
            button = tk.Button(self.window, text="", command=lambda idx=i: self.check_jawaban(idx))
            button.pack()
            self.buttons.append(button)

        self.next_soal()

        self.window.mainloop()

    def load_soal(self):
        self.soal_label.config(text=soal[self.current_soal]["soal"])
        for i, pilihan in enumerate(soal[self.current_soal]["pilihan"]):
            self.buttons[i].config(text=pilihan)

    def check_jawaban(self, jawaban):
        if jawaban == soal[self.current_soal]["jawaban"]:
            self.skor += 1
        self.current_soal += 1
        if self.current_soal < len(soal):
            self.load_soal()
        else:
            self.soal_label.config(text="Permainan selesai!\nSkor Anda: {}/{}".format(self.skor, len(soal)))
            for button in self.buttons:
                button.config(state=tk.DISABLED)

    def next_soal(self):
        if self.current_soal < len(soal):
            self.load_soal()
        else:
            self.soal_label.config(text="Permainan selesai!\nSkor Anda: {}/{}".format(self.skor, len(soal)))
            for button in self.buttons:
                button.config(state=tk.DISABLED)

soal = [
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
    }
]

game = Game3()
'''

'''import tkinter as tk
from tkinter import messagebox

class Game3:
    def __init__(self):
        self.skor = 0
        self.current_question = 0

        self.soal = [
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

        self.window = tk.Tk()
        self.window.title("Game")
        self.question_label = tk.Label(self.window, text="Masuk ke game")
        self.question_label.pack()
        self.answer_options = []
        self.answer_var = tk.IntVar()

        for i in range(len(self.soal[self.current_question]["pilihan"])):
            answer_option = tk.Radiobutton(self.window, text=self.soal[self.current_question]["pilihan"][i], variable=self.answer_var, value=i)
            answer_option.pack()
            self.answer_options.append(answer_option)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        user_answer = self.answer_var.get()
        if user_answer == self.soal[self.current_question]["jawaban"]:
            messagebox.showinfo("Jawaban", "Anda benar!")
            self.skor += 1
        else:
            messagebox.showinfo("Jawaban", "Anda salah!")

        self.current_question += 1
        if self.current_question < len(self.soal):
            self.update_question()
        else:
            self.finish_game()

    def update_question(self):
        self.question_label.config(text=self.soal[self.current_question]["soal"])
        for i in range(len(self.answer_options)):
            self.answer_options[i].config(text=self.soal[self.current_question]["pilihan"][i])
        self.answer_var.set(0)

    def finish_game(self):
        messagebox.showinfo("Permainan Selesai", f"Skor Anda: {self.skor} dari {len(self.soal)}")
        self.window.destroy()

    def main(self):
        self.window.mainloop()

game = Game3()
game.main()
'''

import tkinter as tk
from tkinter import messagebox

class Game3:
    def __init__(self):
        self.skor = 0
        self.current_question = 0

        self.soal = [
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

        self.window = tk.Tk()
        self.window.title("Game")
        self.question_label = tk.Label(self.window, text="Masuk ke game")
        self.question_label.pack()
        self.answer_buttons = []
        self.create_answer_buttons()

    def create_answer_buttons(self):
        for i in range(len(self.soal[self.current_question]["pilihan"])):
            answer_button = tk.Button(self.window, text=self.soal[self.current_question]["pilihan"][i], command=lambda i=i: self.check_answer(i))
            answer_button.pack()
            self.answer_buttons.append(answer_button)

    def check_answer(self, user_answer):
        if user_answer == self.soal[self.current_question]["jawaban"]:
            messagebox.showinfo("Jawaban", "Anda benar!")
            self.skor += 1
        else:
            messagebox.showinfo("Jawaban", "Anda salah!")

        self.current_question += 1
        if self.current_question < len(self.soal):
            self.update_question()
        else:
            self.finish_game()

    def update_question(self):
        for answer_button in self.answer_buttons:
            answer_button.pack_forget()

        self.question_label.config(text=self.soal[self.current_question]["soal"])
        self.answer_buttons = []
        self.create_answer_buttons()

    def finish_game(self):
        messagebox.showinfo("Permainan Selesai", f"Skor Anda: {self.skor} dari {len(self.soal)}")
        self.window.destroy()

    def main(self):
        self.window.mainloop()

game = Game3()
game.main()
