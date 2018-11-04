# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

image planner_background = "planner_background.png"
image highlight = "highlight.png"

image sel_study = "sel_study.png" #1
image sel_club = "sel_club.png" #2
image sel_gwa = "sel_gwa.png" #3
image sel_rest = "sel_rest.png" #4

style center_text:
    text_align 0.5

## 일요일 방에서 핸드폰 아이콘
screen phone_icon():
    vbox xalign 0.34 yalign 0.7:
        imagebutton:
            idle "phone"
            hover im.Alpha("phone.png",2)
            action Jump("phone")

## 일요일 방에서 플래너 아이콘
screen planner_icon():
    vbox xalign 0.64 yalign 0.7:
        imagebutton:
            idle "planner"
            hover im.Alpha("planner.png",2)
            action Jump("planner")

## 플래너를 눌렀을 때 나오는 일정짜기 버튼
screen schedule_button():
    frame:
        xpos 750 yalign 0.5
        xsize 200
        vbox:
            spacing 10

            textbutton "공부하기":
                action SetVariable("tmp", 1)

            textbutton "동아리":
                action SetVariable("tmp", 2)
#                action Notify("동아리 활동했다")

            textbutton "과활동":
                action SetVariable("tmp", 3)
#                action Notify("과활동했다")

            textbutton "휴식":
                action SetVariable("tmp", 4)
#                action Notify("쉬었다")

            textbutton "뒤로가기":
#                $ tmp = 5
                action Jump("GoBack")
                #text_align 0.5



## 스케줄러에서 선택화면이 나타나는 하이라이트 화면
screen schedule_highlight():
    vbox:
        xpos (59+ 99*(day-1)) ypos 307
        add "highlight"

# 월요일부터 금요일까지 노가다 작업
screen schedule_mon():
    if day_schedule[0] != 0:
        frame:
            xpos 59 ypos 307
            if day_schedule[0] == 1:
                add "sel_study"

            elif day_schedule[0] == 2:
                add "sel_club"

            elif day_schedule[0] == 3:
                add "sel_gwa"

            elif day_schedule[0] == 4:
                add "sel_rest"

screen schedule_tue():
    if day_schedule[1] != 0:
        frame:
            xpos 159 ypos 307
            if day_schedule[1] == 1:
                add "sel_study"

            elif day_schedule[1] == 2:
                add "sel_club"

            elif day_schedule[1] == 3:
                add "sel_gwa"

            elif day_schedule[1] == 4:
                add "sel_rest"

screen schedule_wed():
    if day_schedule[2] != 0:
        frame:
            xpos 259 ypos 307
            if day_schedule[2] == 1:
                add "sel_study"

            elif day_schedule[2] == 2:
                add "sel_club"

            elif day_schedule[2] == 3:
                add "sel_gwa"

            elif day_schedule[2] == 4:
                add "sel_rest"

screen schedule_thu():
    if day_schedule[3] != 0:
        frame:
            xpos 359 ypos 307
            if day_schedule[3] == 1:
                add "sel_study"

            elif day_schedule[3] == 2:
                add "sel_club"

            elif day_schedule[3] == 3:
                add "sel_gwa"

            elif day_schedule[3] == 4:
                add "sel_rest"

screen schedule_fri():
    if day_schedule[4] != 0:
        frame:
            xpos 459 ypos 307
            if day_schedule[4] == 1:
                add "sel_study"

            elif day_schedule[4] == 2:
                add "sel_club"

            elif day_schedule[4] == 3:
                add "sel_gwa"

            elif day_schedule[4] == 4:
                add "sel_rest"

screen schedule_sat():
    if day_schedule[5] != 0:
        frame:
            xpos 559 ypos 307
            if day_schedule[5] == 1:
                add "sel_study"

            elif day_schedule[5] == 2:
                add "sel_club"

            elif day_schedule[5] == 3:
                add "sel_gwa"

            elif day_schedule[5] == 4:
                add "sel_rest"

#s tart 함수에서 오는 곳
label sunday_room:
    scene room at truecenter

    show screen phone_icon
    show screen planner_icon


    s "Hi"
    p "밥을 먹었다. 체력을 회복한다"

    $hp += 10

    s "새로운 렌파이 게임을 만들었군요."


    call limitation #아직 구현 안된 것


    s "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    return

label planner:
    show planner_background
    hide screen phone_icon
    hide screen planner_icon

    # 형광색 하이라이트 창
    if day <= 6 :
        show screen schedule_highlight
    else :
        hide screen schedule_highlight

    show screen schedule_mon
    show screen schedule_tue
    show screen schedule_wed
    show screen schedule_thu
    show screen schedule_fri
    show screen schedule_sat

    # 오른쪽 스케줄 창
    show screen schedule_button
    "하루가 지난다"


    if day < 7:
        $ day_schedule[day-1] = tmp

#    hide screen schedule_button

    if tmp != 0:
        if day <= 6:
            $ day += 1
        $ tmp = 0


    jump planner

    return

label GoBack :
    hide planner_background

    hide screen schedule_button
    hide screen schedule_highlight

    hide screen schedule_mon
    hide screen schedule_tue
    hide screen schedule_wed
    hide screen schedule_thu
    hide screen schedule_fri
    hide screen schedule_sat


    jump sunday_room

label phone:
    hide screen phone_icon
    hide screen planner_icon
    "핸드폰 화면이 구현되지 않았습니다."
    "일요일 화면으로 돌아갑니다"

    jump sunday_room
    return
