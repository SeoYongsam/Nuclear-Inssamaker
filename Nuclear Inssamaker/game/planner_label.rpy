# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label planner:
    call parameter_maxmin_check
    call show_planner
    call planner_icon_select

    # 토요일까지 선택을 완료하고 day가 7이 되면,
    if day == 8:
        hide screen schedule_highlight
        "일주일 일정을 실행하시겠습니까?"
        menu:
            "실행한다":
                $ day = 1
                call hide_planner_button
                hide screen upper_right_UI

                $ renpy.transition(dissolve)
                show screen dateShow
                show screen upper_right_UI

                jump weekday_day

            "처음부터":
                $ day = 1
                $ hp_for_show = hp
                $ mental_point_for_show = mental_point

                $ i = 1
                while i < 8:
                    $ day_schedule[month - 3][(week - 1) * 8 + i] = 0
                    $ i += 1
                call event_schedule_set


    # 버튼 만악의 근원이었지만 해결함
    while True:
        window hide
        pause

    return

label show_planner :
    # 플래너 배경 ON
    show screen planner_UI

    hide screen upper_right_UI
    show screen upper_right_UI

    # 스케줄러 속 월화수목금토 '공부'~'휴식' 아이콘 띄우기
    show screen month_schedule_icon_show

    if month - 3 == month_for_display :
        # 형광색 하이라이트 창
        show screen schedule_highlight

        # 오른쪽 스케줄 창
        show screen schedule_button

    return

label planner_close :
    hide screen planner_UI
    hide screen schedule_button
    hide screen schedule_highlight
    hide screen month_schedule_icon_show
    $ i = 1
    while i < 8:
        $ day_schedule[month - 3][(week - 1) * 8 + i] = 0
        $ i += 1

    call event_schedule_set

    jump sunday_room
    return

label planner_icon_select :
    if day != 8:
        $ day_schedule[month - 3][(week - 1) * 8 + day] = for_day_schedule_select
        $ for_day_schedule_select = 0

    # day_schedule[day]가 선택되어 있다면, day를 늘려 다음 날로 넘어간다.
        while day_schedule[month - 3][(week - 1) * 8 + day] != 0:
#    if for_day_schedule_select != 0:
            $ day += 1
    return

label hide_planner_button :
    hide screen planner_UI
    hide screen schedule_button
    hide screen schedule_highlight

    hide screen month_schedule_icon_show

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

label event_schedule_set :
    # 3월 이벤트 설정
    if (month-3) * 32 + (week-1)*8 + day >= 8:
        if day_schedule[0][13] <= 5 :
            $ day_schedule[0][13] = 5
        if day_schedule[0][14] <= 5 :
            $ day_schedule[0][14] = 5
        if day_schedule[0][15] <= 5 :
            $ day_schedule[0][15] = 5

    if (month-3) * 32 + (week-1)*8 + day >= 16 :
        if day_schedule[0][18] <= 5 :
            $ day_schedule[0][18] = 5
        if day_schedule[0][20] <= 5 :
            $ day_schedule[0][20] = 5

    if gwazam_store == True :
        if day_schedule[0][19] <= 5 :
            $ day_schedule[0][19] = 5

    # 4월 이벤트 설정
    if (month-3) * 32 + (week-1)*8 + day >= 32 :
        if day_schedule[1][5] <= 5 :
            $ day_schedule[1][5] = 5
        if day_schedule[1][6] <= 5 :
            $ day_schedule[1][6] = 5
        if day_schedule[1][7] <= 5 :
            $ day_schedule[1][7] = 5

    if (month-3) * 32 + (week-1)*8 + day >= 48 :
        if day_schedule[1][17] <= 5 :
            $ day_schedule[1][17] = 5

    # 5월 이벤트 설정
    if (month-3) * 32 + (week-1)*8 + day >= 64 :
        if day_schedule[2][2] <= 5 :
            $ day_schedule[2][2] = 5
    if (month-3) * 32 + (week-1)*8 + day >= 72 :
        if day_schedule[2][10] <= 5 :
            $ day_schedule[2][10] = 5
    if (month-3) * 32 + (week-1)*8 + day >= 80 :
        if day_schedule[2][22] <= 5 :
            $ day_schedule[2][22] = 5
        if day_schedule[2][23] <= 5 :
            $ day_schedule[2][23] = 5
    return
