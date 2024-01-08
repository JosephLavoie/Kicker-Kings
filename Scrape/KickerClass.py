class Kicker:
    def __init__(self, name, team, athleteid, profile, league):
        self.name = name
        self.athleteid = athleteid
        self.team = team
        self.profile = profile
        self.league = league

        self.abr = self.getAbr()

        self.field_goal_percent_career = None
        self.field_goal_percent_season = None
        self.field_goal_attempt_average_career = None #attempts/games
        self.field_goal_attempt_average_season = None #attempts this season/games this season
        self.field_goal_made_average_career = None #goods/games
        self.field_goal_made_average_season = None #goods this season/games this season
        self.field_goal_attempt_last_game = None #attempts last game
        self.field_goal_made_last_game = None #goods last game

        self.prediction0 = None
        self.prediction1 = None

    def __str__(self):
        return f"{self.abr}: {self.name}"
    
    def getAbr(self):
        nfl_teams = {
            "Arizona Cardinals":"ARI","Atlanta Falcons":"ATL","Baltimore Ravens":"BAL",
            "Buffalo Bills":"BUF","Carolina Panthers":"CAR","Chicago Bears":"CHI",
            "Cincinnati Bengals":"CIN","Cleveland Browns":"CLE","Dallas Cowboys":"DAL",
            "Denver Broncos":"DEN","Detroit Lions":"DET","Green Bay Packers":"GB",
            "Houston Texans":"HOU","Indianapolis Colts":"IND","Jacksonville Jaguars":"JAX",
            "Kansas City Chiefs":"KC","Miami Dolphins":"MIA","Minnesota Vikings":"MIN",
            "New England Patriots":"NE","New Orleans Saints":"NO","New York Giants":"NYG",
            "New York Jets":"NYJ","Las Vegas Raiders":"LV","Philadelphia Eagles":"PHI",
            "Pittsburgh Steelers":"PIT","Los Angeles Chargers":"LAC","San Francisco 49ers":"SF",
            "Seattle Seahawks":"SEA","Los Angeles Rams":"LAR","Tampa Bay Buccaneers":"TB",
            "Tennessee Titans":"TEN","Washington Commanders":"WAS"
        }
        if self.league == "NFL":
            return nfl_teams.get(self.team, "")
