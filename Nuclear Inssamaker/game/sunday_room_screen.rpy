image planner_background = "planner_background.png"
image planner_schedule_list = "planner_schedule_list.png"
#image highlight = im.Scale("highlight.png",100,100)
image highlight = "highlight.png"

image sel_study = im.Alpha("sel_study.png",0.7)
image sel_club = im.Alpha("sel_club.png",0.7)
image sel_gwa = im.Alpha("sel_gwa.png",0.7)
image sel_rest = im.Alpha("sel_rest.png",0.7)

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
            action Hide("phone_icon"), Hide("planner_icon"), Hide("dateShow"), Show("hp_show"), Jump("planner")

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
            xsize 416
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

    # 달력 상단 중앙 3~6월
    vbox xpos 448 ypos 81 :
        if month == 3 :
            add "month3.png"
        elif month == 4 :
            add "month4.png"
        elif month == 5 :
            add "month5.png"
        else :
            add "month6.png"

    vbox xpos 896 ypos 72 :
        imagebutton :
            idle "exitButton.png"
            hover "exitButton_on.png"
            action Jump("return_to_sunday_room")

## 스케줄러에서 선택화면이 나타나는 노란색 테두리 하이라이트 화면
screen schedule_highlight():
    if day < 7:
        vbox:
            xpos (160 + 128*(day-1)) ypos (184 + 128* (week-1) )
            add "highlight"

## 플래너를 눌렀을 때 나오는 일정짜기 버튼
screen schedule_button():
        vbox:
            xpos 968 ypos 424
            spacing 4
#            xalign 0.5

            imagebutton :
                idle "button_study.png"
                hover "button_study_on.png"
                # action Call("button_reset", number = 1)
                action SetVariable("for_day_schedule_select", 1), Jump("planner")

            imagebutton :
                idle "button_gwa.png"
                hover "button_gwa_on.png"
                action SetVariable("for_day_schedule_select", 3), Jump("planner")
#                action Notify("과활동했다")

            imagebutton :
                idle "button_club.png"
                hover "button_club_on.png"
                action SetVariable("for_day_schedule_select", 2), Jump("planner")
#                action Notify("동아리 활동했다")

            imagebutton :
                idle "button_rest.png"
                hover "button_rest_on.png"
                action SetVariable("for_day_schedule_select", 4), Jump("planner")
#                action Notify("쉬었다")

screen first_month_schedule_icon_show():
    # 월요일
    if day_schedule[0][1] != 0:
        hbox:
            xpos 160 ypos 184
            if day_schedule[0][1] == 1:
                add "sel_study"

            elif day_schedule[0][1] == 2:
                add "sel_club"

            elif day_schedule[0][1] == 3:
                add "sel_gwa"

            elif day_schedule[0][1] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[0][2] != 0:
        hbox:
            xpos 288 ypos 184
            if day_schedule[0][2] == 1:
                add "sel_study"

            elif day_schedule[0][2] == 2:
                add "sel_club"

            elif day_schedule[0][2] == 3:
                add "sel_gwa"

            elif day_schedule[0][2] == 4:
                add "sel_rest"

    if day_schedule[0][3] != 0:
        hbox:
            xpos 416 ypos 184
            if day_schedule[0][3] == 1:
                add "sel_study"

            elif day_schedule[0][3] == 2:
                add "sel_club"

            elif day_schedule[0][3] == 3:
                add "sel_gwa"

            elif day_schedule[0][3] == 4:
                add "sel_rest"

    if day_schedule[0][4] != 0:
        hbox:
            xpos 544 ypos 184
            if day_schedule[0][4] == 1:
                add "sel_study"

            elif day_schedule[0][4] == 2:
                add "sel_club"

            elif day_schedule[0][4] == 3:
                add "sel_gwa"

            elif day_schedule[0][4] == 4:
                add "sel_rest"

    if day_schedule[0][5] != 0:
        hbox:
            xpos 672 ypos 184
            if day_schedule[0][5] == 1:
                add "sel_study"

            elif day_schedule[0][5] == 2:
                add "sel_club"

            elif day_schedule[0][5] == 3:
                add "sel_gwa"

            elif day_schedule[0][5] == 4:
                add "sel_rest"

    if day_schedule[0][6] != 0:
        hbox:
            xpos 800 ypos 184
            if day_schedule[0][6] == 1:
                add "sel_study"

            elif day_schedule[0][6] == 2:
                add "sel_club"

            elif day_schedule[0][6] == 3:
                add "sel_gwa"

            elif day_schedule[0][6] == 4:
                add "sel_rest"

