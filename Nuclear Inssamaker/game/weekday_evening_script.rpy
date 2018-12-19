image study :
    "study/1.png"
    pause 0.3
    "study/2.png"
    pause 0.3
    repeat

image club_thur :
    "club/1.png"
    pause 0.3
    "club/2.png"
    pause 0.3
    repeat

image club :
    "club/3.png"
    pause 0.3
    "club/4.png"
    pause 0.3
    repeat

image gwa :
    "gwa/1.png"
    pause 0.3
    "gwa/2.png"
    pause 0.3
    repeat

image rest :
    "rest/1.png"
    pause 0.3
    "rest/2.png"
    pause 0.3
    repeat

label weekday_evening_event :
    $ day_or_evening = "evening"

    if month == 3 and week == 2 and day == 4 :
        call club_first from _call_club_first

    elif month == 3 and week == 3 and day == 2 :
        #3/17
        #month = 3, week = 3, day = 2
        "오늘은 과잠준비위원회의 첫 회의가 있는 날이다."
        "과준위를 모아 디자인을 토의해보기로 했다."

        scene black
        Player "과잠준비위원회에 지원해주셔서 감사합니다!\n"
        extend "그럼 빠르게 디자인부터 받아볼게요!"
        Jinil "카모로 하면 멋있을 것 같다 ㅋㅋㅋ"
        Samyong "나는 빨간색에 용무늬가 들어갔으면 좋겠는데 ㅋㅋㅋ"
        Jangjung "내가 봤을때는 그냥 검검이 제일 무난해 보이는데?"
        Player "오 다들 그래도 한 가지씩은 생각해왔네\n"
        extend "음 일단 그래도 좀 더 생각을 해보고.."
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
                $ day_schedule[0][19] = 5

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
                        call parameter_maxmin_check from _call_parameter_maxmin_check_45

                    "삼용이가 제안한 보라, 흰색":
                        Player "보라 흰색이 제일 예쁠 것 같아~"
                        Samyong "맞아맞아 엄청 예쁠듯!!"

                        "삼용이와의 관계가 좋아진 것 같다."
                        #삼용 파라미터 업, 디자인도 괜찮아서 과 파라미터 +20
                        $ samyong.parameter += 20

                        "과 친구들에게 결정된 과잠 디자인을 보여주었다."
                        "열렬한 반응이 돌아왔다! 과 친구들 모두 마음에 들어하는 것 같다!"
                        $ gwa_parameter += 4
                        call parameter_maxmin_check from _call_parameter_maxmin_check_46

                    "장중이가 제안한 검검":
                        Player "제일 무난한 건 검검이지!"
                        Jangjung "인정~ 뭘 입든 잘 어울릴듯!"

                        "장중이와의 관계가 좋아진 것 같다."
                        #장중 파라미터 업, 디자인도 나쁘지 않아서 과 파라미터 +10
                        $ jangjung.parameter += 20

                        "과 친구들에게 결정된 과잠 디자인을 보여주었다."
                        "별다른 반응이 없지만, 과잠을 맞춘 것 만으로도 만족하는 분위기이다."
                        $ gwa_parameter += 4
                        call parameter_maxmin_check from _call_parameter_maxmin_check_47

            "과 친구들에게 투표를 받는다.":
                # $ gwazam_finished = False
                Player "으음 여기서 바로 결정하는 것은 어렵겠지?\n"
                extend "애들한테 투표로 물어보자!"
                Jinil "그러지 뭐, 분명 내 디자인이 뽑히겠지!"
                Samyong "아니야 내 디자인이 뽑힐 듯?"
                Jangjung "잘 모르네, 검검이 갑임 ㅋㅋㅋㅋ"
                Player "ㅋㅋㅋㅋ 일단 친구들에게 물어보자"

    elif month == 4 and week == 2 and day == 3 :
        call pcbang from _call_pcbang

    elif month == 4 and week == 3 and day == 1 :
        call festival from _call_festival

    elif month == 4 and week == 4 and day == 2 :
        "장터 관련해서 카톡에서 얘기가 나오고 있다. 확인해보자."
        #4월 24일 포스터 회의
        scene black
        "오늘은 장터 준비위원회끼리 모여서 포스터 디자인을 하기로 했다."

        "내가 없어도 회의가 잘 돌아갈 것 같지만...\n갈까 말까?"

        menu:
            "회의에 참여한다":
                $ day_schedule[1][26] = 5
                "회의에 참여했다."

                show poster at truecenter

                "포스터 디자인은 심플하게 가기로 했다."
                "사실 심플 할지는 모르겠지만 포토샵을 다룰 줄 아는 현재가 알아서 하기로 했다."
                "워낙 회의가 잘 진행돼서 내가 안왔어도 됐으려나 싶지만 그래도 마음은 조금 놓인다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening from _call_normal_weekday_evening_3

    elif month == 4 and week == 4 and day == 3 :
        #4월 25일 예산 및 메뉴 정하기
        scene black
        "오늘은 장터 준비위원회끼리 모여서 예산 및 메뉴를 정하기로 했다."

        "내가 없어도 회의가 잘 돌아갈 것 같지만...\n갈까 말까?"
        menu:
            "회의에 참여한다":
                $ day_schedule[1][27] = 5
                "회의에 참여했다."

                show meeting at truecenter

                "예산은 적당하게 50만원으로 잡았다."
                "메뉴는 다른 장터와 차별을 두고 싶었지만 예산에 맞춰 재료를 준비해야했기\n때문에 파전과 치킨너겟 등 기존 장터들과 비슷하게 메뉴를 정했다."
                "오늘 회의에 와서 다행이라고 생각한다."
                "애들이 열정이 많아서인지 무모해서인지는 모르겠지만 메뉴를 정할때 회의가 산으로 갈 뻔한 적이 많았다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening from _call_normal_weekday_evening_4

    elif month == 4 and week == 4 and day == 4 :
        #4월 26일 메뉴판 만들기
        scene black
        "오늘은 장터 준비위원회끼리 모여서 메뉴판을 만들기로 했다."

        "내가 없어도 메뉴판을 잘 만들 것 같지만...\n갈까 말까?"

        menu:
            "회의에 참여한다":
                $ day_schedule[1][28] = 5
                "회의에 참여했다."

                show menu_pan at truecenter
                "메뉴판은 정말 쉽게 정했다.\n"
                "이미 메뉴를 정했기 때문에 장터날에 붙일 것만 만들면 됐기 때문이다."
                "오늘은 회의 보다는 메뉴판 디자인을 했디 때문에 내가 안왔어도 됐으려나 싶지만 그래도 마음은 조금 놓인다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening from _call_normal_weekday_evening_5

    elif month == 5 and week == 1 and day == 1 :
        scene black
        "오늘은 장터 준비위원회끼리 장터 전날 모여서 장을 보기로 했다."

        "내가 없어도 장을 잘 볼 수 있을지 의심스럽지만...\n갈까 말까?"

        menu:
            "장을 보러 간다":
                $ day_schedule[1][29] = 5
                "장을 보러 갔다."

                show shopping at truecenter
                "알고보니 오늘은 내가 장을 꼭 보러 왔어야 했다.\n"
                "애들의 상태가 의심스럽기 때문이다."
                "중간고사가 끝난지 얼마 안돼서 모든 것을 놓은 것만 같다."
                "장터 재료를 사는 것 보다 애들은 자신이 필요한 것들에 더 눈이 가는 것 같다."
                "다행이 나라도 정신을 차리고 장터에 필요한 도구와 음식을 샀다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening from _call_normal_weekday_evening_6

    elif month == 5 and week == 2 and day == 2 :
        call han_river from _call_han_river

    elif month == 5 and week == 3 and day == 1 :
        call karaoke from _call_karaoke

    elif month == 6 and week == 1 and day == 5 :
        call club_concert from _call_club_concert

    else :
        call normal_weekday_evening from _call_normal_weekday_evening_7

    return




