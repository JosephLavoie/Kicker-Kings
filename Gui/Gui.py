import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from Kicker import SelectedKicker
import Classes.KickerClass as c
import Save.NFLKickers as save

def door():
    from_file = None

    def set_flow(from_local:bool):
        nonlocal from_file
        from_file = from_local
        window.destroy()

    window = tk.Tk(className="Kicker King - Startup")
    window.geometry("800x450")

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)

    title = tk.Label(window, text="Select an option", font=("Verdana", 20))
    title.grid(row=0, column=1)

    nfl_button = tk.Button(window, text="From Network", command=lambda: set_flow(False), height=5, width=15, font=("Verdana", 15))
    nfl_button.grid(row=1, column=0, sticky="n")

    cfb_button = tk.Button(window, text="From Save", command=lambda: set_flow(True), height=5, width=15, font=("Verdana", 15))
    cfb_button.grid(row=1, column=2, sticky="n")

    window.mainloop()

    return from_file

def antichambre():
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


def kickerking(kickers:list, league:str, from_file:bool):

    after_decimal = 2

    def StatsFormat(kicker):
        formatted_stats = []

        format_decimal = f"%0.{str(after_decimal)}f"

        statistics = [kicker.field_goal_percent_career,
                    kicker.field_goal_percent_season,
                    kicker.field_goal_attempt_average_career,
                    kicker.field_goal_attempt_average_season,
                    kicker.field_goal_made_average_career,
                    kicker.field_goal_made_average_season
                    ]

        for stat in statistics:
            formatted_stats.append(format_decimal % stat)
        
        formatted_stats.append(kicker.field_goal_attempt_last_game)
        formatted_stats.append(kicker.field_goal_made_last_game)

        return formatted_stats
            


    def on_select(event):
        selected_index = kicker_listbox.curselection()
        if selected_index:
            selected_item_index = selected_index[0]

            player_label.config(text=str(kickers[selected_item_index]))
            
            if (kickers[selected_item_index]).field_goal_percent_career == None:
                kickers[selected_item_index] = SelectedKicker(kickers[selected_item_index], league, from_file)
            
            DisplayStats(kickers[selected_item_index])

    stats = []

    def DisplayStats(kicker):
        print("Display Stats")
        nonlocal stats
        stats = StatsFormat(kicker)

        fg_avg_made_last_game.config(text=f"\n\n\n\n\n\n\n\n\n\nLast Game:{stats[7]}")
        fg_avg_made_season.config(text=f"\n\n\n\n\n\n\n\n\nSeason:{stats[5]}")
        fg_avg_made_career.config(text=f"\n\n\n\n\n\n\n\nCareer:{stats[4]}")
        fg_avg_attempted_last_game.config(text=f"\n\n\n\n\n\nLast Game:{stats[6]}")
        fg_avg_attempted_season.config(text=f"\n\n\n\n\nSeason:{stats[3]}")
        fg_avg_attempted_career.config(text=f"\n\n\n\nCareer:{stats[2]}")
        fg_percent_season.config(text=f"\n\nSeason:{stats[1]}%")
        fg_percent_career.config(text=f"\nCareer:{stats[0]}%")

        return None
    
    def SaveData():
        save_kickers = save.SaveKickerInfo(kickers)

        save_window = tk.Tk(className="Saved Kickers")
        save_window.geometry("400x400")

        saved_listbox = tk.Listbox(save_window)
        saved_listbox.pack(expand=True, fill='both')

        for kicker in save_kickers:
            saved_listbox.insert(tk.END, kicker)

        save_window.mainloop()



    window = tk.Tk(className="Kicker King - " + league)
    window.geometry("1200x675")

    projection = tk.StringVar()

    def projection_check():
        try:
            proj = float(projection.get())

        except:
            return None 
        if not stats:
            return None
        
        stats_labels = [fg_avg_attempted_career, fg_avg_attempted_season, fg_avg_made_career,
                        fg_avg_made_season, fg_avg_attempted_last_game, fg_avg_made_last_game]
        
        for i in range(len(stats[2:])):
            if proj > float(stats[i+2]):
                stats_labels[i].config(fg="red")
            elif proj < float(stats[i+2]):
                stats_labels[i].config(fg="green")

            
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=3)
    window.grid_columnconfigure(2, weight=3)
    window.grid_columnconfigure(3, weight=3)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)

    
    kicker_listbox = tk.Listbox(window, selectmode=tk.SINGLE)
    kicker_listbox.grid(row=0, column=0, rowspan=3, sticky="nesw")

    for kicker in kickers:
        kicker_listbox.insert(tk.END, kicker) 
    
    player_label = tk.Label(window, text="Selected: None", font=("Verdana", 20))
    player_label.grid(row=0, column=2, sticky="n") 
    
    kicker_listbox.bind("<<ListboxSelect>>", on_select)

    fg_avg_made_last_game = tk.Label(window, text="\n\n\n\n\n\n\n\n\n\nLast Game:", font =("Verdana", 12))
    fg_avg_made_season = tk.Label(window, text="\n\n\n\n\n\n\n\n\nSeason:", font =("Verdana", 12))
    fg_avg_made_career = tk.Label(window, text="\n\n\n\n\n\n\n\nCareer:", font =("Verdana", 12))
    fg_avg_made = tk.Label(window, text="\n\n\n\n\n\n\nAvg FGs Made:", font =("Verdana", 12, "bold"))
    fg_avg_attempted_last_game = tk.Label(window, text="\n\n\n\n\n\nLast Game:", font =("Verdana", 12))
    fg_avg_attempted_season = tk.Label(window, text="\n\n\n\n\nSeason:", font =("Verdana", 12))
    fg_avg_attempted_career = tk.Label(window, text="\n\n\n\nCareer:", font =("Verdana", 12))
    fg_avg_attempted = tk.Label(window, text="\n\n\nAvg FGs Attempted:", font =("Verdana", 12, "bold"))
    fg_percent_season = tk.Label(window, text="\n\nSeason:%", font =("Verdana", 12))
    fg_percent_career = tk.Label(window, text="\nCareer:%", font =("Verdana", 12))
    fg_percent = tk.Label(window, text="Field Goal %:", font =("Verdana", 12, "bold"))

    fg_avg_made_last_game.grid(row=0, column=3, sticky="ne")
    fg_avg_made_season.grid(row=0, column=3, sticky="ne")
    fg_avg_made_career.grid(row=0, column=3, sticky="ne")
    fg_avg_made.grid(row=0, column=3, sticky="ne")
    fg_avg_attempted_last_game.grid(row=0, column=3, sticky="ne")
    fg_avg_attempted_season.grid(row=0, column=3, sticky="ne")
    fg_avg_attempted_career.grid(row=0, column=3, sticky="ne")
    fg_avg_attempted.grid(row=0, column=3, sticky="ne")
    fg_percent_season.grid(row=0, column=3, sticky="ne")
    fg_percent_career.grid(row=0, column=3, sticky="ne")
    fg_percent.grid(row=0, column=3, sticky="ne")


    save_button = tk.Button(window, text="Save", command=SaveData)
    save_button.grid(row=0, column=1, sticky="n", pady=10)


    u_projection_label = tk.Label(window, text="Your Projection:", font=("Verdana", 15))
    u_projection_label.grid(row=2, column=3, sticky="n")

    u_projection_entry = tk.Entry(window, textvariable=projection, font=("Verdana", 12))
    u_projection_entry.grid(row=2, column=3)
    u_projection_entry.focus()

    projection_button = tk.Button(window, text="Projection Check", command=projection_check)
    projection_button.grid(row=2, column=3, sticky="s", pady=10)
    


    window.mainloop()