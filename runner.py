import PySimpleGUI as sg
import math

ranks = ["Iron","Bronze", "Silver","Gold", "Platinium","Diamond","Master","Grandmaster","Challenger"]
tiers = ["IV","III", "II","I"]
icon = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsEAAA7BAbiRa+0AAATzSURBVEhLtZR7TFNXHMfvvfTS0kJbHkUeAmIFipSHlFIHlJZWRKEg2tKXUAdRnMZFB8zHYIKgDhBF42OgMHzMbEtmsplsJm7LkmXOuGwkYDLjZpYsWbJky0yWZWuJPb+zc9rLw21Ztj/2TX65N+ee8/l9z++e32EWpVjJiBUPElLSQWsoQgVlayCvpBAstiJYnpMWYJjIXDJJTEIUmv7fFGUoWq1+fHHOgfsDLfh4YCs+GmjGQwEv1nrzpuPU6e8rVia/qdIuG4iKjyoRFv07iaLkuzs+qEMU2Ov34SMkAQ2aiI5dmGvCPQ/d2HejDqsrMz6MjI/WCEv/WWKFbF3HR/Vzx+bB/jDUeXUd9kxWgW/SDLve3YC7b9lw3zdu7Dln/ZmPkbaSpWyY8PcSyzNU33b/4Am56yPgede8yQhsTS1wVTUgMlUBl6kBfcMqGPrahbecsiJeKm4TGH9RLB8de7v1NUvIYR9xSoEUTN95XQliTRbgTHXAlZqB0xuByS6AkloNDD5yYXt/xU+8jNcKrCXipL6d45Ynhx45MC1DCEyCgmlIDHrEGsqBNRLX5npgy6zA5hQBm1sEhq0a6H3gwJlr0+4ItEVlFaff7vvRg+2TZnzG7yKwp8Gx69YG2ZJSxOqJ20riutoOnLEGOF0F8LmF0HFzPfaS3XK81CcgQ1JYnZpfuj5vwLElGlg4EUvAymcbkaixEbHGasQZNwBX6wRuvQPY8hqQWGrB2JQHB6cbcZRK9aXAJIqQmb0jz4DvLSuWl5UCrfFSMK21uNWLZN09SLm/D0XUOxG3pQU4TztwlgYQWeohRaeFnulNOFWf8USgkvLy0Tt2kq1U7imEeGsZ0PouBR/1N2OJb1tQ2nEAyUcuINnB/qCo7XnE7z8CnGMbcBubIKFYB4fu2nC+LRsLWIbhpYq29vdqsM6dA8usBgIWjpkAHiBg5SZHMLHzZZR45BRKuDAVlHX2BqVDZ0G0qws4Zysk6kvhwGc2nFeXDQKWNHJcnGH7rQ14rSsLllUuguedU8cp3hZQv3gYZQ6eR2ljV5Dq+JlgzPB5xPcOg3R3Fywv1kLnnTqcpE//TcAyjG5cx299w/p781g5lqnVC6WYf9I7Q71vHxSOnoX885che2QcZbxK4KfGkOTEGKQdOwlrKlfA3nsNOG5V6icCNqy8xpxbL9yrxym5yQuOB8jp6CduXyHggtFBMExdBt3Ji5BPYFnjVyH59ASkXLoOiRUWaLtuwvYJUzBCKq8RkGHFqhOc7R/XBhu6ChCFLjomlw+Bl06dg6qb70D5tbdBN3YNNOOvw0rynrljDxi3r4a9XzRg9Ub1JEFxYeK8dAxvPmy4+9ynthCURrilW0I/z9xZB7nNTsh2eSDL5QC11wEatx20G/Oh82ET3v+9G2+eqpphRPJSgbiopIokVeOE6TvqlN7BU4HN+ETAEwKP+t2hVqfjE3N2fClgx6cDroXWP0Tui/TyFVMEIw/TlsjyUmHqsN9DJtMy+EL1pUEX0qAQGqMBN75Ckg75vaGdDZPkFTvzphkVEy2gnpKEl8feoA5pCeiPo4AR4pTCe38lCcj4/LdQkPGzASeutqU+Js2wRuD8SbxCx0gUsxESxUxkjHI2Ikoxy0bEzLAi+QwZmxVJFbORcuWsKDockQrlfbEy/j4nUX7FMLJqgfJ/i2H+AGKN3gvOW8mPAAAAAElFTkSuQmCC'
def calculate_lp(frank, ftier, flp, trank, ttier, tlp):
    if((not frank in ranks) or (not trank in ranks)):
        raise ValueError("Select proper ranks.")
    if(((not ftier in tiers) and flp == "") or ((not ttier in tiers) == "" and tlp == "")):
        raise ValueError("Select proper tiers or LP.")
    
    if ranks.index(frank) > 5:
        frank = "Master"
        ftier = "IV"
        flp = int(flp)
    else:
        flp = 0 
    if ranks.index(trank) > 5:
        trank = "Master"
        ttier = "IV"
        tlp = int(tlp)  
    else:
        tlp = 0  
    if (ranks.index(frank) > ranks.index(trank)) or ((not ranks.index(frank) == 6) and ranks.index(frank) == ranks.index(trank) and tiers.index(ftier) >= tiers.index(ttier)):
        raise ValueError("Go learn to play! You should climb, not fall.")
    req_lp = ((((ranks.index(trank)) - (ranks.index(frank) + 1)) * 4 + tiers.index(ttier) + 4 - tiers.index(ftier)) * 100) + (tlp - flp)
    return req_lp