label normal_weekday_evening :
    if day_schedule[month - 3][(week - 1) * 8 + day] == 1:
        call evening_study from _call_evening_study

    elif day_schedule[month - 3][(week - 1) * 8 + day] == 2:
        call evening_club from _call_evening_club

    elif day_schedule[month - 3][(week - 1) * 8 + day] == 3:
        call evening_gwa from _call_evening_gwa

    elif day_schedule[month - 3][(week - 1) * 8 + day] == 4:
        call evening_rest from _call_evening_rest

    else :
        extend "에러"

    stop sound
    return

label evening_study:
    show study at truecenter
    play sound "sound/study.mp3"
    if (month == 4 and week == 3 and day >= 5) or (month == 4 and week == 4 and day <= 4) or (month == 6 and week == 2 and day >= 4) or (month == 6 and week == 3 and day <= 3) :
        "시험을 대비해서 공부를 열심히 했다.\n"
        extend "체력 -15, 멘탈 -15, 공부 +4"

        python :
            hp -= 15
            mental_point -= 15
            study_parameter += 4
            # gwa_parameter -= 1
            # club_parameter -= 1

    else :
        "공부를 했다.\n"
        extend "체력 -15, 멘탈 -15, 공부 +2.7"

        python :
            hp -= 15
            mental_point -= 15
            study_parameter += 2.7
            # gwa_parameter -= 1
            # club_parameter -= 1

    $ study_count += 1
    call parameter_maxmin_check from _call_parameter_maxmin_check_48

    return

