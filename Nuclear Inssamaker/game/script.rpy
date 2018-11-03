# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image room = im.Scale("room.png",1480,820)
image phone = "phone.png"
image planner = "planner.png"

# 게임에서 사용할 캐릭터를 정의합니다.
#define e = Character('아이린', color="#c8ffc8")
define s = Character('시스템', color="#c8ffc8")

# 변수 선언
init python:
    hp = 72
    day = 1

screen hp_show():
    frame:
        align(0.05,0.05)
        hbox:
            spacing 10
            text "HP" style "button_text" yalign 0.5
            bar value AnimatedValue(hp,100,1.0) yalign 0.5 xsize 200

screen stats_screen():
    frame:
        align(0.95,0.15)
        xysize(180, 100)
        vbox:
            align(0.0, 0.5)
            text "{u}Stats:{/u}"
            null height 10
            text "HP: [hp]"
            null height 10
            text "Day: [day]"

screen one_button_screen():
    textbutton "스탯" action If(renpy.get_screen("stats_screen"), Hide("stats_screen"), Show("stats_screen")) align (0.95, 0.05)

screen phone_button():
#    frame:
#        xalign 0.34 yalign 0.7
    vbox xalign 0.34 yalign 0.7:
        imagebutton:
            idle "phone"
            hover im.Alpha("phone.png",0.3)
            action Jump("phone")

screen planner_button():
    vbox xalign 0.64 yalign 0.7:
        imagebutton:
            idle "planner"
            hover im.Alpha("planner.png",0.3)
            action Jump("planner")

# 여기에서부터 게임이 시작합니다.
label start:
    # call what_is_your_name
    show screen hp_show
    show screen one_button_screen
    show screen phone_button
    show screen planner_button

    scene room at truecenter
    #show phone at topleft #위치 조정이 어려워
    #show planner at topright #위치 조정이 어려워

    s "Hi"
    p "밥을 먹었다. 체력을 회복한다"

    $hp += 10

    s "새로운 렌파이 게임을 만들었군요."


    call limitation #아직 구현 안된 것

    menu :
        "핸드폰":
            call phone

        "플래너":
            call planner

    s "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    return


label limitation: #아직 구현 안된 것
    "핸드폰과 플래너를 버튼으로 만들지 않았습니다"
    "아직 이미지를 위치가 정확하게 놓을 수가 없습니다;"
    return

label phone:
    "핸드폰 화면이 구현되지 않았습니다."
    return

label planner:
    "플래너 화면이 구현되지 않았습니다."
    return

label what_is_your_name:
    s "이름이 무엇인가요?"
    define p = Character("주인공") #[povname]

    python:
        povname = renpy.input("플레이어의 이름을 정해주세요")
        povname = povname.strip()

        if not povname:
            povname = "주인공"

    p "내 이름은 [povname]!"

    return