#2주차
    if day_schedule[0][8] != 0:
        hbox:
            xpos 160 ypos 312
            if day_schedule[0][8] == 1:
                add "sel_study"

            elif day_schedule[0][8] == 2:
                add "sel_club"

            elif day_schedule[0][8] == 3:
                add "sel_gwa"

            elif day_schedule[0][8] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[0][9] != 0:
        hbox:
            xpos 288 ypos 312
            if day_schedule[0][9] == 1:
                add "sel_study"

            elif day_schedule[0][9] == 2:
                add "sel_club"

            elif day_schedule[0][9] == 3:
                add "sel_gwa"

            elif day_schedule[0][9] == 4:
                add "sel_rest"

    if day_schedule[0][10] != 0:
        hbox:
            xpos 416 ypos 312
            if day_schedule[0][10] == 1:
                add "sel_study"

            elif day_schedule[0][10] == 2:
                add "sel_club"

            elif day_schedule[0][10] == 3:
                add "sel_gwa"

            elif day_schedule[0][10] == 4:
                add "sel_rest"

    if day_schedule[0][11] != 0:
        hbox:
            xpos 544 ypos 312
            if day_schedule[0][11] == 1:
                add "sel_study"

            elif day_schedule[0][11] == 2:
                add "sel_club"

            elif day_schedule[0][11] == 3:
                add "sel_gwa"

            elif day_schedule[0][11] == 4:
                add "sel_rest"

    if day_schedule[0][12] != 0:
        hbox:
            xpos 672 ypos 312
            if day_schedule[0][12] == 1:
                add "sel_study"

            elif day_schedule[0][12] == 2:
                add "sel_club"

            elif day_schedule[0][12] == 3:
                add "sel_gwa"

            elif day_schedule[0][12] == 4:
                add "sel_rest"

    if day_schedule[0][13] != 0:
        hbox:
            xpos 800 ypos 312
            if day_schedule[0][13] == 1:
                add "sel_study"

            elif day_schedule[0][13] == 2:
                add "sel_club"

            elif day_schedule[0][13] == 3:
                add "sel_gwa"

            elif day_schedule[0][13] == 4:
                add "sel_rest"

#3주차
    if day_schedule[0][15] != 0:
        hbox:
            xpos 160 ypos 440
            if day_schedule[0][15] == 1:
                add "sel_study"

            elif day_schedule[0][15] == 2:
                add "sel_club"

            elif day_schedule[0][15] == 3:
                add "sel_gwa"

            elif day_schedule[0][15] == 4:
                add "sel_rest"

    if day_schedule[0][16] != 0:
        hbox:
            xpos 288 ypos 440
            if day_schedule[0][16] == 1:
                add "sel_study"

            elif day_schedule[0][16] == 2:
                add "sel_club"

            elif day_schedule[0][16] == 3:
                add "sel_gwa"

            elif day_schedule[0][16] == 4:
                add "sel_rest"

    if day_schedule[0][17] != 0:
        hbox:
            xpos 416 ypos 440
            if day_schedule[0][17] == 1:
                add "sel_study"

            elif day_schedule[0][17] == 2:
                add "sel_club"

            elif day_schedule[0][17] == 3:
                add "sel_gwa"

            elif day_schedule[0][17] == 4:
                add "sel_rest"

    if day_schedule[0][18] != 0:
        hbox:
            xpos 544 ypos 440
            if day_schedule[0][18] == 1:
                add "sel_study"

            elif day_schedule[0][18] == 2:
                add "sel_club"

            elif day_schedule[0][18] == 3:
                add "sel_gwa"

            elif day_schedule[0][18] == 4:
                add "sel_rest"

    if day_schedule[0][19] != 0:
        hbox:
            xpos 672 ypos 440
            if day_schedule[0][19] == 1:
                add "sel_study"

            elif day_schedule[0][19] == 2:
                add "sel_club"

            elif day_schedule[0][19] == 3:
                add "sel_gwa"

            elif day_schedule[0][19] == 4:
                add "sel_rest"

    if day_schedule[0][20] != 0:
        hbox:
            xpos 800 ypos 440
            if day_schedule[0][20] == 1:
                add "sel_study"

            elif day_schedule[0][20] == 2:
                add "sel_club"

            elif day_schedule[0][20] == 3:
                add "sel_gwa"

            elif day_schedule[0][20] == 4:
                add "sel_rest"

