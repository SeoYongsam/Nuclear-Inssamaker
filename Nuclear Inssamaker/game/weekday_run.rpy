<<<<<<< HEAD
=======

<<<<<<< HEAD
    $ day = 1
    while day < 7:
        call weekday_day
        call weekday_evening
        call weekday_SNS

        $ day += 1
=======
    call weekday_day
    call weekday_evening
    call weekday_SNS

    return

>>>>>>> c2d9b47a4ef56f8dd4b1d37a45ac13904676b98a
label weekday_day :
    $ YoIl = day_name[day]

    #낮 일정 소화
    scene bg lecture_room with dissolve
    "[YoIl] 낮, 강의실에서 수업을 들었다."

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
    "[YoIl] 저녁이 되었다.\n"
>>>>>>> f0a093a49f5e48ae089e2e04dedbc2a2e8783b98

    if day_schedule[((week - 1) * 7 + day) % 28] == 1:
        call evening_study
    elif day_schedule[((week - 1) * 7 + day) % 28] == 2:
        call evening_club
    elif day_schedule[((week - 1) * 7 + day) % 28] == 3:
        call evening_gwa
    elif day_schedule[((week - 1) * 7 + day) % 28] == 4:
        call evening_rest
    else :
        extend "에러"
    window hide
    pause

    jump weekday_SNS

    return

label weekday_SNS :
    #밤 일정 소화
    scene black
    "[YoIl] 밤, SNS를 확인했다."
    show phone_night at truecenter
    pause

    if day < 6 :
        $ day += 1
        jump weekday_day
    else :
        "일요일 화면으로 돌아갑니다."
        call weekday_schedule_reset
        jump sunday_room
    return

<<<<<<< HEAD
label weekday_day :
    $ YoIl = day_name[day]

    #낮 일정 소화
    scene bg lecture_room with dissolve
    "[YoIl] 낮, 강의실에서 수업을 들었다."

    $ j = renpy.random.randint(1,3)
    if j == 1:
        call lecture_sleep
    else :
        call lecture

    scene black

    return

label weekday_evening :
    #저녁 일정 소화
    scene black
    "[YoIl] 저녁이 되었다.\n"

    if day_schedule[((week - 1) * 7 + day) % 28] == 1:
        call evening_study
    elif day_schedule[((week - 1) * 7 + day) % 28] == 2:
        call evening_club
    elif day_schedule[((week - 1) * 7 + day) % 28] == 3:
        call evening_gwa
    elif day_schedule[((week - 1) * 7 + day) % 28] == 4:
        call evening_rest
    else :
        extend "에러"
    window hide
    pause
    return

label weekday_SNS :
    #밤 일정 소화
    scene black
    "[YoIl] 밤, SNS를 확인했다."
    show phone_night at truecenter
    pause

    return

=======
>>>>>>> f0a093a49f5e48ae089e2e04dedbc2a2e8783b98
label weekday_schedule_reset :
#    $ i = 1
#    while i < 7:
#        $ day_schedule[i] = 0
#        $ i += 1
    if ((week - 1) * 7 + day) % 28 == 0:
        $ i = 1
        while i < 28:
            $ day_schedule[i] = 0
            $ i += 1

    $ day = 1
    $ week += 1
    $ for_day_schedule_select = 0

    scene black with dissolve
    pause
    return

label evening_study:
    $ rand = renpy.random.randint(1, 8)
    #$ renpy.scene()
    #$ renpy.show("study/%d.jpg" %rand)
    show expression ("study/%d.jpg" %rand) at truecenter
    return

label evening_club:
    $ rand = renpy.random.randint(1, 7)
    show expression ("club/%d.jpg" %rand) at truecenter
    return

label evening_gwa:
    $ rand = renpy.random.randint(1, 6)
    show expression ("gwa/%d.jpg" %rand) at truecenter
    return

label evening_rest:
    $ rand = renpy.random.randint(1, 6)
    show expression ("rest/%d.jpg" %rand) at truecenter
    return
