image lecture_room = "lecture_room.png"
label weekday_day_event :
    $ day_or_evening = "day"
    if month == 3 and week == 1 and day == 3 :
        show lecture_room at truecenter
        "김범준" "안녕하십니까. 언시리어스 게임 강의를 맡은 김범준입니다.!@#$!@#"
        "김범준" "퀴즈는 이번달 넷째주 월요일, 23일에 보겠습니다."
        Player "퀴즈 대비해서 공부를 열심히 해야겠다"

    elif month == 3 and week == 2 and day == 1 :
        call dongsoze

    elif month == 3 and week == 2 and day == 5 :
        call all_mt

    elif month == 3 and week == 3 and day == 4 :
        "과잠 투표 결과 : 1안-8명 / 2안-6명 / 3안-4명"
        "투표를 하시겠습니까, 과잠을 결정하시겠습니까?"
        menu :
            "투표 계속하기" :
                ""

            "투표 마치고 강제로 선택하기" :
                "어떤 과잠을 선택하시겠습니까?"
                menu :
                    "1안" :
                        ""
                    "2안" :
                        ""
                    "3안" :
                        ""
                $ gwa_jam_finished = True


    elif month == 3 and week == 3 and day == 5 :
        if gwa_jam_finished == False :
            "과잠 투표 결과 : 1안-11명 / 2안-8명 / 3안-5명"
            "투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    ""

                "투표 마치고 강제로 선택하기" :
                    "어떤 과잠을 선택하시겠습니까?"
                    menu :
                        "1안" :
                            ""
                        "2안" :
                            ""
                        "3안" :
                            ""
                    $ gwa_jam_finished = True


    elif month == 3 and week == 3 and day == 6 :
        if gwa_jam_finished == False :
            #"과잠 투표 결과 : 1안-11명 / 2안-8명 / 3안-5명"
            "투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    ""

                "투표 마치고 강제로 선택하기" :
                    "어떤 과잠을 선택하시겠습니까?"
                    menu :
                        "1안" :
                            ""
                        "2안" :
                            ""
                        "3안" :
                            ""
                    $ gwa_jam_finished = True

    elif month == 3 and week == 4 and day == 1 :
        if gwa_jam_finished == False :
            #"과잠 투표 결과 : 1안-11명 / 2안-8명 / 3안-5명"
            "투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    ""

                "투표 마치고 강제로 선택하기" :
                    "어떤 과잠을 선택하시겠습니까?"
                    menu :
                        "1안" :
                            ""
                        "2안" :
                            ""
                        "3안" :
                            ""
                    $ gwa_jam_finished = True

        scene black with dissolve
        show lecture_room at truecenter
        "김범준" "언시리어스게임 퀴즈를 시작하겠습니다."
        "김범준" "초성퀴즈!"
        "김범준" "ㅅㅂ"
        Player "퀴즈가 너무 어려웠다."
        if study_parameter < 34 :
            extend "그래서 망친 것 같다."
            # 멘탈 하락
            "멘탈이 터졌다"
            $ mental_point -= 40

        elif study_parameter < 67 :
            extend "그렇지만 공부를 조금 해서 그럭저럭 봤다."
            # 멘탈 일정

        else :
            extend "그렇지만 공부를 겁나 열심히 했었기 때문에 상쾌하게 잘 봤다."
            # 멘탈 증가
            "기분이 좋아졌다."
            $ mental_point += 30

    elif month == 3 and week == 4 and day == 2 :
        if gwa_jam_finished == False :
            #"과잠 투표 결과 : 1안-11명 / 2안-8명 / 3안-5명"
            "투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    ""

                "투표 마치고 강제로 선택하기" :
                    "어떤 과잠을 선택하시겠습니까?"
                    menu :
                        "1안" :
                            ""
                        "2안" :
                            ""
                        "3안" :
                            ""
                    $ gwa_jam_finished = True

    elif month == 4 and week == 1 and day == 1 :
        call uniform_day

    elif month == 4 and week == 1 and day == 2 :
        "장소 투표 결과 대별리8 / 신숲8 / 보류4"
        "투표를 더 진행하시겠습니까?"
        menu :
            "투표 계속하기" :
                ""

            "투표 마치고 결정하기" :
                "투표가 동률이 나왔습니다. 당신은 무엇을 선택하시겠습니까?"
                menu :
                    "대별리" :
                        ""
                    "신숲" :
                        ""

        "장발후발 투표 결과 장발대10 / 후발대6"
        "투표를 더 진행하시겠습니까?"
        menu :
            "투표 계속하기" :
                ""

            "투표 마치고 결정하기" :
                ""

    elif month == 4 and week == 1 and day == 5 :
        call fun_mt

    elif month == 5 and week == 1 and day == 2 :
        call jangtuh

    elif month == 5 and week == 2 and day == 2 :
        call han_river

    elif month == 5 and week == 3 and day == 6 :
        call olympic

    elif day == 6 :
        "토요일 낮이 되었다."
        call normal_weekday_evening

    else :
        $ day_or_evening = "evening"

    return