#4주차
    if day_schedule[0][22] != 0:
        hbox:
            xpos 160 ypos 568
            if day_schedule[0][22] == 1:
                add "sel_study"

            elif day_schedule[0][22] == 2:
                add "sel_club"

            elif day_schedule[0][22] == 3:
                add "sel_gwa"

            elif day_schedule[0][22] == 4:
                add "sel_rest"

    if day_schedule[0][23] != 0:
        hbox:
            xpos 288 ypos 568
            if day_schedule[0][23] == 1:
                add "sel_study"

            elif day_schedule[0][23] == 2:
                add "sel_club"

            elif day_schedule[0][23] == 3:
                add "sel_gwa"

            elif day_schedule[0][23] == 4:
                add "sel_rest"

    if day_schedule[0][24] != 0:
        hbox:
            xpos 416 ypos 568
            if day_schedule[0][24] == 1:
                add "sel_study"

            elif day_schedule[0][24] == 2:
                add "sel_club"

            elif day_schedule[0][24] == 3:
                add "sel_gwa"

            elif day_schedule[0][24] == 4:
                add "sel_rest"

    if day_schedule[0][25] != 0:
        hbox:
            xpos 544 ypos 568
            if day_schedule[0][25] == 1:
                add "sel_study"

            elif day_schedule[0][25] == 2:
                add "sel_club"

            elif day_schedule[0][25] == 3:
                add "sel_gwa"

            elif day_schedule[0][25] == 4:
                add "sel_rest"

    if day_schedule[0][26] != 0:
        hbox:
            xpos 672 ypos 568
            if day_schedule[0][26] == 1:
                add "sel_study"

            elif day_schedule[0][26] == 2:
                add "sel_club"

            elif day_schedule[0][26] == 3:
                add "sel_gwa"

            elif day_schedule[0][26] == 4:
                add "sel_rest"

    if day_schedule[0][27] != 0:
        hbox:
            xpos 800 ypos 568
            if day_schedule[0][27] == 1:
                add "sel_study"

            elif day_schedule[0][27] == 2:
                add "sel_club"

            elif day_schedule[0][27] == 3:
                add "sel_gwa"

            elif day_schedule[0][27] == 4:
                add "sel_rest"

screen second_month_schedule_icon_show():
    # 월요일
    if day_schedule[1][1] != 0:
        hbox:
            xpos 160 ypos 184
            if day_schedule[1][1] == 1:
                add "sel_study"

            elif day_schedule[1][1] == 2:
                add "sel_club"

            elif day_schedule[1][1] == 3:
                add "sel_gwa"

            elif day_schedule[1][1] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[1][2] != 0:
        hbox:
            xpos 288 ypos 184
            if day_schedule[1][2] == 1:
                add "sel_study"

            elif day_schedule[1][2] == 2:
                add "sel_club"

            elif day_schedule[1][2] == 3:
                add "sel_gwa"

            elif day_schedule[1][2] == 4:
                add "sel_rest"

    if day_schedule[1][3] != 0:
        hbox:
            xpos 416 ypos 184
            if day_schedule[1][3] == 1:
                add "sel_study"

            elif day_schedule[1][3] == 2:
                add "sel_club"

            elif day_schedule[1][3] == 3:
                add "sel_gwa"

            elif day_schedule[1][3] == 4:
                add "sel_rest"

    if day_schedule[1][4] != 0:
        hbox:
            xpos 544 ypos 184
            if day_schedule[1][4] == 1:
                add "sel_study"

            elif day_schedule[1][4] == 2:
                add "sel_club"

            elif day_schedule[1][4] == 3:
                add "sel_gwa"

            elif day_schedule[1][4] == 4:
                add "sel_rest"

    if day_schedule[1][5] != 0:
        hbox:
            xpos 672 ypos 184
            if day_schedule[1][5] == 1:
                add "sel_study"

            elif day_schedule[1][5] == 2:
                add "sel_club"

            elif day_schedule[1][5] == 3:
                add "sel_gwa"

            elif day_schedule[1][5] == 4:
                add "sel_rest"

    if day_schedule[1][6] != 0:
        hbox:
            xpos 800 ypos 184
            if day_schedule[1][6] == 1:
                add "sel_study"

            elif day_schedule[1][6] == 2:
                add "sel_club"

            elif day_schedule[1][6] == 3:
                add "sel_gwa"

            elif day_schedule[1][6] == 4:
                add "sel_rest"

