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
        $ club_open = True

    elif month == 3 and week == 2 and day == 5 :
        call all_mt

    elif month == 3 and week == 3 and day == 5 :
        # 3/20
        if gwazam_finished == False :
            "과잠 투표 결과"
            "진일이가 제안한 카모-2명\n삼용이가 제안한 보라, 흰색-6명\n장중이가 제안한 검검-8명"
            "투표를 하시겠습니까, 투표를 마치고 과잠을 결정하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "아직 의견이 충분히 모인 것 같지 않다.\n시간을 더 두고 친구들의 의견을 모아보자."
                    # $ gwazam_finished = False

                "최다 표를 얻은 검검 과잠 선택하기" :
                    "친구들이 좋아하는 것 같긴 한데, 너무 빨리 정한 것 같은 느낌이 든다."
                    $ gwa_parameter += 3
                    call parameter_maxmin_check

                    $ gwazam_hidden = True
                    $ gwazam_finished = True

    elif month == 3 and week == 3 and day == 6 :
        # 3/21
        if gwazam_finished == False :
            "과잠 투표 결과"
            "진일이가 제안한 카모-3명\n삼용이가 제안한 보라, 흰색-8명\n장중이가 제안한 검검-10명"
            "투표를 하시겠습니까, 투표를 마치고 과잠을 결정하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "아직 의견이 충분히 모인 것 같지 않다.\n시간을 더 두고 친구들의 의견을 모아보자."
                    # $ gwazam_finished = False

                "최다 표를 얻은 검검 과잠 선택하기" :
                    "의견을 적당히 모은 것 같다. 과 분위기가 좋아진 것 같다."
                    $ gwa_parameter += 6
                    call parameter_maxmin_check

                    $ gwazam_hidden = True
                    $ gwazam_finished = True

    elif month == 3 and week == 4 and day == 1 :
        # 3/23
        if gwazam_finished == False :
            "과잠 투표 결과"
            "진일이가 제안한 카모-5명\n삼용이가 제안한 보라, 흰색-13명\n장중이가 제안한 검검-12명"
            "투표를 하시겠습니까, 투표를 마치고 과잠을 결정하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "아직 의견이 충분히 모인 것 같지 않다.\n시간을 더 두고 친구들의 의견을 모아보자."
                    # $ gwazam_finished = False

                "최다 표를 얻은 보라색 과잠 선택하기" :
                    "오랫동안 의견을 수렴해서 불만이 거의 안나온다. 과 분위기가 많이 좋아졌다."
                    $ gwa_parameter += 10
                    call parameter_maxmin_check

                    $ gwazam_finished = True

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
        # 3/24
        if gwazam_finished == False :
            "과잠 투표 결과"
            "진일이가 제안한 카모-6명\n삼용이가 제안한 보라, 흰색-15명\n장중이가 제안한 검검-13명"
            "투표를 하시겠습니까, 투표를 마치고 과잠을 결정하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "아직 의견이 충분히 모인 것 같지 않다.\n시간을 더 두고 친구들의 의견을 모아보자."
                    # $ gwazam_finished = False

                "최다 표를 얻은 검검 과잠 선택하기" :
                    "다 같이 만족하는 결과가 나왔다. 과 분위기가 아주 아주 좋아졌다."
                    $ gwa_parameter += 7
                    call parameter_maxmin_check

                    $ gwazam_finished = True

    elif month == 3 and week == 4 and day == 3 and gwazam_finished == False :
            "기간이 다 되어서 투표가 마감되었다."
            "다수결에 따라서 보라, 흰색 과잠으로 과잠 디자인이 결정되었다."
            $ gwazam_finished == True

    elif month == 4 and week == 1 and day == 1 :
        call uniform_day

    elif month == 4 and week == 1 and day == 2 :
        "지난밤 카톡에서 뻔엠 장소와 장발후발 관련 얘기가 나왔습니다. 확인해주세요."
        "장소 투표 결과 대별리8 / 신숲8 / 미투표4"
        "투표를 더 진행하시겠습니까?"
        menu :
            "투표 계속하기" :
                "투표를 계속 진행합니다."

            "투표 마치고 결정하기" :
                "투표가 동률이 나왔습니다. 당신은 무엇을 선택하시겠습니까?"
                menu :
                    "장중이와 진일이가 미는 '대별리'" :
                        "투표를 마감했다. 장중이와 진일이가 좋아한다"
                        $ jangjung.parameter += 20
                        $ jinil.parameter += 20

                    "삼용이가 미는 '신숲'" :
                        "투표를 마감했다. 삼용이가 좋아한다."
                        $ samyong.parameter += 20

                call parameter_maxmin_check
                $ fun_mt_location_finished = True

        "장발후발 투표 결과 장발대10 / 후발대6"
        "투표를 더 진행하시겠습니까?"
        menu :
            "투표 계속하기" :
                "투표를 계속 진행합니다."

            "투표 종료하기" :
                $ fun_mt_vote_finished = True
                # 4/4 전까지 끝냈는가?를 세기 위한 변수
                $ fun_mt_vote_day = (month-3)*28 + (week-1)*7 + day + 1

    elif month == 4 and week == 1 and day == 3 :
        if fun_mt_location_finished == False :
            "장소 투표 결과 대별리10 / 신숲10"
            "투표가 동률이 나왔습니다. 당신은 무엇을 선택하시겠습니까?"
            menu :
                "장중이와 진일이가 미는 '대별리'" :
                    "투표를 마감했다. 장중이와 진일이가 좋아한다"
                    $ jangjung.parameter += 20
                    $ jinil.parameter += 20

                "삼용이가 미는 '신숲'" :
                    "투표를 마감했다. 삼용이가 좋아한다."
                    $ samyong.parameter += 20

        if fun_mt_vote_finished == False :
            "장발후발 투표 결과 장발대 9 / 후발대 11"
            "투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "투표를 계속 진행합니다."

                "투표 종료하기" :
                    $ fun_mt_vote_finished = True
                    $ fun_mt_vote_day = (month-3)*28 + (week-1)*7 + day + 1

    elif month == 4 and week == 1 and day == 4 :
        if fun_mt_vote_finished == False :
            "장발후발 투표 결과 장발대 8 / 후발대 14"
            "점점 장발대가 줄어들고 있습니다.\n투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "투표를 계속 진행합니다."

                "투표 종료하기" :
                    $ fun_mt_vote_finished = True
                    $ fun_mt_vote_day = (month-3)*28 + (week-1)*7 + day + 1


    elif month == 4 and week == 1 and day == 5 :
        if fun_mt_vote_finished == False :
            "장발후발 투표 결과 장발대 8 / 후발대 14"
            "투표가 종료되었습니다."

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
