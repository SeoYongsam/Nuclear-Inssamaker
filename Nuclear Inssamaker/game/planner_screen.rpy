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
                if day <= 7 :
                    action SetVariable("for_day_schedule_select", 1), SetVariable("hp_for_show", hp_for_show-15), SetVariable("mental_point_for_show", mental_point_for_show-15), Jump("planner")
                #else :
                #    action Null

            imagebutton :
                idle "planner/button_gwa.png"
                hover "planner/button_gwa_on.png"
                if day <= 7 :
                    action SetVariable("for_day_schedule_select", 3), SetVariable("hp_for_show", hp_for_show-20), SetVariable("mental_point_for_show", mental_point_for_show-5), Jump("planner")

            imagebutton :
                # if month != 3 or week > 2 :
                if club_open == True :
                    idle "planner/button_club.png"
                    hover "planner/button_club_on.png"
                    if day <= 7 :
                        if day != 4 :
                            action SetVariable("for_day_schedule_select", 2), SetVariable("hp_for_show", hp_for_show-25), SetVariable("mental_point_for_show", mental_point_for_show+20), Jump("planner")
                        else :
                            if club_count < 10 :
                                action SetVariable("for_day_schedule_select", 2), SetVariable("hp_for_show", hp_for_show-25), SetVariable("mental_point_for_show", mental_point_for_show+10), Jump("planner")
                            elif club_count < 20 :
                                action SetVariable("for_day_schedule_select", 2), SetVariable("hp_for_show", hp_for_show-20), SetVariable("mental_point_for_show", mental_point_for_show+20), Jump("planner")
                            else :
                                action SetVariable("for_day_schedule_select", 2), SetVariable("hp_for_show", hp_for_show+15), SetVariable("mental_point_for_show", mental_point_for_show+30), Jump("planner")

                else :
                    idle im.Alpha("planner/button_club.png", 0.2)
                    hover im.Alpha("planner/button_club.png", 0.2)
                    action NullAction

            imagebutton :
                idle "planner/button_rest.png"
                hover "planner/button_rest_on.png"
                if day <= 7 :
                    action SetVariable("for_day_schedule_select", 4), SetVariable("hp_for_show", hp_for_show+50), SetVariable("mental_point_for_show", mental_point_for_show+30), Jump("planner")

screen month_schedule_icon_show():
    if month == month_for_display + 3 :
        text "{color=#DC143C}Today!{/color}" xpos 160 - 128 + 12 ypos 175 + 128*(week-1) + 30

        for i in range(1, 6) :
            hbox :
                if i >= day and day_schedule[month - 3][(week - 1) * 8 + i] == 0:
                    xpos 160 + 128*(i-1) + 20 ypos 175 + 128*(week-1) + 104
                    add "planner/underline.png"
        if 6 >= day and day_schedule[month - 3][(week - 1) * 8 + 6] == 0:
            add "planner/underline.png" xpos 160 + 128*5 + 20 ypos 175 + 128*(week-1) + 67
        if 7 >= day and day_schedule[month - 3][(week - 1) * 8 + 7] == 0:
            add "planner/underline.png" xpos 160 + 128*5 + 20 ypos 175 + 128*(week-1) + 104

    for i in range(1, 5) :
        for j in range(1, 6) :
            if day_schedule[month_for_display][(i-1)*8 + j] != 0:
                hbox:
                    xpos 160 + 128*(j-1) + 15 ypos 175 + 128*(i-1) + 97
                    if day_schedule[month_for_display][(i-1)*8 + j] == 1:
                        if (month_for_display == 1 and i == 3 and j >= 5) or (month_for_display == 1 and i == 4 and j <= 4) or (month_for_display == 3 and i == 2 and j >= 4) or (month_for_display == 3 and i == 3 and j <= 3) :
                            add im.Alpha(im.MatrixColor("planner/sel_study_hard.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)
                        else :
                            add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 2:
                        if j != 4 :
                            add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)
                        else :
                            add im.Alpha(im.MatrixColor("planner/sel_club_thur.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 3:
                        add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 4:
                        add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 5:
                         add im.Alpha(im.MatrixColor("planner/sel_event.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 6:
                         add im.Alpha(im.MatrixColor("planner/sel_hospital.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

                    elif day_schedule[month_for_display][(i-1)*8 + j] == 7:
                         add im.Alpha(im.MatrixColor("planner/sel_home.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)


        vbox:
            xpos 160 + 128*5 + 12 ypos 175 + 128*(i-1) + 60
            if day_schedule[month_for_display][(i-1)*8 + 6] == 1:
                if (month_for_display == 1 and i == 3) or (month_for_display == 3 and i == 2) :
                    add im.Alpha(im.MatrixColor("planner/sel_study_hard.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)
                else :
                    add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 5:
                add im.Alpha(im.MatrixColor("planner/sel_event.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 6:
                 add im.Alpha(im.MatrixColor("planner/sel_hospital.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 6] == 7:
                 add im.Alpha(im.MatrixColor("planner/sel_home.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)


            null height 15

            if day_schedule[month_for_display][(i-1)*8 + 7] == 1:
                if (month_for_display == 1 and i == 3) or (month_for_display == 3 and i == 2):
                    add im.Alpha(im.MatrixColor("planner/sel_study_hard.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)
                else :
                    add im.Alpha(im.MatrixColor("planner/sel_study.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 2:
                add im.Alpha(im.MatrixColor("planner/sel_club.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 3:
                add im.Alpha(im.MatrixColor("planner/sel_gwa.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 4:
                add im.Alpha(im.MatrixColor("planner/sel_rest.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 5:
                add im.Alpha(im.MatrixColor("planner/sel_event.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 6:
                 add im.Alpha(im.MatrixColor("planner/sel_hospital.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)

            elif day_schedule[month_for_display][(i-1)*8 + 7] == 7:
                 add im.Alpha(im.MatrixColor("planner/sel_home.png",im.matrix.saturation( 0.1+(( (i/week) * ((month_for_display+3)/month)) ))), 0.8)


    # layer 레이어
    if month_for_display == 0 :
        add "planner/3_quest.png"
        add "planner/3.13-14_MT.png" xpos 0 ypos -9

        if month != 3 or week != 1 :
            add "planner/3.09_dongsoze.png" xpos 0 ypos -9
            add "planner/3.23_quiz.png" xpos 0 ypos -9

        if month != 3 or week > 2 :
            add "planner/3.17-19_gwazam.png" xpos 0 ypos -9

        if gwazam_store == True :
            add "planner/3.18_gwazam_store.png" xpos 0 ypos -12

    elif month_for_display == 1 :
        add "planner/4_midtermexam.png"
        add "planner/4.02_school.png"
        add "planner/4.16_festival.png"

        add "planner/4.06-07_mt.png"
        add "planner/4.27_meeting.png"

    elif month_for_display == 2 :
        add "planner/5.03_market.png"
        add "planner/5.10_hanriver.png"
        add "planner/5.16_garaoke.png"
        add "planner/5.21_olympic.png"

    elif month_for_display == 3 :
        add "planner/6.06_club.png"
        add "planner/6.21_end.png"

#    elif month_for_display == 1 :
#        return

#    elif month_for_display == 2 :
#        return

#    elif month_for_display == 3 :
#        return


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
