image planner_background = "planner_background.png"
image planner_schedule_list = "planner_schedule_list.png"
#image highlight = im.Scale("highlight.png",100,100)
image highlight = "highlight.png"

image sel_study = im.Alpha("sel_study.png",0.3)
image sel_club = "sel_club.png"
image sel_gwa = "sel_gwa.png"
image sel_rest = "sel_rest.png"

## 일요일 방에서 핸드폰 아이콘
screen phone_icon():
    vbox :
        xalign 0.34 yalign 0.7
        imagebutton:
            idle "phone_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("phone_icon.png",2)
            # 클릭시 phone label을 실행함
            action Jump("phone")

## 일요일 방에서 플래너 아이콘
screen planner_icon() :
    vbox xalign 0.64 yalign 0.7 :
        imagebutton:
            idle "planner_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("planner_icon.png",2)
            # 클릭시 planner label을 실행함
            action Hide("phone_icon"), Hide("planner_icon"), Show("hp_show"), Jump("planner")

screen hp_show():
#    frame:
#        align(0.05,0.05)
    hbox:
        xpos 972 ypos 300 # 멘탈박스는 344
        #align (0.05, 0.05) # 박스 위치, 화면에서 가로방향으로 0.95, 세로방향으로 0.05 비율 되는 곳에 존재

        # horizon box 각 요소별 스페이싱 10씩
        spacing 10

 #       text "HP" style "button_text" yalign 0.5

        # 화면 상단 HP 버튼을 누르면 체력이 10씩 증가
#        textbutton "HP" :
#            yalign 0.5
#            text_color "#f00"
#            text_hover_color "#ff0"
#            action SetVariable("hp", hp + 10)

        # 체력바
        bar value AnimatedValue(hp, 100, 1.0) :
            left_bar color("#008000")
            right_bar color("#008000",alpha = 0.2)
            yalign 0.5
            xsize 288
            ysize 24

# 일요일 방 hp, mental, to-do-list 바
screen sunday_room_UI() :
    ## 일단 여기다가 background 때려 박았음"
    add "hp_background.png"
    add "mental_background.png"
    add "to_do_list.png"
    ##

screen planner_UI() :
    add Solid("#000c")
    add "planner_background.png"
    add "planner_schedule_list"

## 스케줄러에서 선택화면이 나타나는 노란색 테두리 하이라이트 화면
screen schedule_highlight():
    if day < 7:
        vbox:
            xpos (32 + 128*(day-1)) ypos (180 + 128* ((week-1)%4) )
            add "highlight"

## 플래너를 눌렀을 때 나오는 일정짜기 버튼
screen schedule_button():
    frame:
        xpos 986 ypos 450
        xsize 260
        vbox:
            spacing 10
            xalign 0.5

            textbutton "공부하기":
                action SetVariable("for_day_schedule_select", 1)

            textbutton "동아리":
                action SetVariable("for_day_schedule_select", 2)
#                action Notify("동아리 활동했다")

            textbutton "과활동":
                action SetVariable("for_day_schedule_select", 3)
#                action Notify("과활동했다")

            textbutton "휴식":
                action SetVariable("for_day_schedule_select", 4)
#                action Notify("쉬었다")

            textbutton "뒤로가기":
#               $ for_day_schedule_select = 5
                action SetVariable("for_day_schedule_select", 5)
#                action Jump("sunday_room")
#                action SetVariable("for_day_schedule_select", 5), Jump("sunday_room")

#                action Function(renpy.call, "hide_planner_button"), Jump("sunday_room")
                #text_align 0.5

