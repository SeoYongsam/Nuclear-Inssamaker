image planner_background = "planner_background.png"
image highlight = "highlight.png"

image sel_study = im.Scale("sel_study.png",98,98)   #1
image sel_club = im.Scale("sel_club.png",98,98)     #2
image sel_gwa = im.Scale("sel_gwa.png",98,98)       #3
image sel_rest = im.Scale("sel_rest.png",98,98)     #4

## 일요일 방에서 핸드폰 아이콘
screen phone_icon():
    vbox :
        xalign 0.34 yalign 0.7
        imagebutton:
            idle "phone"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("phone.png",2)
            # 클릭시 phone label을 실행함
            action Jump("phone")

## 일요일 방에서 플래너 아이콘
screen planner_icon():
    vbox xalign 0.64 yalign 0.7 :
        imagebutton:
            idle "planner"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("planner.png",2)
            # 클릭시 planner label을 실행함
            action Jump("planner")

## 스케줄러에서 선택화면이 나타나는 노란색 테두리 하이라이트 화면
screen schedule_highlight():
    if day < 7:
        vbox:
            xpos (59+ 99*(day-1)) ypos 307
            add "highlight"

## 플래너를 눌렀을 때 나오는 일정짜기 버튼
screen schedule_button():
    frame:
        xpos 750 yalign 0.5
        xsize 200
        vbox:
            spacing 10

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
                #text_align 0.5

screen schedule_icon_show():
    # 월요일
    if day_schedule[1] != 0:
        hbox:
            xpos 60 ypos 308
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
            xpos 159 ypos 308
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
            xpos 258 ypos 308
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
            xpos 357 ypos 308
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
            xpos 456 ypos 308
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
            xpos 555 ypos 308
            if day_schedule[6] == 1:
                add "sel_study"

            elif day_schedule[6] == 2:
                add "sel_club"

            elif day_schedule[6] == 3:
                add "sel_gwa"

            elif day_schedule[6] == 4:
                add "sel_rest"

screen schedule_revise_button():
    hbox:
        xpos 60 ypos 308
        spacing 1
        imagebutton :
            idle im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            hover im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            action Call("button_reset", number = 1)

        imagebutton :
            idle im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            hover im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            action Call("button_reset", number = 2)

        imagebutton :
            idle im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 3)

        imagebutton :
            idle im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 4)

        imagebutton :
            idle im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 5)

        imagebutton :
            idle im.Scale(im.Alpha("sel_study.png",0), 98, 98)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 6)
