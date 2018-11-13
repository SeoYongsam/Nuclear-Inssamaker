#image highlight = im.Scale("highlight.png",100,100)

image sel_study = im.Alpha("planner/sel_study.png",0.7)
image sel_club = im.Alpha("planner/sel_club.png",0.7)
image sel_gwa = im.Alpha("planner/sel_gwa.png",0.7)
image sel_rest = im.Alpha("planner/sel_rest.png",0.7)

screen planner_UI() :
    add Solid("#000c")
    add "planner/planner_background.png"
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
            action [Hide("planner_UI"), Hide("schedule_button"),
                    Hide("schedule_highlight"),
                    Hide("month_schedule_icon_show"), Jump("sunday_room")]
            #아래 코드는 위와 똑같지만 작동하지 않는 코드. Call이 호출되면 뒷 액션들은 호출되지 않는 것 같다.
            #action Call("hide_planner_button"), Jump("sunday_room")

## 스케줄러에서 선택화면이 나타나는 노란색 테두리 하이라이트 화면
screen schedule_highlight():
    if day < 7:
        vbox:
            xpos (160 + 128*(day-1)) ypos (184 + 128* (week-1) )
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
                # action Call("button_reset", number = 1)
                action SetVariable("for_day_schedule_select", 1), Jump("planner")

            imagebutton :
                idle "planner/button_gwa.png"
                hover "planner/button_gwa_on.png"
                action SetVariable("for_day_schedule_select", 3), Jump("planner")
#                action Notify("과활동했다")

            imagebutton :
                idle "planner/button_club.png"
                hover "planner/button_club_on.png"
                action SetVariable("for_day_schedule_select", 2), Jump("planner")
#                action Notify("동아리 활동했다")

            imagebutton :
                idle "planner/button_rest.png"
                hover "planner/button_rest_on.png"
                action SetVariable("for_day_schedule_select", 4), Jump("planner")
#                action Notify("쉬었다")

screen month_schedule_icon_show():
    # 월요일
    if day_schedule[month_for_display][1] != 0:
        hbox:
            xpos 160 ypos 184
            if day_schedule[month_for_display][1] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)
#im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+(1/week) * ((month_for_display+3)/month))), 0.8)

            elif day_schedule[month_for_display][1] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][1] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][1] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

    # 화요일
    if day_schedule[month_for_display][2] != 0:
        hbox:
            xpos 288 ypos 184
            if day_schedule[month_for_display][2] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][2] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][2] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][2] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][3] != 0:
        hbox:
            xpos 416 ypos 184
            if day_schedule[month_for_display][3] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][3] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][3] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][3] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][4] != 0:
        hbox:
            xpos 544 ypos 184
            if day_schedule[month_for_display][4] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][4] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][4] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][4] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][5] != 0:
        hbox:
            xpos 672 ypos 184
            if day_schedule[month_for_display][5] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][5] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][5] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][5] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][6] != 0:
        hbox:
            xpos 800 ypos 184
            if day_schedule[month_for_display][6] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][6] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][6] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][6] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((1/week) * ((month_for_display+3)/month)))), 0.8)

#2주차
    if day_schedule[month_for_display][8] != 0:
        hbox:
            xpos 160 ypos 312
            if day_schedule[month_for_display][8] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][8] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][8] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][8] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

    # 화요일
    if day_schedule[month_for_display][9] != 0:
        hbox:
            xpos 288 ypos 312
            if day_schedule[month_for_display][9] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][9] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][9] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][9] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][10] != 0:
        hbox:
            xpos 416 ypos 312
            if day_schedule[month_for_display][10] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][10] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][10] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][10] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][11] != 0:
        hbox:
            xpos 544 ypos 312
            if day_schedule[month_for_display][11] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][11] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][11] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][11] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][12] != 0:
        hbox:
            xpos 672 ypos 312
            if day_schedule[month_for_display][12] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][12] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][12] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][12] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][13] != 0:
        hbox:
            xpos 800 ypos 312
            if day_schedule[month_for_display][13] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][13] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][13] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][13] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((2/week) * ((month_for_display+3)/month)))), 0.8)

#3주차
    if day_schedule[month_for_display][15] != 0:
        hbox:
            xpos 160 ypos 440
            if day_schedule[month_for_display][15] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][15] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][15] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][15] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][16] != 0:
        hbox:
            xpos 288 ypos 440
            if day_schedule[month_for_display][16] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][16] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][16] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][16] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][17] != 0:
        hbox:
            xpos 416 ypos 440
            if day_schedule[month_for_display][17] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][17] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][17] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][17] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][18] != 0:
        hbox:
            xpos 544 ypos 440
            if day_schedule[month_for_display][18] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][18] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][18] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][18] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][19] != 0:
        hbox:
            xpos 672 ypos 440
            if day_schedule[month_for_display][19] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][19] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][19] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][19] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][20] != 0:
        hbox:
            xpos 800 ypos 440
            if day_schedule[month_for_display][20] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][20] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][20] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][20] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((3/week) * ((month_for_display+3)/month)))), 0.8)

#4주차
    if day_schedule[month_for_display][22] != 0:
        hbox:
            xpos 160 ypos 568
            if day_schedule[month_for_display][22] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][22] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][22] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][22] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][23] != 0:
        hbox:
            xpos 288 ypos 568
            if day_schedule[month_for_display][23] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][23] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][23] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][23] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][24] != 0:
        hbox:
            xpos 416 ypos 568
            if day_schedule[month_for_display][24] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][24] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][24] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][24] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][25] != 0:
        hbox:
            xpos 544 ypos 568
            if day_schedule[month_for_display][25] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][25] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][25] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][25] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][26] != 0:
        hbox:
            xpos 672 ypos 568
            if day_schedule[month_for_display][26] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][26] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][26] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][26] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

    if day_schedule[month_for_display][27] != 0:
        hbox:
            xpos 800 ypos 568
            if day_schedule[month_for_display][27] == 1:
                add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][27] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][27] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

            elif day_schedule[month_for_display][27] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.2+((4/week) * ((month_for_display+3)/month)))), 0.8)

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
