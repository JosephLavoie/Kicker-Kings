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
            formatted_stats.append(str(format_decimal % stat))
        
        formatted_stats.append(kicker.field_goal_attempt_last_game)
        formatted_stats.append(kicker.field_goal_made_last_game)

        return formatted_stats
            


    def on_select(event):
        selected_index = kicker_listbox.curselection()
        if selected_index:
            selected_item_index = selected_index[0]

            player_label.config(text=str(kickers[selected_item_index]))
            
            if (kickers[selected_item_index]).field_goal_percent_career == None: 
                kickers[selected_item_index] = SelectedKicker(kickers[selected_item_index], league)
            
            DisplayStats(kickers[selected_item_index])

    def DisplayStats(kicker):
        print("Display Stats")

        stats = StatsFormat(kicker)

        fg_percent.config(text=f"\n\nCareer:{stats[0]}%\nSeason:{stats[1]}%")
        fg_avg_attempted.config(text=f"\n\n\n\n\n\nCareer:{stats[2]}\nSeason:{stats[3]}\nLast Game:{stats[6]}")
        fg_avg_made.config(text=f"\n\n\n\n\n\n\n\n\n\n\n\nCareer:{stats[4]}\nSeason:{stats[5]}\nLast Game:{stats[7]}")

        return None  

        

    window = tk.Tk(className="Kicker King - " + league)
    window.geometry("1200x675")

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=3)
    window.grid_columnconfigure(2, weight=3)
    window.grid_columnconfigure(3, weight=3)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    
    kicker_listbox = tk.Listbox(window, selectmode=tk.SINGLE)
    kicker_listbox.grid(row=0, column=0, rowspan=2, sticky="nesw")

    for kicker in kickers:
        kicker_listbox.insert(tk.END, kicker) 
    
    player_label = tk.Label(window, text="Selected: None", font=("Verdana", 20))
    player_label.grid(row=0, column=2, sticky="n") 
    
    kicker_listbox.bind("<<ListboxSelect>>", on_select)

    fg_avg_made = tk.Label(window, text="\n\n\n\n\n\n\n\n\n\n\n\nCareer:\nSeason:\nLast Game:", font =("Verdana", 12))
    fg_avg_made_label = tk.Label(window, text="\n\n\n\n\n\n\nAvg FGs Made:", font =("Verdana", 15))
    fg_avg_attempted = tk.Label(window, text="\n\n\n\n\n\nCareer:\nSeason:\nLast Game:", font =("Verdana", 12))
    fg_avg_attempted_label = tk.Label(window, text="\n\n\nAvg FGs Attempted:", font =("Verdana", 15))
    fg_percent = tk.Label(window, text="\n\nCareer:%\nSeason:%", font =("Verdana", 12))
    fg_percent_label = tk.Label(window, text="Field Goal %:", font =("Verdana", 15))

    fg_avg_made.grid(row=0, column=3, sticky="ne")
    fg_avg_made_label.grid(row=0, column=3, sticky="ne")
    fg_avg_attempted.grid(row=0, column=3, sticky="ne")
    fg_avg_attempted_label.grid(row=0, column=3, sticky="ne")
    fg_percent.grid(row=0, column=3, sticky="ne")
    fg_percent_label.grid(row=0, column=3, sticky="ne")


    window.mainloop()