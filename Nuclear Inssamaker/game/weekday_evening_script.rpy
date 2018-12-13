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
        call club_first

    elif month == 4 and week == 2 and day == 3 :
        call pcbang

    elif month == 4 and week == 3 and day == 1 :
        call festival

    elif month == 4 and week == 4 and day == 2 :
        "장터 관련해서 카톡에서 얘기가 나오고 있다. 확인해보자."
        #4월 24일 포스터 회의
        scene black
        "오늘은 장터 준비위원회끼리 모여서 포스터 디자인을 하기로 했다."

        "내가 없어도 회의가 잘 돌아갈 것 같지만...\n갈까 말까?"

        menu:
            "회의에 참여한다":

                "회의에 참여했다."

                show poster at truecenter

                "포스터 디자인은 심플하게 가기로 했다."
                "사실 심플 할지는 모르겠지만 포토샵을 다룰 줄 아는 현재가 알아서 하기로 했다."
                "워낙 회의가 잘 진행돼서 내가 안왔어도 됐으려나 싶지만 그래도 마음은 조금 놓인다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening

    elif month == 4 and week == 4 and day == 3 :
        #4월 25일 예산 및 메뉴 정하기
        scene black
        "오늘은 장터 준비위원회끼리 모여서 예산 및 메뉴를 정하기로 했다."

        "내가 없어도 회의가 잘 돌아갈 것 같지만...\n갈까 말까?"
        menu:
            "회의에 참여한다":
                "회의에 참여했다."

                show meeting at truecenter

                "예산은 적당하게 50만원으로 잡았다."
                "메뉴는 다른 장터와 차별을 두고 싶었지만 예산에 맞춰 재료를 준비해야했기\n
                때문에 파전과 치킨너겟 등 기존 장터들과 비슷하게 메뉴를 정했다."
                "오늘 회의에 와서 다행이라고 생각한다."
                "애들이 열정이 많아서인지 무모해서인지는 모르겠지만 메뉴를 정할때 회의가 산으로 갈 뻔한 적이 많았다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening

    elif month == 4 and week == 4 and day == 4 :
        #4월 26일 메뉴판 만들기
        scene black
        "오늘은 장터 준비위원회끼리 모여서 메뉴판을 만들기로 했다."

        "내가 없어도 메뉴판을 잘 만들 것 같지만...
        \n 갈까 말까?"

        menu:
            "회의에 참여한다":
                "회의에 참여했다."

                show menu_pan at truecenter
                "메뉴판은 정말 쉽게 정했다."
                "이미 메뉴를 정했기 때문에 장터날에 붙일 것만 만들면 됐기 때문이다."
                "오늘은 회의 보다는 메뉴판 디자인을 했디 때문에 내가 안왔어도 됐으려나 싶지만 그래도 마음은 조금 놓인다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening

    elif month == 5 and week == 1 and day == 1 :
        scene black
        "오늘은 장터 준비위원회끼리 장터 전날 모여서 장을 보기로 했다."

        "내가 없어도 장을 잘 볼 수 있을지 의심스럽지만...
        \n 갈까 말까?"

        menu:
            "장을 보러 간다":
                "장을 보러 갔다."

                show shopping at truecenter
                "오늘은 내가 장을 보러 왔어야 했다."
                "애들의 상태가 의심스럽기 때문이다. 중간고사가 끝난지 얼마 안돼서 모든 것을 놓은 것만 같다."
                "장터 재료를 사는 것 보다 애들은 자신이 필요한 것들에 더 눈이 가는 것 같다."
                "다행이 나라도 정신을 차리고 장터에 필요한 도구와 음식을 샀다."
                $ jangtuh_pre_event += 1

            "계획한 대로 오후를 보낸다":
                call normal_weekday_evening

    elif month == 5 and week == 3 and day == 1 :
        call karaoke

    elif month == 6 and week == 3 and (day == 6 or day == 7) :
        call jongpa

    else :
        call normal_weekday_evening

    return




label normal_weekday_evening :
    if day_schedule[month - 3][(week - 1) * 8 + day] == 1:
        call evening_study

    elif day_schedule[month - 3][(week - 1) * 8 + day] == 2:
        call evening_club

    elif day_schedule[month - 3][(week - 1) * 8 + day] == 3:
        call evening_gwa

    elif day_schedule[month - 3][(week - 1) * 8 + day] == 4:
        call evening_rest

    else :
        extend "에러"

    return

label evening_study:
    show study at truecenter
    if (month == 4 and week == 3 and day >= 5) or (month == 4 and week == 4 and day <= 4) or (month == 6 and week == 2 and day >= 4) or (month == 6 and week == 3 and day <= 3) :
        "시험을 대비해서 열심히 공부했다\n"
        extend "체력 -15, 멘탈 -15, 공부 +15, 과 -3, 동아리 -3"

        python :
            hp -= 15
            mental_point -= 15
            study_parameter += 10
            gwa_parameter -= 3
            club_parameter -= 3

            study_count += 1

    else :
        "공부했다\n"
        extend "체력 -15, 멘탈 -15, 공부 +8, 과 -3, 동아리 -3"

        python :
            hp -= 15
            mental_point -= 15
            study_parameter += 8
            gwa_parameter -= 3
            club_parameter -= 3

            study_count += 1

    call parameter_maxmin_check

    return

label evening_club:
    if day != 4 :
        show club at truecenter
        "동아리 개인연습했다\n"
        extend "체력 -25, 멘탈 +20, 공부 -3, 과 -3, 동아리 +15"

        python :
            hp -= 25
            mental_point += 20
            study_parameter -= 3
            gwa_parameter -= 3
            club_parameter += 15

            club_count += 1

    else :
        show club_thur at truecenter
        "동아리 정기연습했다\n"
        extend "체력 -25, 멘탈 +20, 공부 -3, 과 -3, 동아리 +25"

        python :
            hp -= 25
            mental_point += 20
            study_parameter -= 3
            gwa_parameter -= 3
            club_parameter += 25

            club_count += 1

    call parameter_maxmin_check

    return

label evening_gwa:
    show gwa at truecenter
    "과 활동했다\n"

    extend "체력 -20, 멘탈 -5, 공부 -3, 과 +15, 동아리 -3"

    python :
        hp -= 20
        mental_point -= 5
        study_parameter -= 3
        gwa_parameter += 15
        club_parameter -= 3

        gwa_count += 1

    call parameter_maxmin_check

    return

label evening_rest:
    show rest at truecenter
    "쉬었다\n"
    extend "체력 +50, 멘탈 +30 과 -3, 동아리 -3"

    python :
        hp += 50
        mental_point += 30
        gwa_parameter -= 3
        club_parameter -= 3

    call parameter_maxmin_check

    return
