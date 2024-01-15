import Classes.KickerClass as c

def SaveKickerInfo(kickers:list):
    save_kickers = []
    with open("k.info", 'w'): pass

    for k in kickers:
            if k.field_goal_percent_season:
                save_kickers.append(k)
    


    for k in save_kickers:
        with open("k.info", 'a') as file:
            file.write(f"{k.name},{k.team},{k.athleteid},{k.profile},NFL\n")
            
        with open(f"{k.athleteid}.info", 'w') as file:
            file.write(f"{k.field_goal_percent_season},{k.field_goal_percent_career},{k.field_goal_made_last_game},{k.field_goal_attempt_last_game},{k.field_goal_made_average_season},{k.field_goal_made_average_career},{k.field_goal_attempt_average_season},{k.field_goal_attempt_average_career}")

    
    return save_kickers
