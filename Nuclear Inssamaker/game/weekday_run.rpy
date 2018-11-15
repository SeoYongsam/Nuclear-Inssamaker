image bg lecture_room = "lecture_room.png"

label weekday_day :
    scene black with dissolve
    show screen stats_screen

    $ YoIl = day_name[day]
    $ day_for_show = (week-1)*7 + day + 1

    #낮 일정 소화 #임시 주석처리
    show bg lecture_room at truecenter
    "[YoIl]요일 낮, 강의실에서 수업을 들었다."

    if hp <= 30 :
        if hp == 0 :
            call hp_0_break_event
        else :
            call hp_low_rest_event

    if loneliness == 100 :
        call loneliness_100_event

#    $ j = renpy.random.randint(1,3)
#    if j == 1:
#        call lecture_sleep
#    else :
#        call lecture

    scene black

    jump weekday_evening

    return

label hp_0_break_event :
    return

label hp_low_rest_event :
    return

label loneliness_100_event :
    return

label weekday_evening :
    #저녁 일정 소화
    scene black
    "[YoIl]요일 저녁이 되었다.\n"

    if day_schedule[month - 3][(week - 1) * 7 + day] == 1:
        call evening_study

    elif day_schedule[month - 3][(week - 1) * 7 + day] == 2:
        call evening_club

    elif day_schedule[month - 3][(week - 1) * 7 + day] == 3:
        call evening_gwa

    elif day_schedule[month - 3][(week - 1) * 7 + day] == 4:
        call evening_rest

    else :
        extend "에러"

    #window hide
    #pause

    jump weekday_SNS

    return

label weekday_SNS :
    #밤 일정 소화 #임시 주석처리
#    scene black
#    "[YoIl]요일 밤, SNS를 확인했다."
#    show phone_night at truecenter
#    pause

    if day < 6 :
        $ day += 1
        jump weekday_day
    else :
        "일요일 화면으로 돌아갑니다."
        call weekday_schedule_reset
        $ hp += 30
        $ loneliness += 5

        jump sunday_room
    return

label weekday_schedule_reset :
#    $ i = 1
#    while i < 7:
#        $ day_schedule[0][i] = 0
#        $ i += 1
    if (week - 1) * 7 + day + 1 == 28:
        $ month += 1
        "[month]월이 되었습니다."
        $ week = 1
#        $ i = 1
#        while i < 28:
#            $ day_schedule[0][i] = 0
#            $ i += 1
    else :
        $ week += 1
    $ day = 1
    $ for_day_schedule_select = 0

#    scene black with dissolve
#    pause
    return


label evening_study:
    $ rand = renpy.random.randint(1, 2)
    #$ renpy.scene()
    #$ renpy.show("study/%d.jpg" %rand)
#임시
    show expression ("study/%d.png" %rand) at truecenter
    extend "공부했다\n"
    extend "체력 -5, 외로움 +5, 공부 +10, 과 -5, 동아리 -5"

    python :
        hp -= 5
        loneliness += 5
        study_parameter += 10
        gwa_parameter -= 5
        club_parameter -= 5

    call parameter_maxmin_check

    return

label evening_club:
    $ rand = renpy.random.randint(1, 2)
    show expression ("club/%d.png" %rand) at truecenter
    extend "동아리 활동했다\n"
    extend "체력 -15, 외로움 -10, 공부 -5, 과 -5, 동아리 +15"

    python :
        hp -= 15
        loneliness -= 10
        study_parameter -= 5
        gwa_parameter -= 5
        club_parameter += 15

    call parameter_maxmin_check

    return

label evening_gwa:
#    $ rand = renpy.random.randint(1, 6)
    show expression ("gwa/1.png") at truecenter
    extend "과 활동했다\n"

    extend "체력 -10, 공부 -5, 과 +15, 동아리 -5"

    python :
        hp -= 10
        loneliness -= 0
        study_parameter -= 5
        gwa_parameter += 15
        club_parameter -= 5

    call parameter_maxmin_check

    return

label evening_rest:
#    $ rand = renpy.random.randint(1, 6)
    show expression ("rest/1.png") at truecenter
    extend "쉬었다\n"
    extend "체력 +20, 과 -5, 동아리 -5"

    python :
        hp += 20
        gwa_parameter -= 5
        club_parameter -= 5

    call parameter_maxmin_check

    return
