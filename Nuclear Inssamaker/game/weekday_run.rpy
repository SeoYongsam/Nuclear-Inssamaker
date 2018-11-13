label weekday_day :
    $ YoIl = day_name[day]

    #낮 일정 소화 #임시 주석처리
#    scene bg lecture_room with dissolve
#    "[YoIl]요일 낮, 강의실에서 수업을 들었다."

#    $ j = renpy.random.randint(1,3)
#    if j == 1:
#        call lecture_sleep
#    else :
#        call lecture

    scene black

    jump weekday_evening

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
    $ rand = renpy.random.randint(1, 8)
    #$ renpy.scene()
    #$ renpy.show("study/%d.jpg" %rand)
#임시
#    show expression ("study/%d.jpg" %rand) at truecenter
    extend "공부했다"
    return

label evening_club:
    $ rand = renpy.random.randint(1, 7)
#    show expression ("club/%d.jpg" %rand) at truecenter
    extend "동아리 활동했다"
    return

label evening_gwa:
    $ rand = renpy.random.randint(1, 6)
#    show expression ("gwa/%d.jpg" %rand) at truecenter
    extend "과 활동했다"
    return

label evening_rest:
    $ rand = renpy.random.randint(1, 6)
#    show expression ("rest/%d.jpg" %rand) at truecenter
    extend "쉬었다"
    return
