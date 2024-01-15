import Classes.KickerClass as c
    
def kickerList():

    info_lines, kickers = [], []
    try:
        with open("K.info", 'r') as file:
                # Read each line from the file and append it to the list
                for line in file:
                    info_lines.append(line.strip())
    except:
        #Error
        return None
    
    for e in info_lines:
        info = e.split(',')

        kickers.append(c.Kicker(info[0], info[1], info[2], info[3], "NFL"))
    
    return kickers

def KickerInfo(kicker:c.Kicker):
    
    info_lines = []
    try:
        info_line = open(f"{kicker.athleteid}.info").readline().rstrip()
    except:
        # No info was found
        return kicker
    
    info = info_line.split(',')

    kicker.field_goal_percent_season =  float(info[0])
    kicker.field_goal_percent_career =  float(info[1])
    kicker.field_goal_made_last_game =  int(info[2])
    kicker.field_goal_attempt_last_game =  int(info[3])
    kicker.field_goal_made_average_season =  float(info[4])
    kicker.field_goal_made_average_career =  float(info[5])
    kicker.field_goal_attempt_average_season =  float(info[6])
    kicker.field_goal_attempt_average_career =  float(info[7])

    print("v-v-v--------Removable-------v-v-v")

    print(kicker.field_goal_percent_season)
    print(kicker.field_goal_percent_career)
    print(kicker.field_goal_made_last_game)
    print(kicker.field_goal_attempt_last_game)
    print(kicker.field_goal_made_average_season)
    print(kicker.field_goal_made_average_career)
    print(kicker.field_goal_attempt_average_season)
    print(kicker.field_goal_attempt_average_career)

    print("-------------Removable-------------")


    return kicker
