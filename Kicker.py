import Scrape.NFLKickers as nfl
import Scrape.KickerClass as c
import Gui.Gui as gui

def main():
    global league
    league = gui.start()

    if league == "NFL":
        kickers = nfl.kickerList()
    
    gui.kickerking(kickers, league)




    #for kicker in nfl_kickers:
     #   print(kicker.first + " " + kicker.last)

def SelectedKicker(kicker:c.Kicker):
    if league == "NFL":
        return nfl.KickerInfo()

if __name__ == "__main__":
    main()