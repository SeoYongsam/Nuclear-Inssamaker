label weekday_day :
    scene black #with dissolve
    show screen stats_screen

    show screen phone_icon

    $ YoIl = day_name[day]
    if day < 7 :
        $ day_for_show = (week-1)*7 + day + 1

    if mental_point == 0 :
        call mental_point_0_event

    elif hp <= 50 :
        if hp == 0 :
            call hp_0_break_event
        else :
            call hp_low_rest_event

    elif day < 8 :
        call weekday_day_event

#    $ j = renpy.random.randint(1,3)
#    if j == 1:
#        call lecture_sleep
#    else :
#        call lecture

    scene black

    jump weekday_evening

    return

label hp_0_break_event :
    scene black
    "[YoIl]요일"
    Player "몸이 너무 안좋아 하루동안 병원에 입원했다."
    extend "\n모든 면에서 멍청해진 것 같다."
    $ hp += 80
    $ study_parameter -= 20
    $ gwa_parameter -= 20
    $ club_parameter -= 20
    call parameter_maxmin_check

    jump weekday_SNS
    return

label hp_low_rest_event :
    $ j = renpy.random.randint(1,3)
    if j == 1 :
        show rest at truecenter
        "[YoIl]요일"
        if day < 6 :
            Player "몸이 너무 안좋다. 낮에 수업을 째고 집에서 잤다."
        else :
            Player "몸이 너무 안좋다. 낮에 집에서 잤다."
        $ hp += 40
        $ study_parameter -= 15
        $ gwa_parameter -= 5
        $ club_parameter -= 5
        call parameter_maxmin_check

        jump weekday_evening
    return

label mental_point_0_event :
    scene black
    Player "정신적으로 너무 힘들어서 집에 다녀왔다."
    extend "\n하루 일정을 날리긴 했지만, 멘탈을 좀 회복했다."

    $ mental_point += 40
    $ study_parameter -= 10
    $ gwa_parameter -= 10
    $ club_parameter -= 10
    call parameter_maxmin_check

    return

label weekday_evening :
    #저녁 일정 소화
    if day != 6 :
        scene black
        "[YoIl]요일 저녁이 되었다.\n"
        call weekday_evening_event

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
        "일요일 화면으로 돌아갑니다. 체력을 20 회복합니다.\n멘탈이 5 깎입니다."
        call weekday_schedule_reset
        $ hp += 20
        $ mental_point -= 5
        call parameter_maxmin_check

        jump sunday_room
    return

label weekday_schedule_reset :
    if (week - 1) * 8 + day + 1 == 32:
        "[month]월이 되었습니다."
        $ month += 1
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
