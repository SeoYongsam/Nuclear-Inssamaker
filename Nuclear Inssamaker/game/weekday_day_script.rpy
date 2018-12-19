image lecture_room = "lecture_room.png"

label weekday_day_event :
    $ day_or_evening = "day"
    if month == 3 and week == 1 and day == 3 :
        show lecture_room at truecenter
        "김범준" "안녕하십니까\n"
        extend "언시리어스 게임 강의를 맡은 김범준입니다\n"
        "김범준" "퀴즈는 이번달 넷째주 월요일, 23일에 보겠습니다"
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
        "김범준" "언시리어스게임 퀴즈를 시작하겠습니다"
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

                "최다 표를 얻은 보라색 과잠 선택하기" :
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
        "지난밤 카톡에서 뻔엠 관련 얘기가 나왔습니다.\n"
        "확인해주세요."
        "장발후발 투표 결과 장발대10 / 후발대6\n"
        "투표를 더 진행하시겠습니까?"
        menu :
            "투표 계속하기" :
                "투표를 계속 진행합니다."

            "투표 종료하기" :
                $ fun_mt_vote_finished = True
                # 4/4 전까지 끝냈는가?를 세기 위한 변수
                $ fun_mt_vote_day = (month-3)*28 + (week-1)*7 + day + 1

    elif month == 4 and week == 1 and day == 3 :
        if fun_mt_vote_finished == False :
            "장발후발 투표 결과 장발대 9 / 후발대 11\n"
            "장발대 한명이 후발대로 변경했습니다..투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "투표를 계속 진행합니다."

                "투표 종료하기" :
                    $ fun_mt_vote_finished = True
                    $ fun_mt_vote_day = (month-3)*28 + (week-1)*7 + day + 1

    elif month == 4 and week == 1 and day == 4 :
        if fun_mt_vote_finished == False :
            "장발후발 투표 결과 장발대 8 / 후발대 14\n"
            "점점 장발대가 줄어들고 있습니다.\n"
            "투표를 더 진행하시겠습니까?"
            menu :
                "투표 계속하기" :
                    "투표를 계속 진행합니다."

                "투표 종료하기" :
                    $ fun_mt_vote_finished = True
                    $ fun_mt_vote_day = (month-3)*28 + (week-1)*7 + day + 1

        if gwazam_hidden == True :
            "과잠 업체에서 연락이 와, 오늘 과잠을 받게 되었다."
            "우리 학번만의 과잠을 가지게 되어서인지, 과의 분위기가 좋아졌다."
            $ gwa_parameter += 3
            call parameter_maxmin_check

            if gwazam_store == True :
                "업체를 직접 방문해서 그런지, 옷 핏이 딱 맞아 떨어졌다."
                "친구들이 더욱 만족하는 것 같다. 과 분위기가 더 좋아졌다."
                $ gwa_parameter += 3
                call parameter_maxmin_check

            else :
                "인터넷에서 주문해서 그런지, 옷 핏이 살짝 이상하다."
                "친구들의 만족도가 살짝 떨어진 것 같다. 과 분위기가 약간 안 좋아졌다."
                $ gwa_parameter -= 2
                call parameter_maxmin_check


    elif month == 4 and week == 1 and day == 5 :
        if fun_mt_vote_finished == False :
            "장발후발 투표 결과 장발대 8 / 후발대 14\n"
            "투표가 종료되었습니다."
            $ fun_mt_vote_day = (month-3)*28 + (week-1)*7 + day + 1

        call fun_mt

    elif month == 4 and week == 4 and day == 1 :
        show lecture_room at truecenter
        "중간시험 첫째 날이다. 두근두근 떨린다."
        "{color=#6495ED}문제 : 보기 중 숫자인 것은?{/color}"
        menu :
            "김" :
                "보기 중 숫자인 것은?\n{color=#6495ED}김{/color} / {color=#a33b39}이{/color} / 박"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "이" :
                "보기 중 숫자인 것은?\n김 / {color=#a33b39}이{/color} / 박"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ mid_term_grade += 1

            "박" :
                "보기 중 숫자인 것은?\n김 / {color=#a33b39}이{/color} / {color=#6495ED}박{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

    elif month == 4 and week == 4 and day == 2 :
        show lecture_room at truecenter
        "중간시험 둘째 날이다. 오늘은 잘 볼 수 있을까?"
        if study_parameter >= 2.7 * 6 :
            "{color=#6495ED}문제 : 24절기 중 낮이 가장 짧고 밤이 가장 긴 절기는?{/color}"
        else :
            "{color=#6495ED}문제 : XXXXX X 낮XXX XXX XXX XX XX X XXX?{/color}"
            extend "공부를 덜 했더니 문제를 못 읽겠다..."
        menu :
            "하지" :
                "24절기 중 낮이 가장 짧고 밤이 가장 긴 절기는?\n{color=#6495ED}하지{/color} / 춘분 / {color=#a33b39}동지{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "춘분" :
                "24절기 중 낮이 가장 짧고 밤이 가장 긴 절기는?\n하지 / {color=#6495ED}춘분{/color} / {color=#a33b39}동지{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "동지" :
                "24절기 중 낮이 가장 짧고 밤이 가장 긴 절기는?\n하지 / 춘분 / {color=#a33b39}동지{/color}"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ mid_term_grade += 1

    elif month == 4 and week == 4 and day == 3 :
        show lecture_room at truecenter
        "중간시험 셋째 날이다. 빨리 시험 끝났으면 좋겠다..."
        if study_parameter >= 2.7 * 12 :
            "{color=#6495ED}문제 : 영국의 소설가 골딩이 지은 장편소설은?{/color}"
        else :
            "{color=#6495ED}문제 : XXXX XX가 XXXX XXX XXXX은?{/color}\n"
            extend "공부 좀 할걸... 외계어가 따로 없네..."
        menu :
            "세종대왕" :
                "문제 : 영국의 소설가 골딩이 지은 장편소설은?\n{color=#6495ED}세종대왕{/color} / 염라대왕 / {color=#a33b39}파리대왕{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "염라대왕" :
                "문제 : 영국의 소설가 골딩이 지은 장편소설은?\n세종대왕 / {color=#6495ED}염라대왕{/color} / {color=#a33b39}파리대왕{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "파리대왕" :
                "영국의 소설가 골딩이 지은 장편소설은?\n세종대왕 / 염라대왕 / {color=#a33b39}파리대왕{/color}"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ mid_term_grade += 1

    elif month == 4 and week == 4 and day == 4 :
        show lecture_room at truecenter
        "중간시험 마지막 날이다. 시험 마지막날 개꿀~"
        if study_parameter >= 2.7 * 18 :
            "{color=#6495ED}문제 : 보기 중 농구 선수인 사람은?{/color}"
        else :
            "{color=#6495ED}문제 : XXXXX XXXXX 선수X XXX XXX?{/color}\n"
            extend "하얀 건 종이요 검은 건 글자로다. 공부 안한 업보인가보다..."
        menu :
            "로베르트 레반도프스키" :
                "문제 : 보기 중 농구 선수인 사람은?\n{color=#6495ED}로베르트 레반도프스키{/color} / 표트르 차이콥스키 / {color=#a33b39}더크 노비츠키{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "표트르 차이콥스키" :
                "문제 : 보기 중 농구 선수인 사람은?\n로베르트 레반도프스키 / {color=#6495ED}표트르 차이콥스키{/color} / {color=#a33b39}더크 노비츠키{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "더크 노비츠키" :
                "문제 : 보기 중 농구 선수인 사람은?\n로베르트 레반도프스키 / 표트르 차이콥스키 / {color=#a33b39}더크 노비츠키{/color}"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ mid_term_grade += 1

    elif month == 5 and week == 1 and day == 2 :
        call jangtuh

    elif month == 5 and week == 3 and day == 6 :
        call olympic

    elif month == 6 and week == 3 and day == 1 :
        show lecture_room at truecenter
        "기말 고사 시작했다. 떨린다."
        "{color=#6495ED}문제 : 보기 중 문(Door)과 관련있는 한자성어는?{/color}"
        menu :
            "문전성시" :
                "문제 : 보기 중 문(Door)과 관련있는 한자성어는?\n{color=#a33b39}문전성시{/color} / 동문서답 / 문방사우"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ final_term_grade += 1

            "동문서답" :
                "문제 : 보기 중 문(Door)과 관련있는 한자성어는?\n{color=#a33b39}문전성시{/color} / {color=#6495ED}동문서답{/color} / 문방사우"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "문방사우" :
                "문제 : 보기 중 문(Door)과 관련있는 한자성어는?\n{color=#a33b39}문전성시{/color} / 동문서답 / {color=#6495ED}문방사우{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

    elif month == 6 and week == 3 and day == 2 :
        show lecture_room at truecenter
        "기말 고사 둘째 날이다. 계속 떨린다."
        if study_parameter >= 2.7 * 10 :
            "{color=#6495ED}문제 : 보기 중 목관 악기인 것은?{/color}"
        else :
            "{color=#6495ED}문제 : XXX XXXX XX XXXXXX XXXX 것은?{/color}\n"
            extend "공부를 안해서... 문제를 알아볼 수가 없다."
        menu :
            "손오공" :
                "문제 : 보기 중 목관 악기인 것은?\n{color=#6495ED}손오공{/color} / {color=#a33b39}피콜로{/color} / 베지터"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "피콜로" :
                "문제 : 보기 중 목관 악기인 것은?\n손오공 / {color=#a33b39}피콜로{/color} / 베지터"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ final_term_grade += 1

            "베지터" :
                "문제 : 보기 중 목관 악기인 것은?\n손오공 / {color=#a33b39}피콜로{/color} / {color=#6495ED}베지터{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

    elif month == 6 and week == 3 and day == 3 :
        show lecture_room at truecenter
        "기말 고사 셋째 날이다. 곧 종강이다. 조금만 힘내자"
        if study_parameter >= 2.7 * 20 :
            "{color=#6495ED}문제 : 보기 중 꽃 이름인 것은?{/color}"
        else :
            "{color=#6495ED}문제 : XXX X X 이름X XX X XXXX XXXX XX?{/color}\n"
            extend "공부 좀 더 할걸... 문제를 못 알아보겠네..."
        menu :
            "나루토" :
                "문제 : 보기 중 꽃 이름인 것은?\n{color=#6495ED}나루토{/color} / 사스케 / {color=#a33b39}사쿠라{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "사스케" :
                "문제 : 보기 중 꽃 이름인 것은?\n나루토 / {color=#6495ED}사스케 / {color=#a33b39}사쿠라{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "사쿠라" :
                "문제 : 보기 중 꽃 이름인 것은?\n나루토 / 사스케 / {color=#a33b39}사쿠라{/color}"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ final_term_grade += 1

    elif month == 6 and week == 3 and day == 4 :
        show lecture_room at truecenter
        "기말 고사 마지막날이다. 유종의 미를 거두자."
        if study_parameter >= 2.7 * 30 :
            "{color=#6495ED}문제 : 보기 중 철자가 가장 긴 단어는?{/color}"
        else :
            "{color=#6495ED}문제 : XXX XX XX 가장 XXX XXX?{/color}\n"
            extend "마지막 시험을... 이렇게... 망치는 걸까...?"
        menu :
            "애플" :
                "문제 : 보기 중 철자가 가장 긴 단어는?\n{color=#6495ED}애플{/color} / {color=#a33b39}마이크로소프트{/color} / 아마존"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

            "마이크로소프트" :
                "문제 : 보기 중 철자가 가장 긴 단어는?\n애플 / {color=#a33b39}마이크로소프트{/color} / 아마존"
                "시험 잘 봤다! 행복하다."
                $ mental_point += 10
                $ final_term_grade += 1

            "아마존" :
                "문제 : 보기 중 철자가 가장 긴 단어는?\n애플 / {color=#a33b39}마이크로소프트{/color} / {color=#6495ED}아마존{/color}"
                "시험 문제를 틀렸다... 멘탈이 터졌다."
                $ mental_point -= 10

    elif day == 6 :
        "토요일 낮이 되었다."
        call normal_weekday_evening

    else :
        $ day_or_evening = "evening"

    return
