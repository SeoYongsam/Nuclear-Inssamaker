# 변수 선언
init python:
    import string
    import re
    import random

    hp = 200
    mental_point = 100

    # 게임 시작 시 월, 주, 일
    month = 3
    month_for_display = month - 3
    week = 1
    day = 0

    day_for_show = (week-1)*7 + day + 1
    day_name = ["일","월","화","수","목","금","토","토"]
    YoIl = 0
    day_or_evening = "day"

    study_parameter = 0
    study_count = 0
    club_parameter = 0
    club_count = 0
    club_open = False
    gwa_parameter = 0
    gwa_count = 0

    rand_list_for_katlk_list = [1, 2, 3, 4, 5]

    talk_with_who = "그룹"

    #event용 스위치
    gwazam_finished = False
    gwazam_store = False
    gwazam_hidden = False

    fun_mt_location_finished = False
    fun_mt_vote_finished = False
    # 4월 4일 전까지 투표를 끝냈는가 확인하기 위한 변수
    fun_mt_vote_day = 0
    # 장터 사전이벤트 한 갯수
    jangtuh_pre_event = 0

    class messages :
        def __init__(self) :
            self.message = []
            # self.message_temp = []
            self.new_message_count = 0
            self.parameter = 0
            self.denominator_length = 1.0 #분모
            self.numerator_length = 0.0 #분자

        # messages.add("이름|내용")
        def add(self, data) :
            tmp = data.split("|")

            tmplist = list(tmp[1])
            for i in range (1, len(tmp[1])/17 + 1) :
                tmplist.insert( 17  * ( len(tmp[1])/17 + 1 - i ), "\n")
            if tmplist[len(tmplist) - 1] == "\n" :
                del tmplist[len(tmplist) - 1]
            tmp[1] = ''.join(tmplist)

            if tmp[0] == "주인공" :
                self.denominator_length += 44 + tmp[1].count("\n") * 24

            elif tmp[0] == "연속":
                self.denominator_length += 44 + tmp[1].count("\n") * 24

            elif tmp[0] == "날짜":
                self.denominator_length += 44

            else :
                self.denominator_length += 75 + tmp[1].count("\n") * 24

            self.message.extend([[tmp[0], tmp[1]]])
#            self.message_temp.extend([[tmp[0], tmp[1]]])

            if tmp[0] != "날짜" and tmp[0] != "주인공" :
                self.new_message_count += 1

        def reset(self) :
            del self.message[:]

        #def reset_temp(self) :
        #    del self.message_temp[:]

    #클래스 테스트2
    #캐릭터 일람 : 장중, 삼용, 현재, 동아, 진일, 미래, 주인공
    grouptalk = messages()
    jangjung = messages()
    samyong = messages()
    hyunjae = messages()
    jinil = messages()
    dongah = messages()

    fbook_post = []
#    fbook_count = 0

    def fbook_post_add(data) :
        fbook_count_tmp = 0
        tmp = data.split("|")
#        if week > 1 or month > 3:
#            del fbook_post[0]
#            while fbook_post[0] != "본문" :
#                del fbook_post[0]
        if tmp[0] == "본문" :
            tmplist = list(tmp[3])
            for i in range (1, len(tmp[3])/21 + 1) :
                tmplist.insert( 21  * ( len(tmp[3])/21 + 1 - i ), "\n")
            if tmplist[len(tmplist) - 1] == "\n" :
                del tmplist[len(tmplist) - 1]
            tmp[3] = ''.join(tmplist)

            fbook_post.extend([[tmp[0], tmp[1], tmp[2], tmp[3]]])
#            fbook_count_tmp += 1
#            fbook_count = fbook_count_tmp

        elif tmp[0] == "댓글" :
            tmplist = list(tmp[2])
            for i in range (1, len(tmp[2])/21 + 1) :
                tmplist.insert( 21  * ( len(tmp[2])/21 + 1 - i ), "\n")
            if tmplist[len(tmplist) - 1] == "\n" :
                del tmplist[len(tmplist) - 1]
            tmp[2] = ''.join(tmplist)

            fbook_post.extend([[tmp[0], tmp[1], tmp[2]]])
        else :
            fbook_post.extend([[tmp[0]]])


    #카톡모드 1 = 친구목록, 2 = 대화목록
    ktalk_mode = 1

    # day_schedule[month - 3][(week-1)*8 + day] 형식(day는 1부터 시작)으로 이용할 것이기 때문에
    day_schedule = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for_day_schedule_select = 0


# 여기에서부터 게임이 시작합니다.
label start:
    # 플레이어 이름을 묻는 함수 what_is_your_name
    # call what_is_your_name

    # 화면 우측 위 '스탯'버튼. 클릭하면 스탯창이 나온다.
    show screen stats_button_screen

    Player "으으 머리야...분명히 금요일에 병샷을 한 것 까지는 기억나는데..."
    Player "아 핸드폰 어딨지?\n"
    extend "핸드폰 한 번 확인해봐야겠다."

    "일요일에는\n핸드폰을 이용해 SNS를 확인하거나\n달력를 이용해 다음주 일정을 짜세요."

    call change_SNS
    call event_schedule_set

    # sunday_room_label의 sunday_room label 호출
    jump sunday_room


# label start에서 넘어옴
label limitation:
    "아직 구현 안 된 것 목록입니다.\n첫 주 페이스북 이미지\n카카오톡 하단 버튼"
    return

