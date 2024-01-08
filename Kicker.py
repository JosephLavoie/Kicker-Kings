import Scrape.NFLKickers as nfl
import Scrape.KickerClass as c
import Gui.Gui as gui


def main():
    league = gui.start()

    if league == "NFL":
        kickers = nfl.kickerList()
    
    gui.kickerking(kickers, league)




    #for kicker in nfl_kickers:
     #   print(kicker.first + " " + kicker.last)

def SelectedKicker(kicker:c.Kicker, league):
    if league == "NFL":
        print("SelectedKicker: if")
        return nfl.KickerInfo(kicker)

if __name__ == "__main__":
    main()