# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

screen phone_button():
#    frame:
#        xalign 0.34 yalign 0.7
    vbox xalign 0.34 yalign 0.7:
        imagebutton:
            idle "phone"
            hover im.Alpha("phone.png",2)
            action Call("phone")

screen planner_button():
    vbox xalign 0.64 yalign 0.7:
        imagebutton:
            idle "planner"
            hover im.Alpha("planner.png",2)
            action Call("planner")

label sunday_room:
    scene room at truecenter

    show screen phone_button
    show screen planner_button

    s "Hi"
    p "밥을 먹었다. 체력을 회복한다"

    $hp += 10

    s "새로운 렌파이 게임을 만들었군요."


    call limitation #아직 구현 안된 것


    menu :
        "핸드폰":
            call phone

        "플래너":
            jump planner

    s "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    return

label phone:
    hide screen phone_button
    hide screen planner_button
    "핸드폰 화면이 구현되지 않았습니다."
    return

label planner:
    hide screen phone_button
    hide screen planner_button    
    "플래너 화면이 구현되지 않았습니다."
    return