label evening_club:
    play sound "sound/club.mp3"
    if day != 4 :
        show club at truecenter
        "동아리 개인연습을 했다.\n"
        extend "체력 -25, 멘탈 +20, 동아리 +2.7"

        python :
            hp -= 25
            mental_point += 20
            # study_parameter -= 1
            # gwa_parameter -= 1
            club_parameter += 2.7

    else :
        show club_thur at truecenter
        if club_count < 10 :
            "동아리 정기연습을 했다.\n"
            extend "체력 -25, 멘탈 +10, 동아리 +5"

            python :
                hp -= 25
                mental_point += 10
                # study_parameter -= 1
                # gwa_parameter -= 1
                club_parameter += 4

        elif club_count < 20 :
            "동아리에서 간단하게 버스킹을 했다.\n"
            extend "체력 -20, 멘탈 +20, 동아리 +7"
            python :
                hp -= 20
                mental_point += 20
                # study_parameter -= 1
                # gwa_parameter -= 1
                club_parameter += 5

        else :
            "동아리 선배들과 친해져서 맛집 탐방을 가기로 했다.\n맛있는 것을 먹으니 힘이 조금 나는 것 같다!\n"
            extend "체력 +15, 멘탈 +30, 동아리 +10"
            python :
                hp += 15
                mental_point += 30
                # study_parameter -= 1
                # gwa_parameter -= 1
                club_parameter += 6

    $ club_count += 1
    call parameter_maxmin_check from _call_parameter_maxmin_check_49

    return

label evening_gwa:
    play sound "sound/gwa.mp3"
    show gwa at truecenter
    "과 활동을 했다.\n"

    extend "체력 -20, 멘탈 -5, 과 +2.7"

    python :
        hp -= 20
        mental_point -= 5
        #study_parameter -= 1
        gwa_parameter += 2.7
        #club_parameter -= 1

        gwa_count += 1

    call parameter_maxmin_check from _call_parameter_maxmin_check_50
    return

label evening_rest:
    play sound "sound/rest.mp3"
    show rest at truecenter
    "쉬었다.\n"
    extend "체력 +50, 멘탈 +30"

    python :
        hp += 50
        mental_point += 30
        #gwa_parameter -= 1
        #club_parameter -= 1

    call parameter_maxmin_check from _call_parameter_maxmin_check_51

    return
