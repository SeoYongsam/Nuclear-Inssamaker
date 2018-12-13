label weekday_day_event :
    $ day_or_evening = "day"

    if month == 3 and week == 2 and day == 1 :
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

    elif month == 3 and week == 3 and day == 5 :
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
    elif month == 3 and week == 3 and day == 6 :
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

    elif month == 3 and week == 4 and day == 1 :
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

    elif month == 3 and week == 4 and day == 2 :
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

    elif month == 4 and week == 1 and day == 1 :
        call uniform_day

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
        if day_schedule[month - 3][(week - 1) * 8 + day] == 1:
            call evening_study

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 2:
            call evening_club

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 3:
            call evening_gwa

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 4:
            call evening_rest

    else :
        $ day_or_evening = "evening"

    return