#2주차
    if day_schedule[1][8] != 0:
        hbox:
            xpos 160 ypos 312
            if day_schedule[1][8] == 1:
                add "sel_study"

            elif day_schedule[1][8] == 2:
                add "sel_club"

            elif day_schedule[1][8] == 3:
                add "sel_gwa"

            elif day_schedule[1][8] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[1][9] != 0:
        hbox:
            xpos 288 ypos 312
            if day_schedule[1][9] == 1:
                add "sel_study"

            elif day_schedule[1][9] == 2:
                add "sel_club"

            elif day_schedule[1][9] == 3:
                add "sel_gwa"

            elif day_schedule[1][9] == 4:
                add "sel_rest"

    if day_schedule[1][10] != 0:
        hbox:
            xpos 416 ypos 312
            if day_schedule[1][10] == 1:
                add "sel_study"

            elif day_schedule[1][10] == 2:
                add "sel_club"

            elif day_schedule[1][10] == 3:
                add "sel_gwa"

            elif day_schedule[1][10] == 4:
                add "sel_rest"

    if day_schedule[1][11] != 0:
        hbox:
            xpos 544 ypos 312
            if day_schedule[1][11] == 1:
                add "sel_study"

            elif day_schedule[1][11] == 2:
                add "sel_club"

            elif day_schedule[1][11] == 3:
                add "sel_gwa"

            elif day_schedule[1][11] == 4:
                add "sel_rest"

    if day_schedule[1][12] != 0:
        hbox:
            xpos 672 ypos 312
            if day_schedule[1][12] == 1:
                add "sel_study"

            elif day_schedule[1][12] == 2:
                add "sel_club"

            elif day_schedule[1][12] == 3:
                add "sel_gwa"

            elif day_schedule[1][12] == 4:
                add "sel_rest"

    if day_schedule[1][13] != 0:
        hbox:
            xpos 800 ypos 312
            if day_schedule[1][13] == 1:
                add "sel_study"

            elif day_schedule[1][13] == 2:
                add "sel_club"

            elif day_schedule[1][13] == 3:
                add "sel_gwa"

            elif day_schedule[1][13] == 4:
                add "sel_rest"

#3주차
    if day_schedule[1][15] != 0:
        hbox:
            xpos 160 ypos 440
            if day_schedule[1][15] == 1:
                add "sel_study"

            elif day_schedule[1][15] == 2:
                add "sel_club"

            elif day_schedule[1][15] == 3:
                add "sel_gwa"

            elif day_schedule[1][15] == 4:
                add "sel_rest"

    if day_schedule[1][16] != 0:
        hbox:
            xpos 288 ypos 440
            if day_schedule[1][16] == 1:
                add "sel_study"

            elif day_schedule[1][16] == 2:
                add "sel_club"

            elif day_schedule[1][16] == 3:
                add "sel_gwa"

            elif day_schedule[1][16] == 4:
                add "sel_rest"

    if day_schedule[1][17] != 0:
        hbox:
            xpos 416 ypos 440
            if day_schedule[1][17] == 1:
                add "sel_study"

            elif day_schedule[1][17] == 2:
                add "sel_club"

            elif day_schedule[1][17] == 3:
                add "sel_gwa"

            elif day_schedule[1][17] == 4:
                add "sel_rest"

    if day_schedule[1][18] != 0:
        hbox:
            xpos 544 ypos 440
            if day_schedule[1][18] == 1:
                add "sel_study"

            elif day_schedule[1][18] == 2:
                add "sel_club"

            elif day_schedule[1][18] == 3:
                add "sel_gwa"

            elif day_schedule[1][18] == 4:
                add "sel_rest"

    if day_schedule[1][19] != 0:
        hbox:
            xpos 672 ypos 440
            if day_schedule[1][19] == 1:
                add "sel_study"

            elif day_schedule[1][19] == 2:
                add "sel_club"

            elif day_schedule[1][19] == 3:
                add "sel_gwa"

            elif day_schedule[1][19] == 4:
                add "sel_rest"

    if day_schedule[1][20] != 0:
        hbox:
            xpos 800 ypos 440
            if day_schedule[1][20] == 1:
                add "sel_study"

            elif day_schedule[1][20] == 2:
                add "sel_club"

            elif day_schedule[1][20] == 3:
                add "sel_gwa"

            elif day_schedule[1][20] == 4:
                add "sel_rest"

