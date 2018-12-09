# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#start 함수에서 넘어옴
label sunday_room:
    $ day = 0
    scene sunday_room_image at truecenter

    $ YoIl = day_name[day]
    $ day_for_show = (week-1)*7 + day + 1

    show screen dateShow

    show screen upper_right_UI
    # sunday_room_screen에 있는 핸드폰, 플래너 아이콘을 보여주는 스크린
    show screen phone_icon
    show screen planner_icon

#    "일요일이 되었습니다.\n"
#    extend "핸드폰을 이용해 SNS를 확인하거나,\n"
#    extend "플래너를 이용해 다음주 일정을 짜세요."
    while True :
        window hide
        pause

    return

## 일요일 방에서 플래너 아이콘
screen planner_icon() :
    vbox xpos 892 ypos 364 :
        imagebutton:
            idle "planner_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover "planner_icon_sel.png" #im.Alpha("planner_icon.png",2)
            # 클릭시 planner label을 실행함
            action [Hide("phone_icon"), Hide("planner_icon"),
                    SetVariable("month_for_display", month - 3),
                    SetVariable("day", 1),
                    Hide("dateShow"), Jump("planner")]
