image sunday_room_image = "room.png" #im.Scale("room.png",1480,820)

#start 함수에서 넘어옴
label sunday_room:
    $ day = 0
    if month == 3 and week == 1 and day == 0 :
        python :
             hp = 200
             mental_point = 100

             day_or_evening = "day"

             study_parameter = 0.0
             study_count = 0
             mid_term_grade = 0
             final_term_grade = 0

             club_parameter = 0.0
             club_count = 0
             club_open = False
             gwa_parameter = 0.0
             gwa_count = 0

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

             fbook_post = []
             fbook_count = 0
             #카톡모드 1 = 친구목록, 2 = 대화목록
             ktalk_mode = 1

             # day_schedule[month - 3][(week-1)*8 + day] 형식(day는 1부터 시작)으로 이용할 것이기 때문에
             day_schedule = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    $ hp_for_show = hp
    $ mental_point_for_show = mental_point

    scene sunday_room_image at truecenter

    $ YoIl = day_name[day]
    if day < 7 :
        $ day_for_show = (week-1)*7 + day + 1

    show screen dateShow

    show screen upper_right_UI
    # sunday_room_screen에 있는 핸드폰, 플래너 아이콘을 보여주는 스크린
    show screen phone_icon
    show screen planner_icon

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
                    Hide("dateShow"), Play("sound", "sound/planner_sel.mp3"),
                    Jump("planner")]
