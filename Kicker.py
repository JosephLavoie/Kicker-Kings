import Scrape.NFLKickers as nfl
import Gui.Gui as gui

def main():
    league = gui.start()

    if league == "NFL":
        kickers = nfl.kickerList()
    
    gui.kickerking(kickers, league)




    #for kicker in nfl_kickers:
     #   print(kicker.first + " " + kicker.last)

if __name__ == "__main__":
    main()