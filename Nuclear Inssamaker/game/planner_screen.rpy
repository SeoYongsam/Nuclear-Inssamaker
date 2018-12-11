image sel_study = im.Alpha("planner/sel_study.png",0.7)
image sel_club = im.Alpha("planner/sel_club.png",0.7)
image sel_gwa = im.Alpha("planner/sel_gwa.png",0.7)
image sel_rest = im.Alpha("planner/sel_rest.png",0.7)

screen planner_UI() :
    add Solid("#000c")
    add "planner/planner_background.png"
    if month == month_for_display + 3 :
        add "planner/planner_schedule_list.png"

    # 달력 상단 중앙 3~6월
    vbox xpos 448 ypos 81 :
        if month_for_display == 0 :
            add "planner/month3.png"
        elif month_for_display == 1 :
            add "planner/month4.png"
        elif month_for_display == 2 :
            add "planner/month5.png"
        else :
            add "planner/month6.png"

    #플래너 이전 달로 가는 화살표
    vbox xpos 372 ypos 88 :
        imagebutton :
            idle "planner/arrow_left.png"
            hover "planner/arrow_left_on.png"
            action Call("show_previous_month")

    #플래너 다음 달로 가는 화살표
    vbox xpos 564 ypos 88 :
        imagebutton :
            idle "planner/arrow_right.png"
            hover "planner/arrow_right_on.png"
            action Call("show_next_month")

    #플래너 종료창
    vbox xpos 896 ypos 72 :
        imagebutton :
            idle "planner/exitButton.png"
            hover "planner/exitButton_on.png"
            #플래너 X버튼 누르면 플래너 화면들을 전부 숨기고, 일요일 방으로 간다.
            action Jump("planner_close")
            #아래 코드는 위와 똑같지만 작동하지 않는 코드. Call이 호출되면 뒷 액션들은 호출되지 않는 것 같다.
            #action Call("hide_planner_button"), Jump("sunday_room")

## 스케줄러에서 선택화면이 나타나는 노란색 테두리 하이라이트 화면
screen schedule_highlight():
    if day <= 6:
        vbox:
            xpos (160 + 128*(day-1) - 4) ypos (175 + 128* (week-1) - 4)
            add "planner/highlight.png"

    elif day == 7 :
        vbox:
            xpos (160 + 128 * 5 - 4) ypos (175 + 128* (week-1) - 4 )
            add "planner/highlight.png"

## 플래너를 눌렀을 때 나오는 일정짜기 버튼
screen schedule_button():
        vbox:
            xpos 968 ypos 424
            spacing 4
#            xalign 0.5

            imagebutton :
                idle "planner/button_study.png"
                hover "planner/button_study_on.png"
                action SetVariable("for_day_schedule_select", 1), Jump("planner")

            imagebutton :
                idle "planner/button_gwa.png"
                hover "planner/button_gwa_on.png"
                action SetVariable("for_day_schedule_select", 3), Jump("planner")

            imagebutton :
                if month != 3 or week > 2 :
                    idle "planner/button_club.png"
                    hover "planner/button_club_on.png"
                    action SetVariable("for_day_schedule_select", 2), Jump("planner")
                else :
                    idle im.Alpha("planner/button_club.png", 0.2)
                    hover im.Alpha("planner/button_club.png", 0.2)
                    action NullAction

            imagebutton :
                idle "planner/button_rest.png"
                hover "planner/button_rest_on.png"
                action SetVariable("for_day_schedule_select", 4), Jump("planner")

screen month_schedule_icon_show():
    # 플래너 밑줄
    if month == month_for_display + 3 :
        for i in range(1, 6) :
            hbox :
                if i >= day :
                    xpos 160 + 128*(i-1) + 20 ypos 175 + 128*(week-1) + 104
                    add "planner/underline.png"
        if 6 >= day :
            add "planner/underline.png" xpos 160 + 128*5 + 20 ypos 175 + 128*(week-1) + 67
        if 7 >= day :
            add "planner/underline.png" xpos 160 + 128*5 + 20 ypos 175 + 128*(week-1) + 104

    for i in range(1, 5) :
        for j in range(1, 6) :
        # 월요일
            if day_schedule[month_for_display][(i-1)*8 + j] != 0:
                hbox:
                    xpos 160 + 128*(j-1) + 15 ypos 175 + 128*(i-1) + 97
                    if day_schedule[month_for_display][(i-1)*8 + j] == 1:
                        add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 2:
                        add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 3:
                        add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 4:
                        add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

        vbox:
            xpos 160 + 128*5 + 12 ypos 175 + 128*(i-1) + 60
            if day_schedule[month_for_display][(i-1)*8 + 6] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            null height 15

            if day_schedule[month_for_display][(i-1)*8 + 7] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

#screen schedule_revise_button():
#    hbox:
#        xpos 160 ypos 180
#        spacing -4
#        imagebutton :
#            idle im.Alpha("sel_study.png",0)
#            hover im.Alpha("sel_study.png",0)
#            action Call("button_reset", number = 1)
#
#        imagebutton :
#            idle im.Alpha("sel_study.png",0)
#            hover im.Alpha("sel_study.png",0)
#            action Call("button_reset", number = 2)
#
#        imagebutton :
#            idle im.Alpha("sel_study.png",0)
#            hover im.Alpha("sel_study.png",0)
#            action Call("button_reset", number = 3)
#
#        imagebutton :
#            idle im.Alpha("sel_study.png",0)
#            hover im.Alpha("sel_study.png",0)
#            action Call("button_reset", number = 4)
#
#        imagebutton :
#            idle im.Alpha("sel_study.png",0)
#            hover im.Alpha("sel_study.png",0)
#            action Call("button_reset", number = 5)
#
#        imagebutton :
#            idle im.Alpha("sel_study.png",0)
#            hover im.Alpha("sel_study.png",0)
#            action Call("button_reset", number = 6)