#4주차
    if day_schedule[1][22] != 0:
        hbox:
            xpos 160 ypos 568
            if day_schedule[1][22] == 1:
                add "sel_study"

            elif day_schedule[1][22] == 2:
                add "sel_club"

            elif day_schedule[1][22] == 3:
                add "sel_gwa"

            elif day_schedule[1][22] == 4:
                add "sel_rest"

    if day_schedule[1][23] != 0:
        hbox:
            xpos 288 ypos 568
            if day_schedule[1][23] == 1:
                add "sel_study"

            elif day_schedule[1][23] == 2:
                add "sel_club"

            elif day_schedule[1][23] == 3:
                add "sel_gwa"

            elif day_schedule[1][23] == 4:
                add "sel_rest"

    if day_schedule[1][24] != 0:
        hbox:
            xpos 416 ypos 568
            if day_schedule[1][24] == 1:
                add "sel_study"

            elif day_schedule[1][24] == 2:
                add "sel_club"

            elif day_schedule[1][24] == 3:
                add "sel_gwa"

            elif day_schedule[1][24] == 4:
                add "sel_rest"

    if day_schedule[1][25] != 0:
        hbox:
            xpos 544 ypos 568
            if day_schedule[1][25] == 1:
                add "sel_study"

            elif day_schedule[1][25] == 2:
                add "sel_club"

            elif day_schedule[1][25] == 3:
                add "sel_gwa"

            elif day_schedule[1][25] == 4:
                add "sel_rest"

    if day_schedule[1][26] != 0:
        hbox:
            xpos 672 ypos 568
            if day_schedule[1][26] == 1:
                add "sel_study"

            elif day_schedule[1][26] == 2:
                add "sel_club"

            elif day_schedule[1][26] == 3:
                add "sel_gwa"

            elif day_schedule[1][26] == 4:
                add "sel_rest"

    if day_schedule[1][27] != 0:
        hbox:
            xpos 800 ypos 568
            if day_schedule[1][27] == 1:
                add "sel_study"

            elif day_schedule[1][27] == 2:
                add "sel_club"

            elif day_schedule[1][27] == 3:
                add "sel_gwa"

            elif day_schedule[1][27] == 4:
                add "sel_rest"

screen third_month_schedule_icon_show():
    # 월요일
    if day_schedule[2][1] != 0:
        hbox:
            xpos 160 ypos 184
            if day_schedule[2][1] == 1:
                add "sel_study"

            elif day_schedule[2][1] == 2:
                add "sel_club"

            elif day_schedule[2][1] == 3:
                add "sel_gwa"

            elif day_schedule[2][1] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[2][2] != 0:
        hbox:
            xpos 288 ypos 184
            if day_schedule[2][2] == 1:
                add "sel_study"

            elif day_schedule[2][2] == 2:
                add "sel_club"

            elif day_schedule[2][2] == 3:
                add "sel_gwa"

            elif day_schedule[2][2] == 4:
                add "sel_rest"

    if day_schedule[2][3] != 0:
        hbox:
            xpos 416 ypos 184
            if day_schedule[2][3] == 1:
                add "sel_study"

            elif day_schedule[2][3] == 2:
                add "sel_club"

            elif day_schedule[2][3] == 3:
                add "sel_gwa"

            elif day_schedule[2][3] == 4:
                add "sel_rest"

    if day_schedule[2][4] != 0:
        hbox:
            xpos 544 ypos 184
            if day_schedule[2][4] == 1:
                add "sel_study"

            elif day_schedule[2][4] == 2:
                add "sel_club"

            elif day_schedule[2][4] == 3:
                add "sel_gwa"

            elif day_schedule[2][4] == 4:
                add "sel_rest"

    if day_schedule[2][5] != 0:
        hbox:
            xpos 672 ypos 184
            if day_schedule[2][5] == 1:
                add "sel_study"

            elif day_schedule[2][5] == 2:
                add "sel_club"

            elif day_schedule[2][5] == 3:
                add "sel_gwa"

            elif day_schedule[2][5] == 4:
                add "sel_rest"

    if day_schedule[2][6] != 0:
        hbox:
            xpos 800 ypos 184
            if day_schedule[2][6] == 1:
                add "sel_study"

            elif day_schedule[2][6] == 2:
                add "sel_club"

            elif day_schedule[2][6] == 3:
                add "sel_gwa"

            elif day_schedule[2][6] == 4:
                add "sel_rest"

#2주차
    if day_schedule[2][8] != 0:
        hbox:
            xpos 160 ypos 312
            if day_schedule[2][8] == 1:
                add "sel_study"

            elif day_schedule[2][8] == 2:
                add "sel_club"

            elif day_schedule[2][8] == 3:
                add "sel_gwa"

            elif day_schedule[2][8] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[2][9] != 0:
        hbox:
            xpos 288 ypos 312
            if day_schedule[2][9] == 1:
                add "sel_study"

            elif day_schedule[2][9] == 2:
                add "sel_club"

            elif day_schedule[2][9] == 3:
                add "sel_gwa"

            elif day_schedule[2][9] == 4:
                add "sel_rest"

    if day_schedule[2][10] != 0:
        hbox:
            xpos 416 ypos 312
            if day_schedule[2][10] == 1:
                add "sel_study"

            elif day_schedule[2][10] == 2:
                add "sel_club"

            elif day_schedule[2][10] == 3:
                add "sel_gwa"

            elif day_schedule[2][10] == 4:
                add "sel_rest"

    if day_schedule[2][11] != 0:
        hbox:
            xpos 544 ypos 312
            if day_schedule[2][11] == 1:
                add "sel_study"

            elif day_schedule[2][11] == 2:
                add "sel_club"

            elif day_schedule[2][11] == 3:
                add "sel_gwa"

            elif day_schedule[2][11] == 4:
                add "sel_rest"

    if day_schedule[2][12] != 0:
        hbox:
            xpos 672 ypos 312
            if day_schedule[2][12] == 1:
                add "sel_study"

            elif day_schedule[2][12] == 2:
                add "sel_club"

            elif day_schedule[2][12] == 3:
                add "sel_gwa"

            elif day_schedule[2][12] == 4:
                add "sel_rest"

    if day_schedule[2][13] != 0:
        hbox:
            xpos 800 ypos 312
            if day_schedule[2][13] == 1:
                add "sel_study"

            elif day_schedule[2][13] == 2:
                add "sel_club"

            elif day_schedule[2][13] == 3:
                add "sel_gwa"

            elif day_schedule[2][13] == 4:
                add "sel_rest"

