define Jinil = Character("진일", color="#ffcccc", image="Jinil")#, window_left_padding = -100)
#image side Jinil :
#    "character/cha1.png"
#    xzoom -1

define Player = Character("주인공", color="#ffcccc", image="Player")
#image side Player :
#    "character/cha2.png"
#    xzoom -1

define Jangjung = Character("장중", color="#ffcccc", image="Jangjung")
#image side Jangjung :
#    "character/cha3.png"
#    xzoom -1

define Samyong = Character("삼용", color="#ffcccc", image="Samyong")
#image side Samyong :
#    "character/cha4.png"
#    xzoom -1


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
    show expression ("study/%d.png" %rand) at truecenter
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
    show expression ("club/%d.png" %rand) at truecenter
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
    show expression ("gwa/1.png") at truecenter
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
    show expression ("rest/1.png") at truecenter
    "쉬었다\n"
    extend "체력 +20, 과 -5, 동아리 -5"

    python :
        hp += 20
        gwa_parameter -= 5
        club_parameter -= 5

    call parameter_maxmin_check

    return
