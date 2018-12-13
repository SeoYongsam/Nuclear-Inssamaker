image study :
    "study/1.png"
    pause 0.3
    "study/2.png"
    pause 0.3
    repeat

image club_thur :
    "club/1.png"
    pause 0.3
    "club/2.png"
    pause 0.3
    repeat

image club :
    "club/3.png"
    pause 0.3
    "club/4.png"
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
        call normal_weekday_evening

    return




label normal_weekday_evening :
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
    show study at truecenter
    "공부했다\n"
    extend "체력 -15, 멘탈 -15, 공부 +10, 과 -3, 동아리 -3"

    python :
        hp -= 15
        mental_point -= 15
        study_parameter += 10
        gwa_parameter -= 3
        club_parameter -= 3

    call parameter_maxmin_check

    return

label evening_club:
    if day != 4 :
        show club at truecenter
        "동아리 개인연습했다\n"
        extend "체력 -25, 멘탈 +20, 공부 -3, 과 -3, 동아리 +15"

        python :
            hp -= 25
            mental_point += 20
            study_parameter -= 3
            gwa_parameter -= 3
            club_parameter += 15

    else :
        show club_thur at truecenter
        "동아리 정기연습했다\n"
        extend "체력 -25, 멘탈 +20, 공부 -3, 과 -3, 동아리 +25"

        python :
            hp -= 25
            mental_point += 20
            study_parameter -= 3
            gwa_parameter -= 3
            club_parameter += 25

    call parameter_maxmin_check

    return

label evening_gwa:
    show gwa at truecenter
    "과 활동했다\n"

    extend "체력 -20, 멘탈 -5, 공부 -3, 과 +15, 동아리 -3"

    python :
        hp -= 20
        mental_point -= 5
        study_parameter -= 3
        gwa_parameter += 15
        club_parameter -= 3

    call parameter_maxmin_check

    return

label evening_rest:
    show rest at truecenter
    "쉬었다\n"
    extend "체력 +50, 멘탈 +30 과 -3, 동아리 -3"

    python :
        hp += 50
        mental_point += 30
        gwa_parameter -= 3
        club_parameter -= 3

    call parameter_maxmin_check

    return