#3주차
    if day_schedule[2][15] != 0:
        hbox:
            xpos 160 ypos 440
            if day_schedule[2][15] == 1:
                add "sel_study"

            elif day_schedule[2][15] == 2:
                add "sel_club"

            elif day_schedule[2][15] == 3:
                add "sel_gwa"

            elif day_schedule[2][15] == 4:
                add "sel_rest"

    if day_schedule[2][16] != 0:
        hbox:
            xpos 288 ypos 440
            if day_schedule[2][16] == 1:
                add "sel_study"

            elif day_schedule[2][16] == 2:
                add "sel_club"

            elif day_schedule[2][16] == 3:
                add "sel_gwa"

            elif day_schedule[2][16] == 4:
                add "sel_rest"

    if day_schedule[2][17] != 0:
        hbox:
            xpos 416 ypos 440
            if day_schedule[2][17] == 1:
                add "sel_study"

            elif day_schedule[2][17] == 2:
                add "sel_club"

            elif day_schedule[2][17] == 3:
                add "sel_gwa"

            elif day_schedule[2][17] == 4:
                add "sel_rest"

    if day_schedule[2][18] != 0:
        hbox:
            xpos 544 ypos 440
            if day_schedule[2][18] == 1:
                add "sel_study"

            elif day_schedule[2][18] == 2:
                add "sel_club"

            elif day_schedule[2][18] == 3:
                add "sel_gwa"

            elif day_schedule[2][18] == 4:
                add "sel_rest"

    if day_schedule[2][19] != 0:
        hbox:
            xpos 672 ypos 440
            if day_schedule[2][19] == 1:
                add "sel_study"

            elif day_schedule[2][19] == 2:
                add "sel_club"

            elif day_schedule[2][19] == 3:
                add "sel_gwa"

            elif day_schedule[2][19] == 4:
                add "sel_rest"

    if day_schedule[2][20] != 0:
        hbox:
            xpos 800 ypos 440
            if day_schedule[2][20] == 1:
                add "sel_study"

            elif day_schedule[2][20] == 2:
                add "sel_club"

            elif day_schedule[2][20] == 3:
                add "sel_gwa"

            elif day_schedule[2][20] == 4:
                add "sel_rest"

#4주차
    if day_schedule[2][22] != 0:
        hbox:
            xpos 160 ypos 568
            if day_schedule[2][22] == 1:
                add "sel_study"

            elif day_schedule[2][22] == 2:
                add "sel_club"

            elif day_schedule[2][22] == 3:
                add "sel_gwa"

            elif day_schedule[2][22] == 4:
                add "sel_rest"

    if day_schedule[2][23] != 0:
        hbox:
            xpos 288 ypos 568
            if day_schedule[2][23] == 1:
                add "sel_study"

            elif day_schedule[2][23] == 2:
                add "sel_club"

            elif day_schedule[2][23] == 3:
                add "sel_gwa"

            elif day_schedule[2][23] == 4:
                add "sel_rest"

    if day_schedule[2][24] != 0:
        hbox:
            xpos 416 ypos 568
            if day_schedule[2][24] == 1:
                add "sel_study"

            elif day_schedule[2][24] == 2:
                add "sel_club"

            elif day_schedule[2][24] == 3:
                add "sel_gwa"

            elif day_schedule[2][24] == 4:
                add "sel_rest"

    if day_schedule[2][25] != 0:
        hbox:
            xpos 544 ypos 568
            if day_schedule[2][25] == 1:
                add "sel_study"

            elif day_schedule[2][25] == 2:
                add "sel_club"

            elif day_schedule[2][25] == 3:
                add "sel_gwa"

            elif day_schedule[2][25] == 4:
                add "sel_rest"

    if day_schedule[2][26] != 0:
        hbox:
            xpos 672 ypos 568
            if day_schedule[2][26] == 1:
                add "sel_study"

            elif day_schedule[2][26] == 2:
                add "sel_club"

            elif day_schedule[2][26] == 3:
                add "sel_gwa"

            elif day_schedule[2][26] == 4:
                add "sel_rest"

    if day_schedule[2][27] != 0:
        hbox:
            xpos 800 ypos 568
            if day_schedule[2][27] == 1:
                add "sel_study"

            elif day_schedule[2][27] == 2:
                add "sel_club"

            elif day_schedule[2][27] == 3:
                add "sel_gwa"

            elif day_schedule[2][27] == 4:
                add "sel_rest"