screen week_schedule_icon_show():
    # 월요일
    if day_schedule[1] != 0:
        hbox:
            xpos 32 ypos 180
            if day_schedule[1] == 1:
                add "sel_study"

            elif day_schedule[1] == 2:
                add "sel_club"

            elif day_schedule[1] == 3:
                add "sel_gwa"

            elif day_schedule[1] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[2] != 0:
        hbox:
            xpos 160 ypos 180
            if day_schedule[2] == 1:
                add "sel_study"

            elif day_schedule[2] == 2:
                add "sel_club"

            elif day_schedule[2] == 3:
                add "sel_gwa"

            elif day_schedule[2] == 4:
                add "sel_rest"

    if day_schedule[3] != 0:
        hbox:
            xpos 288 ypos 180
            if day_schedule[3] == 1:
                add "sel_study"

            elif day_schedule[3] == 2:
                add "sel_club"

            elif day_schedule[3] == 3:
                add "sel_gwa"

            elif day_schedule[3] == 4:
                add "sel_rest"

    if day_schedule[4] != 0:
        hbox:
            xpos 416 ypos 180
            if day_schedule[4] == 1:
                add "sel_study"

            elif day_schedule[4] == 2:
                add "sel_club"

            elif day_schedule[4] == 3:
                add "sel_gwa"

            elif day_schedule[4] == 4:
                add "sel_rest"

    if day_schedule[5] != 0:
        hbox:
            xpos 544 ypos 180
            if day_schedule[5] == 1:
                add "sel_study"

            elif day_schedule[5] == 2:
                add "sel_club"

            elif day_schedule[5] == 3:
                add "sel_gwa"

            elif day_schedule[5] == 4:
                add "sel_rest"

    if day_schedule[6] != 0:
        hbox:
            xpos 672 ypos 180
            if day_schedule[6] == 1:
                add "sel_study"

            elif day_schedule[6] == 2:
                add "sel_club"

            elif day_schedule[6] == 3:
                add "sel_gwa"

            elif day_schedule[6] == 4:
                add "sel_rest"

#2주차
    if day_schedule[8] != 0:
        hbox:
            xpos 32 ypos 308
            if day_schedule[8] == 1:
                add "sel_study"

            elif day_schedule[8] == 2:
                add "sel_club"

            elif day_schedule[8] == 3:
                add "sel_gwa"

            elif day_schedule[8] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[9] != 0:
        hbox:
            xpos 160 ypos 308
            if day_schedule[9] == 1:
                add "sel_study"

            elif day_schedule[9] == 2:
                add "sel_club"

            elif day_schedule[9] == 3:
                add "sel_gwa"

            elif day_schedule[9] == 4:
                add "sel_rest"

    if day_schedule[10] != 0:
        hbox:
            xpos 288 ypos 308
            if day_schedule[10] == 1:
                add "sel_study"

            elif day_schedule[10] == 2:
                add "sel_club"

            elif day_schedule[10] == 3:
                add "sel_gwa"

            elif day_schedule[10] == 4:
                add "sel_rest"

    if day_schedule[11] != 0:
        hbox:
            xpos 416 ypos 308
            if day_schedule[11] == 1:
                add "sel_study"

            elif day_schedule[11] == 2:
                add "sel_club"

            elif day_schedule[11] == 3:
                add "sel_gwa"

            elif day_schedule[11] == 4:
                add "sel_rest"

    if day_schedule[12] != 0:
        hbox:
            xpos 544 ypos 308
            if day_schedule[12] == 1:
                add "sel_study"

            elif day_schedule[12] == 2:
                add "sel_club"

            elif day_schedule[12] == 3:
                add "sel_gwa"

            elif day_schedule[12] == 4:
                add "sel_rest"

    if day_schedule[13] != 0:
        hbox:
            xpos 672 ypos 308
            if day_schedule[13] == 1:
                add "sel_study"

            elif day_schedule[13] == 2:
                add "sel_club"

            elif day_schedule[13] == 3:
                add "sel_gwa"

            elif day_schedule[13] == 4:
                add "sel_rest"

