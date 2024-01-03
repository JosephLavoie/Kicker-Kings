import Scrape.NFLKickers as nfl
import Tkinter.Gui as gui

def main():
    
    kickers = nfl.kickerList()
    gui.start()



    #for kicker in nfl_kickers:
     #   print(kicker.first + " " + kicker.last)

if __name__ == "__main__":
    main()