screen fourth_month_schedule_icon_show():
    # 월요일
    if day_schedule[3][1] != 0:
        hbox:
            xpos 160 ypos 184
            if day_schedule[3][1] == 1:
                add "sel_study"

            elif day_schedule[3][1] == 2:
                add "sel_club"

            elif day_schedule[3][1] == 3:
                add "sel_gwa"

            elif day_schedule[3][1] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[3][2] != 0:
        hbox:
            xpos 288 ypos 184
            if day_schedule[3][2] == 1:
                add "sel_study"

            elif day_schedule[3][2] == 2:
                add "sel_club"

            elif day_schedule[3][2] == 3:
                add "sel_gwa"

            elif day_schedule[3][2] == 4:
                add "sel_rest"

    if day_schedule[3][3] != 0:
        hbox:
            xpos 416 ypos 184
            if day_schedule[3][3] == 1:
                add "sel_study"

            elif day_schedule[3][3] == 2:
                add "sel_club"

            elif day_schedule[3][3] == 3:
                add "sel_gwa"

            elif day_schedule[3][3] == 4:
                add "sel_rest"

    if day_schedule[3][4] != 0:
        hbox:
            xpos 544 ypos 184
            if day_schedule[3][4] == 1:
                add "sel_study"

            elif day_schedule[3][4] == 2:
                add "sel_club"

            elif day_schedule[3][4] == 3:
                add "sel_gwa"

            elif day_schedule[3][4] == 4:
                add "sel_rest"

    if day_schedule[3][5] != 0:
        hbox:
            xpos 672 ypos 184
            if day_schedule[3][5] == 1:
                add "sel_study"

            elif day_schedule[3][5] == 2:
                add "sel_club"

            elif day_schedule[3][5] == 3:
                add "sel_gwa"

            elif day_schedule[3][5] == 4:
                add "sel_rest"

    if day_schedule[3][6] != 0:
        hbox:
            xpos 800 ypos 184
            if day_schedule[3][6] == 1:
                add "sel_study"

            elif day_schedule[3][6] == 2:
                add "sel_club"

            elif day_schedule[3][6] == 3:
                add "sel_gwa"

            elif day_schedule[3][6] == 4:
                add "sel_rest"

#2주차
    if day_schedule[3][8] != 0:
        hbox:
            xpos 160 ypos 312
            if day_schedule[3][8] == 1:
                add "sel_study"

            elif day_schedule[3][8] == 2:
                add "sel_club"

            elif day_schedule[3][8] == 3:
                add "sel_gwa"

            elif day_schedule[3][8] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[3][9] != 0:
        hbox:
            xpos 288 ypos 312
            if day_schedule[3][9] == 1:
                add "sel_study"

            elif day_schedule[3][9] == 2:
                add "sel_club"

            elif day_schedule[3][9] == 3:
                add "sel_gwa"

            elif day_schedule[3][9] == 4:
                add "sel_rest"

    if day_schedule[3][10] != 0:
        hbox:
            xpos 416 ypos 312
            if day_schedule[3][10] == 1:
                add "sel_study"

            elif day_schedule[3][10] == 2:
                add "sel_club"

            elif day_schedule[3][10] == 3:
                add "sel_gwa"

            elif day_schedule[3][10] == 4:
                add "sel_rest"

    if day_schedule[3][11] != 0:
        hbox:
            xpos 544 ypos 312
            if day_schedule[3][11] == 1:
                add "sel_study"

            elif day_schedule[3][11] == 2:
                add "sel_club"

            elif day_schedule[3][11] == 3:
                add "sel_gwa"

            elif day_schedule[3][11] == 4:
                add "sel_rest"

    if day_schedule[3][12] != 0:
        hbox:
            xpos 672 ypos 312
            if day_schedule[3][12] == 1:
                add "sel_study"

            elif day_schedule[3][12] == 2:
                add "sel_club"

            elif day_schedule[3][12] == 3:
                add "sel_gwa"

            elif day_schedule[3][12] == 4:
                add "sel_rest"

    if day_schedule[3][13] != 0:
        hbox:
            xpos 800 ypos 312
            if day_schedule[3][13] == 1:
                add "sel_study"

            elif day_schedule[3][13] == 2:
                add "sel_club"

            elif day_schedule[3][13] == 3:
                add "sel_gwa"

            elif day_schedule[3][13] == 4:
                add "sel_rest"

