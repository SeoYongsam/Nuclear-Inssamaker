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
    week = 1
    day = 1
    day_name = [0,"월요일","화요일","수요일","목요일","금요일","토요일"]
    YoIl = 0
    # day_schedule[0]은 사용하지 않음
    # day_schedule[day] 형식(day는 1부터 시작)으로 이용할 것이기 때문에
    day_schedule = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for_day_schedule_select = 0
    i = 0

# 여기에서부터 게임이 시작합니다.
label start:
    # 플레이어 이름을 묻는 함수 what_is_your_name
    # call what_is_your_name

    # 화면 우측 위 '스탯'버튼. 클릭하면 스탯창이 나온다.
    show screen stats_button_screen


    call limitation #아직 구현 안된 것

    # sunday_room_label의 sunday_room label 호출
    jump sunday_room


# label start에서 넘어옴
label limitation:
    "아직 구현 안 된 것 목록입니다. \n"
    extend "핸드폰 화면"
    return

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
            text "Week: [week]"
            text "Day: [day]"

# 무한히 대화창을 없애버리는 기능을 하는 label
label hide_dialouge_box:
    while True :
        window hide
        pause