screen dateShow() :
    add "date.png" xpos 12 ypos 9
    hbox xpos 12 ypos 9 xysize(360, 60) :
        if YoIl != "일" :
            text "{color=#000}[month]월 [day_for_show]일 [YoIl]요일" :
                size 25 xalign 0.8 yalign 0.5
        else :
            text "{color=#000}[month]월 [day_for_show]{color=#000}일 {color=#ff0000}[YoIl]요일{color=#000}" :
                size 25 xalign 0.8 yalign 0.5
        if day_or_evening == "day" :
            add "date_day.png" xalign 0.1 yalign 0.5
        else :
            add "date_evening.png" xalign 0.1 yalign 0.5

# 일요일 방 hp, mental, to-do-list 바
screen upper_right_UI() :
    ## 일단 여기다가 background 때려 박았음"
    add "parameter_UI.png"
    vbox :
        xpos 1016 ypos 16
        xsize 244 ysize 28
        bar value AnimatedValue(244*hp/200, 244, 0.5) style "HP_bar"

    vbox :
        xpos 1016 ypos 64
        xsize 244 ysize 28
        bar value AnimatedValue(244*mental_point/100, 244, 0.5) style "MP_bar"

    #add im.Scale("HP_bar.png", 244*hp/200, 28) xpos 1016 ypos 16
    #add im.Scale("MP_bar.png", 244*(mental_point)/100, 28) xpos 1016 ypos 64
    vbox :
        xpos 992 ypos 180
        xsize 52 ysize 4
        bar value AnimatedValue(52*study_parameter/100 , 52, 0.5) style "bar"

    vbox :
        xpos 1092 ypos 180
        xsize 52 ysize 4
        bar value AnimatedValue(52*gwa_parameter/100 , 52, 0.5) style "bar"

    vbox :
        xpos 1192 ypos 180
        xsize 52 ysize 4
        bar value AnimatedValue(52*club_parameter/100 , 52, 0.5) style "bar"

    #add im.Scale("parameter_bar.png", 52*(study_parameter)/100, 4) xpos 992 ypos 180
    #add im.Scale("parameter_bar.png", 52*(gwa_parameter)/100, 4) xpos 1092 ypos 180
    #add im.Scale("parameter_bar.png", 52*(club_parameter)/100, 4) xpos 1192 ypos 180


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
            text "멘탈: [mental_point]"
            text "Month: [month]"
            text "Week: [week]"
            text "Day: [day]"
            text "공부: [study_parameter]"
            text "동아리: [club_parameter]"
            text "과: [gwa_parameter]"
            text "삼용: [samyong.parameter]"
            text "진일: [jinil.parameter]"
            text "장중: [jangjung.parameter]"

label parameter_maxmin_check :
    if hp < 0 :
        $ hp = 0
    elif hp > 200 :
        $ hp = 200

    if mental_point < 0 :
        $ mental_point = 0
    elif mental_point > 100 :
        $ mental_point = 100

    if study_parameter < 0 :
        $ study_parameter = 0
    elif study_parameter > 100 :
        $ study_parameter = 100

    if club_parameter < 0 :
        $ club_parameter = 0
    elif club_parameter > 100 :
        $ club_parameter = 100

    if gwa_parameter < 0 :
        $ gwa_parameter = 0
    elif gwa_parameter > 100 :
        $ gwa_parameter = 100

    if jangjung.parameter < 0 :
        $ jangjung.parameter = 0
    elif jangjung.parameter > 100 :
        $ jangjung.parameter = 100

    if samyong.parameter < 0 :
        $ samyong.parameter = 0
    elif samyong.parameter > 100 :
        $ samyong.parameter = 100

    if jinil.parameter < 0 :
        $ jinil.parameter = 0
    elif jinil.parameter > 100 :
        $ jinil.parameter = 100

    if dongah.parameter < 0 :
        $ dongah.parameter = 0
    elif dongah.parameter > 100 :
        $ dongah.parameter = 100

define Player = Character("주인공", color="#ffcccc", image="Player")
image side Player :
    "character/cha_player.png"

define Jinil = Character("진일", color="#ffcccc", image="Jinil")#, window_left_padding = -100)
image side Jinil :
    "character/cha_jinil.png"

define Jangjung = Character("장중", color="#ffcccc", image="Jangjung")
image side Jangjung :
    "character/cha_jangjung.png"

define Samyong = Character("삼용", color="#ffcccc", image="Samyong")
image side Samyong :
    "character/cha_samyong.png"

define Daehyun = Character("대현", color="#ffcccc", image="Daehyun")
image side Daehyun :
    "character/cha_daehyun.png"

define Hyunjae = Character("현재", color="#ffcccc", image="Hyunjae")
image side Hyunjae :
    "character/cha_hyunjae.png"

define Mirae = Character("미래", color="#ffcccc", image="Mirae")
image side Mirae :
    "character/cha_mirae.png"

define Dongah = Character("동아", color="#ffcccc", image="Dongah")
image side Dongah :
    "character/cha_dongah.png"

define Ohduck = Character("덕현", color="#ffcccc", image="Ohduck")
image side Ohduck :
    "character/cha_ohduck.png"

define Geumji = Character("금지", color="#ffcccc", image="Geumji")
image side Geumji :
    "character/cha_geumji.png"
