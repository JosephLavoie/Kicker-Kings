import tkinter as tk
from Kicker import SelectedKicker
import Scrape.KickerClass as c

def start():
    league = ""

    def set_league(league_name):
        nonlocal league
        league = league_name
        window.destroy()

    window = tk.Tk(className="Kicker King - Leagues")
    window.geometry("800x450")

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)

    title = tk.Label(window, text="Select a league", font=("Verdana", 20))
    title.grid(row=0, column=1)

    nfl_button = tk.Button(window, text="NFL", command=lambda: set_league("NFL"), height=5, width=15, font=("Verdana", 15))
    nfl_button.grid(row=1, column=0, sticky="n")

    cfb_button = tk.Button(window, text="CFB", command=lambda: set_league("CFB"), height=5, width=15, font=("Verdana", 15))
    cfb_button.grid(row=1, column=2, sticky="n")

    window.mainloop()

    return league


def kickerking(kickers:list, league:str):

    def on_select(event):
        selected_index = kicker_listbox.curselection()
        if selected_index:
            selected_item_index = selected_index[0]
            kicker = kickers[selected_item_index]

            player_label.config(text=str(kicker))
            
            if (kickers[selected_item_index]).field_goal_percent_career == None: 
                kickers[selected_item_index] = SelectedKicker(kicker, league)
    
            DisplayStats(kickers[selected_item_index])

    def DisplayStats(kicker):
        print("Display Stats")
        info.config(text="We are displaying!!!!!")

        return None  

        

    window = tk.Tk(className="Kicker King - " + league)
    window.geometry("1200x675")
    
    kicker_listbox = tk.Listbox(window, selectmode=tk.SINGLE)
    kicker_listbox.pack(side=tk.LEFT, fill=tk.BOTH) 

    for kicker in kickers:
        kicker_listbox.insert(tk.END, kicker) 
    
    player_label = tk.Label(window, text="Selected: None", font = "30")
    player_label.pack()
    
    kicker_listbox.bind("<<ListboxSelect>>", on_select)

    info = tk.Label(window, text="Not Displaying", font = "30")
    info.pack()

    window.mainloop()