# GUI
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

from blackjack import BlackjackGame

def on_enter_stand(event):
    event.widget.config(bg="#993D3D", fg="white")

def on_leave_stand(event):
    event.widget.config(bg="#FF6666", fg="black")
def on_enter_hit(event):
    event.widget.config(bg="#3D993D", fg="white")

def on_leave_hit(event):
    event.widget.config(bg="#66FF66", fg="black")
def on_enter_new(event):
    event.widget.config(bg="#d8e8da", fg="#2F2F2D")

def on_leave_new(event):
    event.widget.config(bg="#EBECE4", fg="#2F2F2D")



class BlackjackGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")
        self.game = BlackjackGame()
        self.card_images = self.load_card_images()

        # Create canvas to display cards
        self.canvas = tk.Canvas(master, width=800, height=600,bg='green')

        self.canvas.pack()
        # Create buttons for player actions
        self.hit_button = tk.Button(master, text="Hit", command=self.hit, bg="#66FF66", fg="black")
        self.hit_button.bind("<Enter>", on_enter_hit)
        self.hit_button.bind("<Leave>", on_leave_hit)
        self.hit_button.pack(side=tk.LEFT,padx=20,pady=50)

        self.stand_button = tk.Button(master, text="Stand", command=self.stand, bg="#FF6666", fg="black")
        self.stand_button.bind("<Enter>", on_enter_stand)
        self.stand_button.bind("<Leave>", on_leave_stand)
        self.stand_button.pack(side=tk.LEFT,padx=40,pady=50)

        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game, bg="#EBECE4", fg="#2F2F2D", width=10, height=2)
        self.new_game_button.bind("<Enter>", on_enter_new)
        self.new_game_button.bind("<Leave>", on_leave_new)
        self.new_game_button.pack(side=tk.RIGHT,pady=50,padx=50)

        self.update_labels()
        # Create buttons and labels (similar to previous code)

    def load_card_images(self):
        suits = ['DIAMONDS', 'CLUBS', 'HEARTS', 'SPADES']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_images = {}

        for suit in suits:
            for value in values:
                if value=='J':
                    val='jack'
                elif value=='Q':
                    val='queen'
                elif value=='K':
                    val='king'
                elif value=='A':
                    val='ace'
                else:
                    val=value

                image = Image.open(
                    f'images/{val}_of_{suit.lower()}.png')  # Assuming you have images in a folder called 'images'
                image = image.resize((75, 100))
                card_images[f'{value}{suit}'] = ImageTk.PhotoImage(image)
        image = Image.open(
            f'images/cardNazad.jpg')  # Assuming you have images in a folder called 'images'
        image = image.resize((75, 100))
        card_images['back'] = ImageTk.PhotoImage(image)
        return card_images

    def update_labels(self):
        self.canvas.delete("all")
        self.display_prediction(self.game.racunaj_predikciju(),500,300)
        self.display_hand(self.game.get_karte_igrac(), 100, 400)
        self.display_hand_dealer(self.game.get_karte_diler(), 100, 100)



    def update_labels_show(self):

        self.canvas.delete("all")
        self.display_prediction(self.game.racunaj_predikciju(),500,300)
        self.display_hand(self.game.get_karte_igrac(), 100, 400)
        self.display_hand(self.game.get_karte_diler(), 100, 100)

    def display_prediction(self,prediction,x,y):
        self.canvas.create_text(x, y, anchor=tk.NW,text=prediction, font=("Arial", 12))

    def display_hand(self, hand, x, y):
        for card in hand:
            print(card)
            print("----------------------")
            card_image = self.card_images[card]
            self.canvas.create_image(x, y, anchor=tk.NW, image=card_image)
            x += 80

    def display_hand_dealer(self, hand, x, y):
        for card in hand:
            print(card)
            print("----------------------")
            card_image = self.card_images[card]
            self.canvas.create_image(x, y, anchor=tk.NW, image=card_image)
            x += 80
        if len(hand)==1:
            card_image = self.card_images['back']
            self.canvas.create_image(x, y, anchor=tk.NW, image=card_image)
            x += 80

    def hit(self):

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = (screen_width - root.winfo_reqwidth()) // 2
        center_y = (screen_height - root.winfo_reqheight()) // 2
        root.geometry(f"+{center_x}+{center_y}")

        #TODO PISI ISPOD

        self.game.igrac_hit()

        self.update_labels()

        if self.game.igrac_izgubio():
            messagebox.showinfo('Resultat', 'izgubili ste')
            self.new_game()

    def stand(self):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = (screen_width - root.winfo_reqwidth()) // 2
        center_y = (screen_height - root.winfo_reqheight()) // 2
        root.geometry(f"+{center_x}+{center_y}")

        # TODO PISI ISPOD

        self.game.igrac_stand()

        self.update_labels()

        self.game.diler_hit()
        self.update_labels()  # iscrtava nesto u GUI-u

        while self.game.get_zbir_diler() < 17:

            self.game.diler_hit()
            self.update_labels()

        if self.game.diler_izgubio() or self.game.get_zbir_diler() < self.game.get_zbir_igrac():
            messagebox.showinfo('Resultat', 'pobedili ste')
            self.new_game()
        else:
            messagebox.showinfo('Resultat', 'izgubili ste')

        self.new_game()

    def new_game(self):
        # TODO zapocni igru

        self.game.zapocni_igru()

        self.update_labels()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = (screen_width - root.winfo_reqwidth()) // 2
        center_y = (screen_height - root.winfo_reqheight()) // 2
        root.geometry(f"+{center_x}+{center_y}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#4E4D50")
    gui = BlackjackGUI(root)
    root.mainloop()
# graficko okruzenje