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
    day_schedule = [0,0,0,0,0,0,0]
    tmp_1 = 0
    tmp_2 = 0
    i = 0

# 여기에서부터 게임이 시작합니다.
label start:
    # call what_is_your_name
    show screen hp_show
    show screen one_button_screen

    jump sunday_room

label execute:
    return


label limitation: #아직 구현 안 된 것
    "아직 구현 안 된 것"
    "스케줄 화면\n"
    extend "핸드폰 화면"
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