def calculate_matches(wr, glp, llp, req_lp):
    if(wr == "" or glp == "" or llp == "" ):
        raise ValueError("Enter the data required.")
    wr = int(wr)
    llp = int(llp)
    glp = int(glp)
    result = {}
    wr = wr / 100
    net_lp = wr * glp - (1 - wr) * llp
    result["req_lp"] = req_lp
    result["net_lp"] = net_lp
    result["matches"] = math.ceil(req_lp / net_lp)
    result["full_win_matches"] = math.ceil(req_lp / glp)
    if net_lp <= 0:
        raise ValueError("Go learn to play! Your net lp is negative or zero.")
    return result



input_column = [
    [
        sg.Text("Win Rate:", background_color = "#005A82", text_color = "#C8AA6E"),
        sg.In(size = (25, 1), tooltip = "0 - 100", key = "-WIN_RATE-", background_color = "#CDFAFA", text_color = "#32281E")
    ],
    [
        sg.Text("LP Gain:  ", background_color = "#005A82", text_color = "#C8AA6E"),
        sg.In(size = (25, 1), tooltip = "Average LP Gain in Victory", key = "-LP_GAIN-", background_color = "#CDFAFA")
    ],
    [
        sg.Text("LP Loss:  ", background_color = "#005A82", text_color = "#C8AA6E"),
        sg.In(size=(25, 1), tooltip = "Average LP Loss in Defeat", key = "-LP_LOSS-", background_color = "#CDFAFA"),
    ],  
    [
    sg.Text("Initial Rank:", background_color = "#005A82", text_color = "#C8AA6E"),
    sg.Combo(ranks, default_value = "Iron", size = (10, 1),  expand_x = True, enable_events = True,  readonly = False, key = '-RANK_INIT-', background_color = "#CDFAFA"),
    sg.Combo(tiers,  size = (3, 1),  expand_x = True,  readonly=False, key = '-TIER_INIT-', background_color = "#CDFAFA"),
    sg.In(size = (3, 1), tooltip = "Initial LP If initial rank master+", key = "-LP_INIT-", visible = False, background_color = "#CDFAFA"),
    ],
    [
    sg.Text("Final Rank:", background_color = "#005A82", text_color = "#C8AA6E"),
    sg.Combo(ranks, default_value = "Diamond", size=(10, 1),  expand_x = True, enable_events = True,  readonly = False, key = '-RANK_FINAL-', background_color = "#CDFAFA"),
    sg.Combo(tiers,  size = (3, 1), expand_x = True, enable_events = True,  readonly = False, key = '-TIER_FINAL-',background_color = "#CDFAFA"),
    sg.In(size = (3, 1), tooltip = "Final LP If Final Rank Master+", key = "-LP_FINAL-", visible = False, background_color = "#CDFAFA"),
    ],
    [
        sg.Button("Calculate!", enable_events = True, key = "-CALCULATE-")
    ]

]

output_column = [
    [
    sg.Text("LP Required: ", background_color = "#005A82", text_color = "#C8AA6E"),
    sg.Text(key = "-OUT_LPREQ-", background_color = "#005A82")
    ],
    [
    sg.Text("Net LP Gain: ", background_color = "#005A82", text_color = "#C8AA6E"),
    sg.Text(key = "-OUT_NETLP-", background_color = "#005A82") 
    ],
    [
    sg.Text("Required Matches: ", background_color = "#005A82", text_color = "#C8AA6E"),
    sg.Text(key = "-OUT_MATCHES-", background_color = "#005A82")
    ],
    [
    sg.Text("Full Win Required Matches: ", background_color = "#005A82", text_color = "#C8AA6E"),
    sg.Text(key = "-OUT_WINMATCHES-", background_color = "#005A82")
    ]

]
layout = [
    [
        sg.Column(input_column, background_color = "#005A82"),
        sg.VSeperator(),
        sg.Column(output_column, background_color = "#005A82")
    ]
]

window = sg.Window("LoL LP Calculator", layout, button_color = "#5B5A56", background_color = "#005A82", icon = icon, titlebar_icon = icon,  use_custom_titlebar = True, titlebar_background_color = "#091428", titlebar_text_color = "#C89B3C", no_titlebar = False, keep_on_top = True)

while True:
    event, values = window.read()
    if  event == sg.WIN_CLOSED:
        break
    elif event == "-CALCULATE-":
            try:
                req_lp = calculate_lp((values["-RANK_INIT-"]), values["-TIER_INIT-"], values["-LP_INIT-"], values["-RANK_FINAL-"], values["-TIER_FINAL-"], values["-LP_FINAL-"])
                result = calculate_matches(values["-WIN_RATE-"], values["-LP_GAIN-"], values["-LP_LOSS-"], req_lp)
                window["-OUT_LPREQ-"].update(value = result["req_lp"])
                window["-OUT_NETLP-"].update(value = result["net_lp"])
                window["-OUT_MATCHES-"].update(value = result["matches"])
                window["-OUT_WINMATCHES-"].update(value = result["full_win_matches"])
            except Exception as e:
                sg.popup(e, keep_on_top = True, icon = icon, title = "!!")
    if values["-RANK_INIT-"] == "Master" or values["-RANK_INIT-"] == "Grandmaster" or values["-RANK_INIT-"] == "Challenger":
        window["-LP_INIT-"].update(visible = True)
        window["-TIER_INIT-"].update(visible = False, value = "")  
    else:
        window["-LP_INIT-"].update(visible = False, value = "")
        window["-TIER_INIT-"].update(visible = True)

    if values["-RANK_FINAL-"] == "Master" or values["-RANK_FINAL-"] == "Grandmaster" or values["-RANK_FINAL-"] == "Challenger":
        window["-LP_FINAL-"].update(visible = True)
        window["-TIER_FINAL-"].update(visible = False, value = "")  
    else:
        window["-LP_FINAL-"].update(visible = False, value = "")
        window["-TIER_FINAL-"].update(visible = True)
    

window.close()

