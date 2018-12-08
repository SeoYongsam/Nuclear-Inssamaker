image bg lecture_room = "lecture_room.png"

label weekday_day :
    scene black #with dissolve
    show screen stats_screen

    show screen phone_icon with vpunch

    $ YoIl = day_name[day]
    $ day_for_show = (week-1)*8 + day + 1

    if day < 8 :
        $ day_or_evening = "day"
        call weekday_day_event

    if hp <= 30 :
        if hp == 0 :
            call hp_0_break_event
        else :
            call hp_low_rest_event

    if mental_point == 100 :
        call mental_point_100_event

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

label mental_point_100_event :
    return

label weekday_evening :
    #저녁 일정 소화
    if day != 6 :
        $ day_or_evening = "evening"
        scene black
        "[YoIl]요일 저녁이 되었다.\n"
        call weekday_evening_event

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

    #window hide
    #pause

    jump weekday_SNS

    return

label weekday_SNS :
    #밤 일정 소화 #임시 주석처리
#    scene black
#    "[YoIl]요일 밤, SNS를 확인했다."
#    show phone_night at truecenter

#    scene black with vpunch

    $ random.shuffle(rand_list_for_katlk_list)
    call change_fbook_post
    call change_group_talk
    call change_jangjung_talk
    call change_jinil_talk
    call change_samyong_talk
    call change_dongah_talk

    pause


    # 일주일 일정 반복. 다 소화하면, 일주일 스케줄 리셋하고 일요일로 감
    if day < 7 :
        $ day += 1
        jump weekday_day
    else :
        "일요일 화면으로 돌아갑니다. 체력을 20 회복합니다."
        call weekday_schedule_reset
        $ hp += 20
        $ mental_point -= 5
        call parameter_maxmin_check

        jump sunday_room
    return

label weekday_schedule_reset :
    if (week - 1) * 8 + day + 1 == 32:
        $ month += 1
        "[month]월이 되었습니다."
        $ week = 1
    else :
        $ week += 1
    $ day = 0

    $ random.shuffle(rand_list_for_katlk_list)
    call change_fbook_post
    call change_group_talk
    call change_jangjung_talk
    call change_jinil_talk
    call change_samyong_talk
    call change_dongah_talk

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
