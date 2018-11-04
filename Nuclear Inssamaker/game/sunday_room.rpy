# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

image planner_background = "planner_background.png"
image highlight = "highlight.png"

image sel_club = "sel_club.png"
image sel_gwa = "sel_gwa.png"
image sel_rest = "sel_rest.png"
image sel_study = "sel_study.png"

style center_text:
    text_align 0.5

screen phone_icon():
#    frame:
#        xalign 0.34 yalign 0.7
    vbox xalign 0.34 yalign 0.7:
        imagebutton:
            idle "phone"
            hover im.Alpha("phone.png",2)
            action Call("phone")

screen planner_icon():
    vbox xalign 0.64 yalign 0.7:
        imagebutton:
            idle "planner"
            hover im.Alpha("planner.png",2)
            action Call("planner")

screen schedule_button():
    frame:
        xpos 750 yalign 0.5
        xsize 200
        vbox:
            spacing 10

            textbutton "공부하기":
                action Jump("schedule_setup")
#                action Notify("공부했다")

            textbutton "동아리":
                action Notify("동아리 활동했다")

            textbutton "과활동":
                action Notify("과활동했다")

            textbutton "휴식":
                action Notify("쉬었다")

            textbutton "뒤로가기":
                action Notify("뒤로간다...")
                #text_align 0.5

screen schedule_highlight():
    vbox:
        xpos (59+ 99*(day-1)) ypos 307
        add "highlight"

screen schedule_text():
    frame:
        xpos 59+ 99*(day-1) ypos 307
        add "sel_study"

label schedule_setup():
    show screen schedule_text
    show screen schedule_highlight

    return

#start 함수에서 오는 곳
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

    show screen schedule_highlight
    show screen schedule_button
    "하루가 지난다"

    hide screen schedule_button
    $ day += 1
    jump sunday_room

    return


label phone:
    hide screen phone_icon
    hide screen planner_icon
    "핸드폰 화면이 구현되지 않았습니다."
    "일요일 화면으로 돌아갑니다"

    jump sunday_room
    return
