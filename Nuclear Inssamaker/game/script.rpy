# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image sunday_room_image = im.Scale("room.png",1480,820)
image bg lecture_room = im.Scale("lecture_room.png",1480,820)
image phone_night = "phone_night.png"

# 게임에서 사용할 캐릭터를 정의합니다.

# 변수 선언
init python:
    hp = 30
    loneliness = 0

    month = 3 # number 0~3 : 3~6월
    month_for_display = month - 3
    week = 1
    day = 0
    day_for_show = (week-1)*7 + day + 1
    day_name = ["일","월","화","수","목","금","토"]
    YoIl = 0

    ktalk_mode = ["friends", "talk"]

    # day_schedule[month - 3][(week-1)*7 + day] 형식(day는 1부터 시작)으로 이용할 것이기 때문에
    day_schedule = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for_day_schedule_select = 0

# 여기에서부터 게임이 시작합니다.
label start:
    # 플레이어 이름을 묻는 함수 what_is_your_name
    # call what_is_your_name

    # 화면 우측 위 '스탯'버튼. 클릭하면 스탯창이 나온다.
    show screen stats_button_screen

    call limitation #아직 구현 안된 것

    "일요일에는.\n"
    extend "핸드폰을 이용해 SNS를 확인하거나,\n"
    extend "플래너를 이용해 다음주 일정을 짜세요."

    # sunday_room_label의 sunday_room label 호출
    jump sunday_room


# label start에서 넘어옴
label limitation:
    "아직 구현 안 된 것 목록입니다.\n첫 주 페이스북 이미지\n카카오톡 하단 버튼"
    return

screen dateShow() :
    add "date.png" xpos 12 ypos 9
    vbox xpos 12 ypos 9 xysize(360, 60) :
        if YoIl != "일" :
            text "{color=#000}[month]월 [day_for_show]일 [YoIl]요일" :
                size 25 xalign 0.3 yalign 0.5
        else :
            text "{color=#000}[month]월 {color=#ff0000}[day_for_show]{color=#000}일 {color=#ff0000}[YoIl]{color=#000}요일" :
                size 25 xalign 0.3 yalign 0.5

# label start에서 넘어옴
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




# label start에서 호출됨
screen stats_button_screen():
    textbutton "스탯" :
        # action : "스탯"버튼이 눌렸을 때 실행할 행동
        # if문 해석 : stats_screen이 켜져있으면 Hide하고, 꺼져있으면 Show해라.
        action If(renpy.get_screen("stats_screen"), Hide("stats_screen"), Show("stats_screen"))

        # 버튼위치, 화면에서 가로방향으로 0.95, 세로방향으로 0.05 비율 되는 곳에 존재
        align (0.95, 0.05)

# label start에서 호출된 stats_button_screen의 텍스트버튼이 눌리면 호출됨

screen stats_screen():
    frame:
        align(0.95,0.15)
#        xysize(180, 100)
        vbox:
            spacing 10
            align(1.0, 0.5)
            text "{u}Stats:{/u}"
            text "HP: [hp]"
            text "Month: [month]"
            text "Week: [week]"
            text "Day: [day]"
