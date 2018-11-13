# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#start 함수에서 넘어옴
label sunday_room:
    scene sunday_room_image at truecenter

    $ day = 0
    $ YoIl = day_name[day]
    $ day_for_show = (week-1)*7 + day + 1
    show screen dateShow

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

## 일요일 방에서 핸드폰 아이콘
screen phone_icon():
    vbox :
        xalign 0.34 yalign 0.7
        imagebutton:
            idle "phone_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("phone_icon.png",2)
            # 클릭시 phone label을 실행함
            action Hide("phone_icon"), Hide("planner_icon"), Jump("phone")

## 일요일 방에서 플래너 아이콘
screen planner_icon() :
    vbox xalign 0.64 yalign 0.7 :
        imagebutton:
            idle "planner_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("planner_icon.png",2)
            # 클릭시 planner label을 실행함
            action [Hide("phone_icon"), Hide("planner_icon"),
                    SetVariable("month_for_display", month - 3),
                    SetVariable("day", 1),
                    Hide("dateShow"), Show("hp_show"), Jump("planner")]


# 일요일 방 hp, mental, to-do-list 바
screen sunday_room_UI() :
    ## 일단 여기다가 background 때려 박았음"
    add "hp_background.png"
    add "mental_background.png"
    add "to_do_list.png"
    ##

screen hp_show():
    hbox:
        xpos 972 ypos 300 # 멘탈박스는 344

        # horizon box 각 요소별 스페이싱 10씩
        spacing 10

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