#3주차
    if day_schedule[3][15] != 0:
        hbox:
            xpos 160 ypos 440
            if day_schedule[3][15] == 1:
                add "sel_study"

            elif day_schedule[3][15] == 2:
                add "sel_club"

            elif day_schedule[3][15] == 3:
                add "sel_gwa"

            elif day_schedule[3][15] == 4:
                add "sel_rest"

    if day_schedule[3][16] != 0:
        hbox:
            xpos 288 ypos 440
            if day_schedule[3][16] == 1:
                add "sel_study"

            elif day_schedule[3][16] == 2:
                add "sel_club"

            elif day_schedule[3][16] == 3:
                add "sel_gwa"

            elif day_schedule[3][16] == 4:
                add "sel_rest"

    if day_schedule[3][17] != 0:
        hbox:
            xpos 416 ypos 440
            if day_schedule[3][17] == 1:
                add "sel_study"

            elif day_schedule[3][17] == 2:
                add "sel_club"

            elif day_schedule[3][17] == 3:
                add "sel_gwa"

            elif day_schedule[3][17] == 4:
                add "sel_rest"

    if day_schedule[3][18] != 0:
        hbox:
            xpos 544 ypos 440
            if day_schedule[3][18] == 1:
                add "sel_study"

            elif day_schedule[3][18] == 2:
                add "sel_club"

            elif day_schedule[3][18] == 3:
                add "sel_gwa"

            elif day_schedule[3][18] == 4:
                add "sel_rest"

    if day_schedule[3][19] != 0:
        hbox:
            xpos 672 ypos 440
            if day_schedule[3][19] == 1:
                add "sel_study"

            elif day_schedule[3][19] == 2:
                add "sel_club"

            elif day_schedule[3][19] == 3:
                add "sel_gwa"

            elif day_schedule[3][19] == 4:
                add "sel_rest"

    if day_schedule[3][20] != 0:
        hbox:
            xpos 800 ypos 440
            if day_schedule[3][20] == 1:
                add "sel_study"

            elif day_schedule[3][20] == 2:
                add "sel_club"

            elif day_schedule[3][20] == 3:
                add "sel_gwa"

            elif day_schedule[3][20] == 4:
                add "sel_rest"

#4주차
    if day_schedule[3][22] != 0:
        hbox:
            xpos 160 ypos 568
            if day_schedule[3][22] == 1:
                add "sel_study"

            elif day_schedule[3][22] == 2:
                add "sel_club"

            elif day_schedule[3][22] == 3:
                add "sel_gwa"

            elif day_schedule[3][22] == 4:
                add "sel_rest"

    if day_schedule[3][23] != 0:
        hbox:
            xpos 288 ypos 568
            if day_schedule[3][23] == 1:
                add "sel_study"

            elif day_schedule[3][23] == 2:
                add "sel_club"

            elif day_schedule[3][23] == 3:
                add "sel_gwa"

            elif day_schedule[3][23] == 4:
                add "sel_rest"

    if day_schedule[3][24] != 0:
        hbox:
            xpos 416 ypos 568
            if day_schedule[3][24] == 1:
                add "sel_study"

            elif day_schedule[3][24] == 2:
                add "sel_club"

            elif day_schedule[3][24] == 3:
                add "sel_gwa"

            elif day_schedule[3][24] == 4:
                add "sel_rest"

    if day_schedule[3][25] != 0:
        hbox:
            xpos 544 ypos 568
            if day_schedule[3][25] == 1:
                add "sel_study"

            elif day_schedule[3][25] == 2:
                add "sel_club"

            elif day_schedule[3][25] == 3:
                add "sel_gwa"

            elif day_schedule[3][25] == 4:
                add "sel_rest"

    if day_schedule[3][26] != 0:
        hbox:
            xpos 672 ypos 568
            if day_schedule[3][26] == 1:
                add "sel_study"

            elif day_schedule[3][26] == 2:
                add "sel_club"

            elif day_schedule[3][26] == 3:
                add "sel_gwa"

            elif day_schedule[3][26] == 4:
                add "sel_rest"

    if day_schedule[3][27] != 0:
        hbox:
            xpos 800 ypos 568
            if day_schedule[3][27] == 1:
                add "sel_study"

            elif day_schedule[3][27] == 2:
                add "sel_club"

            elif day_schedule[3][27] == 3:
                add "sel_gwa"

            elif day_schedule[3][27] == 4:
                add "sel_rest"



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
