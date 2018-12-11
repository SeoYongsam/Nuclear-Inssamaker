# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label weekday_day_event :
    $ day_or_evening = "day"

    if month == 3 and week == 2 and day == 1 :
        call dongsoze

    elif month == 3 and week == 2 and day == 5 :
        call all_mt

    elif month == 4 and week == 1 and day == 1 :
        call uniform_day

    elif month == 4 and week == 1 and day == 5 :
        call fun_mt

    elif month == 5 and week == 1 and day == 2 :
        call jangtuh

    elif month == 5 and week == 2 and day == 2 :
        call han_river

    elif month == 5 and week == 3 and day == 6 :
        call olympic

    elif day == 6 :
        "토요일 낮이 되었다."
        if day_schedule[month - 3][(week - 1) * 8 + day] == 1:
            call evening_study

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 2:
            call evening_club

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 3:
            call evening_gwa

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 4:
            call evening_rest

    else :
        $ day_or_evening = "evening"

    return
