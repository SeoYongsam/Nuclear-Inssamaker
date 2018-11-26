# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image sunday_room_image = im.Scale("room.png",1480,820)
image phone_night = "phone_night.png"

# 게임에서 사용할 캐릭터를 정의합니다.

# 변수 선언
init python:
    import string
    hp = 200
    loneliness = 0

    month = 3 # number 0~3 : 3~6월
    month_for_display = month - 3
    week = 1
    day = 0
    day_for_show = (week-1)*7 + day + 1
    day_name = ["일","월","화","수","목","금","토"]
    YoIl = 0


    talk_with_who = "그룹"
#클래스 테스트1
    class messages :
        def __init__(self) :
            self.message = []
            self.new_message_count = 0
            self.new_message_watch = False

        def add(self, data) :
            tmp = data.split("|")
            self.message.extend([[tmp[0], tmp[1]]])

        def reset(self) :
            del self.message[:]

#클래스 테스트2
# 캐릭터 일람 : 장중, 삼용, 현재, 동아, 진일, 미래, 주인공, 0, 1
    grouptalk = messages()
    grouptalk.message = [["날짜","3월 1일 일요일"],
                ["장중", "드디어 내일 개강 ㅋㅋㅋ"], ["삼용", "완전 설렌다 ㅋㅋㅋ"],
                ["현재", "나는 미래랑 내일 수업 두 개 ㅋㅋㅋ"], ["장중", "근데 나 주 2야 ㅋㅋㅋㅋ"],
                ["진일", "선배랑 밥먹으려고 오냐 ㅋㅋㅋ"], ["미래", "와ㅋㅋㅋ 장중이 뭐야"],
                ["장중", "ㅎㅎㅎ 내가 위너"], ["삼용", "나도 저렇게 해서 중국다녀올걸ㅠ"],
                ["주인공", "우리 내일 입학식에서 사진찍자!!"], ["진일", "콜콜"],
                ["장중", "근데 어제 내가 구글링해봤거든 ㅋㅋㅋ\n현재 수능만점이던데 ㅋㅋㅋ"], ["미래", "진짜???"],
                ["장중", "헐 대박이다..."], ["미래", "그치 ㅋㅋㅋㅋㅋ"],
                ["현태", "진짜 설렌다 ㅋㅋㅋ 대학생이라니"], ["삼용", "난 좀 걱정되는데ㅠㅠ\n모르는 것 많이 알려줘"],
                ["주인공", "당연하지 ㅋㅋㅋ 다들 내일 봐!"]]

    jangjung = messages()
    jangjung.message = [["날짜","3월 1일 일요일 뾰로롱"],
                ["장중", "안녕\n테스트를해보겠다"], ["주인공", "안녕\n퓨우우우우우우우우우우전"]]
    jangjung.add("장중|어쩌구저쩌구")


    samyong = messages()
    samyong.message = [["날짜","3월 1일 일요일 뾰로롱"],
                ["삼용", "안녕\n테스트를해보겠다"]]

    hyunjae = messages()
    hyunjae.message = [["날짜","3월 1일 일요일 뾰로롱"],
                ["현재", "안녕\n테스트를해보겠다"]]

    jinil = messages()
    jinil.message = [["날짜","3월 1일 일요일 뾰로롱"],
                ["진일", "안녕\n테스트를해보겠다"]]

    dongah = messages()
    dongah.message = [["날짜","3월 1일 일요일 뾰로롱"],
                ["동아", "안녕\n테스트를해보겠다"]]

    study_parameter = 0
    club_parameter = 0
    gwa_parameter = 0

    #카톡모드 1 = 친구목록, 2 = 대화목록
    ktalk_mode = 1

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

# 일요일 방 hp, mental, to-do-list 바
screen always_except_planner_UI() :
    ## 일단 여기다가 background 때려 박았음"
    add "hp_background.png"
    add "mental_background.png"
    add "to_do_list.png"
    ##

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
screen stats_button_screen() :
    textbutton "스탯" :
        # action : "스탯"버튼이 눌렸을 때 실행할 행동
        # if문 해석 : stats_screen이 켜져있으면 Hide하고, 꺼져있으면 Show해라.
        action If(renpy.get_screen("stats_screen"), Hide("stats_screen"), Show("stats_screen"))

        # 버튼위치, 화면에서 가로방향으로 0.95, 세로방향으로 0.05 비율 되는 곳에 존재
        align (0.95, 0.05)

# label start에서 호출된 stats_button_screen의 텍스트버튼이 눌리면 호출됨

screen stats_screen() :
    frame:
        align(0.05,0.25)
#        xysize(180, 100)
        vbox:
            spacing 3
            align(1.0, 0.5)
            text "{u}Stats:{/u}"
            text "체력: [hp]"
            text "외로움: [loneliness]"
            text "Month: [month]"
            text "Week: [week]"
            text "Day: [day]"
            text "공부: [study_parameter]"
            text "동아리: [club_parameter]"
            text "과: [gwa_parameter]"

label parameter_maxmin_check :
    if hp < 0 :
        $ hp = 0

    if hp > 200 :
        $ hp = 200

    if loneliness < 0 :
        $ loneliness = 0

    if loneliness > 100 :
        $ loneliness = 100

    if study_parameter < 0 :
        $ study_parameter = 0

    if study_parameter > 100 :
        $ study_parameter = 100

    if club_parameter < 0 :
        $ club_parameter = 0

    if club_parameter > 100 :
        $ club_parameter = 100

    if gwa_parameter < 0 :
        $ gwa_parameter = 0

    if gwa_parameter > 100 :
        $ gwa_parameter = 100
