from tkinter import *
import random

def game_win(win):
    """Loo mänguaken"""
    win.title("Lumepalli klõpsamise mäng")
    win.geometry("600x400")
    win.configure(bg="lightblue")
    
    # Algväärtused
    score = 0
    time = 30
    pallid = []  # Salvestame kõik loodud pallide ID-d
    
    # Skoori ja aja kuvamine
    score_label = Label(win, text=f"Skoor: {score}", font=("Arial", 14), bg="lightblue")
    score_label.pack(pady=10)

    time_label = Label(win, text="Aega jäänud: " + str(time) + " s", font=("Arial", 14), bg="lightblue")
    time_label.pack(pady=10)
    
    # Valge osa pallide jaoks
    canvas = Canvas(win, width=600, height=300, bg="white")
    canvas.pack()
    
    def uuenda_aega():
        """Vähenda aega iga sekundi järel"""
        nonlocal time
        if time > 0:  # Kui aega on veel jäänud
            time -= 1
            time_label.config(text=f"Aega jäänud: {time} s")
            loo_pall()  # Loo uus pall iga sekundi järel
            win.after(1000, uuenda_aega)  # Taaskäivita 1 sekundi pärast
        else:  # Kui aeg saab otsa, siis
            canvas.delete("all")  # Kustutame kõik lõuendi elemendid
            canvas.create_text(300, 150, text=f"Mäng läbi!\nLõppskoor: {score}", font=("Arial", 16), fill="red", tags="lõpp")
            # Lisa nupp "Mängi uuesti"
            canvas.create_text(300, 250, text="Mängi uuesti", font=("Arial", 14), fill="blue", tags="mängi_uuesti")
            # Siduge lõuendi klikiga nupp "Mängi uuesti"
            canvas.tag_bind("mängi_uuesti", "<Button-1>", restart_game)
    
    
    def loo_pall():
        """Loo juhuslik pall, millele saab vajutada"""
        
         # Arvuta, mitu palli tuleb luua vastavalt skoorile
        pallide_arv = 1 + (score // 10)
            
        for i in range(pallide_arv):
            x = random.randint(50, 550)  # Juhuslik X koordinaat
            y = random.randint(50, 250)  # Juhuslik Y koordinaat
            radius = 20  # Palli raadius
            pall = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue", tags="pall")
        
            # Salvesta pallide ID-d
            pallid.append(pall)
            
            # Seosta pallile klikkimise sündmus
            canvas.tag_bind(pall, "<Button-1>", lambda event, p=pall: pall_clicked(p))  # Kui pallile klikitakse, käivitage pall_clicked funktsioon.
    
            # Pärast 2 sekundi möödumist kustutame palli, kui sellele ei ole vajutatud
            win.after(2000, pall_kustuta, pall)  # Kutsume pall_kustuta funktsiooni 2 sekundi pärast
            
    def pall_clicked(pall):
        """Kui pallile vajutatakse, suurendame skoori ja kustutame palli"""
        nonlocal score
        score += 1  # Suurendame skoori
        score_label.config(text=f"Skoor: {score}")  # Uuendame skoori
        canvas.delete(pall)  # Kustutame klikkimisega palli
        pallid.remove(pall)  # Eemaldame pallist ID nimekirjast
    
    def pall_kustuta(pall):
        """Kustuta pall, kui sellele ei ole vajutatud."""
        if pall in pallid:  # Kui pall on veel olemas
            canvas.delete(pall)  # Kustutame palli
            pallid.remove(pall)  # Eemaldame pallist ID nimekirjast
    
    def restart_game(event=None):
        """Alusta mängu algusest peale"""
        nonlocal score, time, pallid
        score = 0
        time = 30
        pallid = []  # Eemaldame kõik varasemad pallid
        score_label.config(text=f"Skoor: {score}")
        time_label.config(text=f"Aega jäänud: {time} s")
        canvas.delete("all")  # Kustutame kõik lõuendi elemendid
        uuenda_aega()  # Käivita taimer uuesti
        
        
        
    uuenda_aega()  # Käivita taimer

# Mängu käivitamine
root = Tk()
game = game_win(root)
root.mainloop()
