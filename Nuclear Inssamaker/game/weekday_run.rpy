image home :
    "home1.png"
    pause 0.3
    "home2.png"
    pause 0.3
    repeat

image hospital :
    "hospital1.png"
    pause 0.3
    "hospital2.png"
    pause 0.3
    repeat

screen weekday_schedule_show :
    hbox :
        xalign 0.5 yalign 0.15
        for i in range (1, 8) :
            vbox :
                if day_schedule[month - 3][(week - 1) * 8 + i] == 1:
                    add "weekday_study.png"

                elif day_schedule[month - 3][(week - 1) * 8 + i] == 2:
                    add "weekday_club.png"

                elif day_schedule[month - 3][(week - 1) * 8 + i] == 3:
                    add "weekday_gwa.png"

                elif day_schedule[month - 3][(week - 1) * 8 + i] == 4:
                    add "weekday_rest.png"

                elif day_schedule[month - 3][(week - 1) * 8 + i] == 5:
                    add "weekday_event.png"

                elif day_schedule[month - 3][(week - 1) * 8 + i] == 6:
                    add "weekday_hospital.png"

                elif day_schedule[month - 3][(week - 1) * 8 + i] == 7:
                    add "weekday_home.png"

                if i == 1 :
                    text "M" xalign 0.5

                elif i == 2 :
                    text "T" xalign 0.5

                elif i == 3 :
                    text "W" xalign 0.5

                elif i == 4 :
                    text "T" xalign 0.5

                elif i == 5 :
                    text "F" xalign 0.5

                elif i == 6 :
                    text "{color=#2CB8D6}S{/color}" xalign 0.5

                elif i == 7 :
                    text "{color=#2F4FF4}S{/color}" xalign 0.5

            if day == i :
                null width -39
                add "weekday_today.png"
                null width -3

            if i != 7 :
                null width 30
            else :
                null width 5

label weekday_day :
    stop music fadeout 1.0
    scene black #with dissolve
    show screen stats_screen

    show screen phone_icon
    show screen weekday_schedule_show

    $ YoIl = day_name[day]
    if day < 7 :
        $ day_for_show = (week-1)*7 + day + 1

    if hp == 0 :
        call hp_0_break_event from _call_hp_0_break_event

    elif mental_point == 0 :
        call mental_point_0_event from _call_mental_point_0_event

#    elif hp <= 50 :
#        if hp == 0 :
#            call hp_0_break_event
#        else :
#            call hp_low_rest_event

    elif day < 8 :
        call weekday_day_event from _call_weekday_day_event

#    $ j = renpy.random.randint(1,3)
#    if j == 1:
#        call lecture_sleep
#    else :
#        call lecture

    scene black

    jump weekday_evening

    return

label hp_0_break_event :
    play sound "sound/hospital.mp3"
    $ day_schedule[month - 3][(week - 1) * 8 + day] = 6

    show hospital at truecenter
    "[YoIl]요일"
    Player "몸이 너무 안좋아 하루동안 병원에 입원했다."
    extend "\n오늘 해야 할 일을 하지 못했다."

    $ hp += 80
    $ study_parameter -= -2
    $ gwa_parameter -= 2
    $ club_parameter -= 2
    call parameter_maxmin_check from _call_parameter_maxmin_check_53

    stop sound fadeout 1.0

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
        $ study_parameter -= 3
        $ gwa_parameter -= 1
        $ club_parameter -= 1
        call parameter_maxmin_check from _call_parameter_maxmin_check_54

        jump weekday_evening
    return

label mental_point_0_event :
    play sound "sound/home.mp3"
    $ day_schedule[month - 3][(week - 1) * 8 + day] = 7

    show home at truecenter
    Player "정신적으로 너무 힘들어서 집에 다녀왔다."
    extend "\n하루 일정을 날리긴 했지만, 멘탈을 좀 회복했다."

    $ mental_point += 40
    $ study_parameter -= 1
    $ gwa_parameter -= 1
    $ club_parameter -= 1
    call parameter_maxmin_check from _call_parameter_maxmin_check_55

    stop sound fadeout 1.0

    jump weekday_SNS
    return

label weekday_evening :
    #저녁 일정 소화
    if day != 6 :
        scene black
        "[YoIl]요일 저녁이 되었다.\n"
        call weekday_evening_event from _call_weekday_evening_event

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

    call change_SNS from _call_change_SNS_5

    pause


    # 일주일 일정 반복. 다 소화하면, 일주일 스케줄 리셋하고 일요일로 감
    if day < 7 :
        $ day += 1
        jump weekday_day
    else :
        "일요일 화면으로 돌아갑니다. 체력을 20 회복합니다."
        call weekday_schedule_reset from _call_weekday_schedule_reset
        $ hp += 20
        call parameter_maxmin_check from _call_parameter_maxmin_check_56

        call event_schedule_set from _call_event_schedule_set_3
        if month == 3 or month == 4 :
            play music "music/sunday_3and4.mp3"
        else :
            play music "music/sunday_5and6.mp3"
        jump sunday_room
    return

label weekday_schedule_reset :
    if (week - 1) * 8 + day + 1 == 32:
        $ tmp = month + 1
        "[tmp]월이 되었습니다."
        $ month += 1
        $ week = 1
    else :
        $ week += 1
    $ day = 0

    call change_SNS from _call_change_SNS_6

    $ for_day_schedule_select = 0

    hide screen weekday_schedule_show

#    scene black with dissolve
#    pause
    return

label change_SNS :
    if grouptalk.new_message_count == 0 :
        $ grouptalk.numerator_length = grouptalk.denominator_length
    if jangjung.new_message_count == 0 :
        $ jangjung.numerator_length = jangjung.denominator_length
    if jinil.new_message_count == 0 :
        $ jinil.numerator_length = jinil.denominator_length
    if samyong.new_message_count == 0 :
        $ samyong.numerator_length = samyong.denominator_length
    if dongah.new_message_count == 0 :
        $ dongah.numerator_length = dongah.denominator_length
    $ random.shuffle(rand_list_for_katlk_list)
    call change_fbook_post from _call_change_fbook_post
    call change_group_talk from _call_change_group_talk
    call change_jangjung_talk from _call_change_jangjung_talk
    call change_jinil_talk from _call_change_jinil_talk
    call change_samyong_talk from _call_change_samyong_talk
    call change_dongah_talk from _call_change_dongah_talk
    # play sound "sound/phone_vibrate.mp3"

    return
