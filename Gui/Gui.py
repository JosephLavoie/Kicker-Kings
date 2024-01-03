import tkinter as tk

def start():
    league = ""

    def set_league(league_name):
        nonlocal league
        league = league_name
        window.destroy()

    window = tk.Tk(className="Kicker King - Leagues")
    window.geometry("800x450")
    tk.Label(window, text="Select a league", font="50").pack()
    tk.Button(window, text="NFL", command=lambda:set_league("NFL"), height=5, width=15, font="30").pack()

    window.mainloop()

    return league
        


def kickerking(kickers:list, league:str):
    window = tk.Tk(className="Kicker King - " + league)
    window.geometry("1200x675")
    mylabel = tk.Label(window, text ='Scrollbars', font = "30").pack()
    
    myscroll = tk.Scrollbar(window)
    myscroll.pack(side = tk.RIGHT, fill = tk.Y) 
    
    mylist = tk.Listbox(window, kickers, yscrollcommand = myscroll.set)  
    mylist.pack(side = tk.LEFT, fill = tk.BOTH)    
    
    myscroll.config(command = mylist.yview)
    window.mainloop()