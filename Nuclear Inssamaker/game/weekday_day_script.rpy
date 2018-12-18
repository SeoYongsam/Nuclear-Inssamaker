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

    elif month == 3 and week == 3 and day == 2 :
        #3/17
        #month = 3, week = 3, day = 2
        "오늘은 과잠준비위원회의 첫 회의가 있는 날이다."
        "과준위를 모아 디자인을 토의해보기로 했다."

        scene black
        Player "과잠준비위원회에 지원해주셔서 감사합니다! 그럼 빠르게 디자인부터 받아볼게요!"
        Jinil "카모로 하면 멋있을 것 같다 ㅋㅋㅋ"
        Samyong "나는 빨간색에 용무늬가 들어갔으면 좋겠는데 ㅋㅋㅋ"
        Jangjung "내가 봤을때는 그냥 검검이 제일 무난해 보이는데?"
        Player "오 다들 그래도 한 가지씩은 생각해왔네"
        Player "음 일단 그래도 좀 더 생각을 해보고.."
        Samyong "그럼 실제로 업체랑 디자인 회의 같은 것 해보는 건 어때?"
        Jangjung "오 나도 찬성이야!"
        Jinil "아 무슨 귀찮게 업체까지 가냐..요새는 인터넷으로 그냥 하면 돼!"
        Player "음...어떻게 하지..?"

        menu:
            "디자인도 볼 겸 장중이와 삼용이 말대로 업체를 방문한다." :
                Player "그래도 직접 보는게 낫겠지, 업체 한 번 가보자!"
                Samyong "좋아! 그럼 바로 예약해볼게"
                Jangjung "내일 바로 가자!"

                "삼용, 장중이와의 관계가 좋아진 것 같다."
                "3/18의 일정이 업체 방문으로 교체 되었다."

                #삼용, 장중 파라미터 증가, 3/18 일정 교체, 업체 방문 여부 ㅇ
                $ samyong.parameter += 20
                $ jangjung.parameter += 20
                $ gwazam_store = True

            "그럴 시간 없다. 그냥 인터넷으로 주문한다" :
                Player "에이 요새 인터넷도 좋은데, 찾아갈 시간 없어."
                Player "바로 주문하자"
                Jinil "좋지 좋지!"

                "진일이와의 관계가 좋아진 것 같다."

                #진일 파라미터 증가, 업체 방문 여부 x
                $ jinil.parameter += 20
                $ gwazam_store = False

    elif month == 3 and week == 3 and day == 3 and gwazam_store == True :
        # 3/18
        # month = 3, week = 3, day = 3
        # 업체 방문 안할 경우, 정한 일정, 업체 방문 할 경우 아래의 스크립트.
            "삼용, 장중이와 과잠 업체를 찾아가기로 했다."

            "업체 주인" "아니 요즘 그런 핏은 잘 안살고. @#$@$#"
            Player "아 그래요..? 그럼 이건 어때요??"
            "업체 주인" "그건...@#$@#$"

            "업체 주인과의 얘기를 통해서 \n과잠을 어떻게 맞출지에 대한 방향성을 잡을 수 있었다."


    elif month == 3 and week == 3 and day == 4 :
        # 3/19
        # month = 3, week = 3, day = 4
        # 과잠 최종안 (내부에서 결정할지, 과에서 투표를 돌릴 지 결정)
        Player "자 그럼 최종도안을 결정해 보자!"
        Jinil "나는 전에도 말했던 것 처럼 카모!!"
        Samyong "나는 용무늬가 좋긴한데, 너무 튈것 같으니까 그냥 몸통 보라색, 팔 흰색으로 할게!"
        Jangjung "깔끔하게 검검이 낫지 않겠음? 검검으로 할게!"

        scene black
        "디자인 초안이 총 세 개가 나왔다. \n여기서 결정을 할까, 친구들에게 투표를 받을까..?"
        menu:
            "여기서 결정 한다.":
                #이것을 선택하면 투표를 하지 않기 때문에 자동으로 히든 조건 달성.
                $ gwazam_hidden = True
                $ gwazam_finished = True
                Player "애들이 우리한테 과잠 위임했으니까, 이대로 주문하자!"
                "그렇다면 어떤것을 결정할까?"
                menu:
                    "진일이가 제안한 카모":
                        Player "나도 카모가 좋아!"
                        Jinil "크 역시 뻔대, 안목이 있어~"

                        "진일이와의 관계가 좋아진 것 같다."
                        #진일 파라미터 업, 허나 너무 튀는 과잠이어서 과 파라미터 -10.
                        $ jinil.parameter += 20

                        "과 친구들에게 결정된 과잠 디자인을 보여주었다."
                        "생각보다 반응이 싸늘했다..분위기가 살짝 안 좋아진것 같다.."
                        $ gwa_parameter -= 2
                        call parameter_maxmin_check

                    "삼용이가 제안한 보라, 흰색":
                        Player "보라 흰색이 제일 예쁠 것 같아~"
                        Samyong "맞아맞아 엄청 예쁠듯!!"

                        "삼용이와의 관계가 좋아진 것 같다."
                        #삼용 파라미터 업, 디자인도 괜찮아서 과 파라미터 +20
                        $ samyong.parameter += 20

                        "과 친구들에게 결정된 과잠 디자인을 보여주었다."
                        "열렬한 반응이 돌아왔다! 과 친구들 모두 마음에 들어하는 것 같다!"
                        $ gwa_parameter += 4
                        call parameter_maxmin_check

                    "장중이가 제안한 검검":
                        Player "제일 무난한 건 검검이지!"
                        Jangjung "인정~ 뭘 입든 잘 어울릴듯!"

                        "장중이와의 관계가 좋아진 것 같다."
                        #장중 파라미터 업, 디자인도 나쁘지 않아서 과 파라미터 +10
                        $ jangjung.parameter += 20

                        "과 친구들에게 결정된 과잠 디자인을 보여주었다."
                        "별다른 반응이 없지만, 과잠을 맞춘 것 만으로도 만족하는 분위기이다."
                        $ gwa_parameter += 4
                        call parameter_maxmin_check

            "과 친구들에게 투표를 받는다.":
                # $ gwazam_finished = False
                Player "으음 여기서 바로 결정하는 것은 어렵겠지?"
                Player "애들한테 투표로 물어보자!"
                Jinil "그러지 뭐, 분명 내 디자인이 뽑히겠지!"
                Samyong "아니야 내 디자인이 뽑힐 듯?"
                Jangjung "잘 모르네, 검검이 갑임 ㅋㅋㅋㅋ"
                Player "ㅋㅋㅋㅋ 일단 친구들에게 물어보자"


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

                "최다 표를 얻은 검검 과잠 선택하기" :
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
