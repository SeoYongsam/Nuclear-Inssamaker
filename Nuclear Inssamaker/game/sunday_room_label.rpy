# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#start 함수에서 넘어옴
label sunday_room:
    scene sunday_room_image at truecenter

    show screen sunday_room_UI
    # sunday_room_screen에 있는 핸드폰, 플래너 아이콘을 보여주는 스크린
    show screen phone_icon
    show screen planner_icon

    show screen hp_show

#    "일요일이 되었습니다.\n"
#    extend "핸드폰을 이용해 SNS를 확인하거나,\n"
#    extend "플래너를 이용해 다음주 일정을 짜세요."
    while True :
        window hide
        pause

    return

label planner:
    call show_planner
    show screen stats_screen
    call planner_icon_select

    # 토요일까지 선택을 완료하고 day가 7이 되면,
    if day == 7:
        hide screen schedule_highlight
        "일주일 일정을 실행하시겠습니까?"
        menu:
            "실행한다":
                $ day = 1
                call hide_planner_button
                hide screen sunday_room_UI

                $ renpy.transition(dissolve)
                show screen dateShow
                jump weekday_day

            "처음부터":
                $ day = 1
                $ i = 1
                while i < 7:
                    $ day_schedule[month - 3][(week - 1) * 7 + i] = 0
                    $ i += 1

    # 버튼 만악의 근원
    while True:
        window hide
        pause

    return

label show_planner :
    # 플래너 배경 ON
    show screen planner_UI

    hide screen sunday_room_UI
    show screen sunday_room_UI
    hide screen hp_show
    show screen hp_show

    if month - 3 == month_for_display :
        # 형광색 하이라이트 창
        show screen schedule_highlight

        # 오른쪽 스케줄 창
        show screen schedule_button


    # 스케줄러 속 월화수목금토 '공부'~'휴식' 아이콘 띄우기
    show screen month_schedule_icon_show

#    show screen second_month_schedule_icon_show

#    show screen third_month_schedule_icon_show

#    show screen fourth_month_schedule_icon_show
#    # 그 위에 투명한 수정 버튼
#    show screen schedule_revise_button


    return

label planner_icon_select :
    if day != 7:
        $ day_schedule[month - 3][(week - 1) * 7 + day] = for_day_schedule_select
        $ for_day_schedule_select = 0

    # day_schedule[day]가 선택되어 있다면, day를 늘려 다음 날로 넘어간다.
        while day_schedule[month - 3][(week - 1) * 7 + day] != 0:
#    if for_day_schedule_select != 0:
            $ day += 1
    return

label return_to_sunday_room :
    call hide_planner_button
    $ for_day_schedule_select = 0
    jump sunday_room

    return


label hide_planner_button :
    hide planner_background

    hide screen hp_show

    hide screen planner_UI
    hide screen schedule_button
    hide screen schedule_highlight

    hide screen month_schedule_icon_show

    return

label show_previous_month :
    if month_for_display > 0 and month_for_display <= 3 :
        $ month_for_display -= 1

        if month - 3 != month_for_display :
            hide screen schedule_highlight
            hide screen schedule_button

        else :
            show screen schedule_highlight
            show screen schedule_button            
    return

label show_next_month :
    if month_for_display >= 0 and month_for_display < 3 :
        $ month_for_display += 1

        if month - 3 != month_for_display :
            hide screen schedule_highlight
            hide screen schedule_button

        else :
            show screen schedule_highlight
            show screen schedule_button
    return

#label button_reset(number) :
#    if day_schedule[number] != 0:
#        $ day_schedule[number] = 0
#        $ day = number
##    while day_schedule[day]
##    if day_schedule[day] != 0
##        $ day += 1
#    return

label phone:
    hide screen phone_icon
    hide screen planner_icon
    "핸드폰 화면이 구현되지 않았습니다."
    "일요일 화면으로 돌아갑니다"

    jump sunday_room
    return