#3주차
    if day_schedule[15] != 0:
        hbox:
            xpos 32 ypos 436
            if day_schedule[15] == 1:
                add "sel_study"

            elif day_schedule[15] == 2:
                add "sel_club"

            elif day_schedule[15] == 3:
                add "sel_gwa"

            elif day_schedule[15] == 4:
                add "sel_rest"

    if day_schedule[16] != 0:
        hbox:
            xpos 160 ypos 436
            if day_schedule[16] == 1:
                add "sel_study"

            elif day_schedule[16] == 2:
                add "sel_club"

            elif day_schedule[16] == 3:
                add "sel_gwa"

            elif day_schedule[16] == 4:
                add "sel_rest"

    if day_schedule[17] != 0:
        hbox:
            xpos 288 ypos 436
            if day_schedule[17] == 1:
                add "sel_study"

            elif day_schedule[17] == 2:
                add "sel_club"

            elif day_schedule[17] == 3:
                add "sel_gwa"

            elif day_schedule[17] == 4:
                add "sel_rest"

    if day_schedule[18] != 0:
        hbox:
            xpos 416 ypos 436
            if day_schedule[18] == 1:
                add "sel_study"

            elif day_schedule[18] == 2:
                add "sel_club"

            elif day_schedule[18] == 3:
                add "sel_gwa"

            elif day_schedule[18] == 4:
                add "sel_rest"

    if day_schedule[19] != 0:
        hbox:
            xpos 544 ypos 436
            if day_schedule[19] == 1:
                add "sel_study"

            elif day_schedule[19] == 2:
                add "sel_club"

            elif day_schedule[19] == 3:
                add "sel_gwa"

            elif day_schedule[19] == 4:
                add "sel_rest"

    if day_schedule[20] != 0:
        hbox:
            xpos 672 ypos 436
            if day_schedule[20] == 1:
                add "sel_study"

            elif day_schedule[20] == 2:
                add "sel_club"

            elif day_schedule[20] == 3:
                add "sel_gwa"

            elif day_schedule[20] == 4:
                add "sel_rest"

#4주차
    if day_schedule[22] != 0:
        hbox:
            xpos 32 ypos 564
            if day_schedule[22] == 1:
                add "sel_study"

            elif day_schedule[22] == 2:
                add "sel_club"

            elif day_schedule[22] == 3:
                add "sel_gwa"

            elif day_schedule[22] == 4:
                add "sel_rest"

    if day_schedule[23] != 0:
        hbox:
            xpos 160 ypos 564
            if day_schedule[23] == 1:
                add "sel_study"

            elif day_schedule[23] == 2:
                add "sel_club"

            elif day_schedule[23] == 3:
                add "sel_gwa"

            elif day_schedule[23] == 4:
                add "sel_rest"

    if day_schedule[24] != 0:
        hbox:
            xpos 288 ypos 564
            if day_schedule[24] == 1:
                add "sel_study"

            elif day_schedule[24] == 2:
                add "sel_club"

            elif day_schedule[24] == 3:
                add "sel_gwa"

            elif day_schedule[24] == 4:
                add "sel_rest"

    if day_schedule[25] != 0:
        hbox:
            xpos 416 ypos 564
            if day_schedule[25] == 1:
                add "sel_study"

            elif day_schedule[25] == 2:
                add "sel_club"

            elif day_schedule[25] == 3:
                add "sel_gwa"

            elif day_schedule[25] == 4:
                add "sel_rest"

    if day_schedule[26] != 0:
        hbox:
            xpos 544 ypos 564
            if day_schedule[26] == 1:
                add "sel_study"

            elif day_schedule[26] == 2:
                add "sel_club"

            elif day_schedule[26] == 3:
                add "sel_gwa"

            elif day_schedule[26] == 4:
                add "sel_rest"

    if day_schedule[27] != 0:
        hbox:
            xpos 672 ypos 564
            if day_schedule[27] == 1:
                add "sel_study"

            elif day_schedule[27] == 2:
                add "sel_club"

            elif day_schedule[27] == 3:
                add "sel_gwa"

            elif day_schedule[27] == 4:
                add "sel_rest"


#screen schedule_revise_button():
#    hbox:
#        xpos 32 ypos 180
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
