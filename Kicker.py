import Scrape.NFLKickers as scrape
import Local.NFLKickers as local
import Classes.KickerClass as c
import Gui.Gui as gui


def main():

    from_file = gui.door()

    league = gui.antichambre()

    if league == "NFL":
        if from_file is True:
            kickers = local.kickerList()
        else:
            kickers = scrape.kickerList()

    
    gui.kickerking(kickers, league)




    #for kicker in nfl_kickers:
     #   print(kicker.first + " " + kicker.last)

def SelectedKicker(kicker:c.Kicker, league):
    if league == "NFL":
        print("SelectedKicker: if")
        return scrape.KickerInfo(kicker)

if __name__ == "__main__":
    main()