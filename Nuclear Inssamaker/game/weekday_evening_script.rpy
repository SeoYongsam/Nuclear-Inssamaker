image study :
    "study/1.png"
    pause 0.3
    "study/2.png"
    pause 0.3
    repeat

image club :
    "club/1.png"
    pause 0.3
    "club/2.png"
    pause 0.3
    repeat

image gwa :
    "gwa/1.png"
    pause 0.3
    "gwa/2.png"
    pause 0.3
    repeat

image rest :
    "rest/1.png"
    pause 0.3
    "rest/2.png"
    pause 0.3
    repeat

label weekday_evening_event :
    $ day_or_evening = "evening"

    if month == 3 and week == 2 and day == 4 :
        call club_first

    elif month == 4 and week == 2 and day == 3 :
        call pcbang

    elif month == 4 and week == 3 and day == 1 :
        call festival

    elif month == 5 and week == 3 and day == 1 :
        call karaoke

    else :
        if day_schedule[month - 3][(week - 1) * 8 + day] == 1:
            call evening_study

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 2:
            call evening_club

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 3:
            call evening_gwa

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 4:
            call evening_rest

        else :
            extend "에러"
    return

label evening_study:
    $ rand = renpy.random.randint(1, 2)
    #$ renpy.scene()
    #$ renpy.show("study/%d.jpg" %rand)
#임시
    show study at truecenter
    "공부했다\n"
    extend "체력 -5, 멘탈 -5, 공부 +10, 과 -5, 동아리 -5"

    python :
        hp -= 5
        mental_point -= 5
        study_parameter += 10
        gwa_parameter -= 5
        club_parameter -= 5

    call parameter_maxmin_check

    return

label evening_club:
    $ rand = renpy.random.randint(1, 2)
    show club at truecenter
    "동아리 활동했다\n"
    extend "체력 -15, 멘탈 +10, 공부 -5, 과 -5, 동아리 +15"

    python :
        hp -= 15
        mental_point += 10
        study_parameter -= 5
        gwa_parameter -= 5
        club_parameter += 15

    call parameter_maxmin_check

    return

label evening_gwa:
#    $ rand = renpy.random.randint(1, 6)
    show gwa at truecenter
    "과 활동했다\n"

    extend "체력 -10, 공부 -5, 과 +15, 동아리 -5"

    python :
        hp -= 10
        mental_point += 0
        study_parameter -= 5
        gwa_parameter += 15
        club_parameter -= 5

    call parameter_maxmin_check

    return

label evening_rest:
#    $ rand = renpy.random.randint(1, 6)
    show rest at truecenter
    "쉬었다\n"
    extend "체력 +20, 과 -5, 동아리 -5"

    python :
        hp += 20
        gwa_parameter -= 5
        club_parameter -= 5

    call parameter_maxmin_check

    return
