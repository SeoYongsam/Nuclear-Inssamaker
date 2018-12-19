#이미지 선언
image pcbang = "pcbang/pcbang.jpg"
image leagueoflegends = "pcbang/leagueoflegends.jpg"
image leagueloss = "pcbang/leagueloss.png"
image kartrider = "pcbang/kartrider.jpg"
image pcbangstreet = "pcbang/pcbangstreet.jpg"

#피시방 이벤트 저녁 4월 11일 month4 week2 day3
label pcbang:
    scene black
    "갑자기 대현이가 현재, 미래, 그리고 진일이와 함께 게임을 하러 PC방에 가자고 한다."

    menu:
        "PC방에 같이 가서 게임을 한다":
            show pcbang at truecenter
            "결국 친구들이랑 PC방에 같이 갔다"
            Daehyun "얘들아 무슨 게임 할래?"
            Jinil "5명이면 당연히 '리그 오브 전설' 해야 하는 거 아닌가?"
            Hyunjae "미래랑 나는 '쇼핑카트 라이더' 생각하고 있었는데..."

            menu:
                "진일이가 추천한 '리그 오브 전설'을 한다":
                    play music "music/4.11_pcbang_league_of_legends.mp3"
                    show leagueoflegends at truecenter
                    Jinil "좋았으~ 역시 게임은 '리그 오브 전설'이지~"
                    Hyunjae "ㅋㅋ 알겠어"
                    Daehyun "뻔대 넌 처음 하는거지? 내가 옆에서 도와줄게!"

                    scene black
                    "30분 뒤..."

                    show leagueloss at truecenter
                    Jinil "아 니네들 진짜 뭐하냐\n"
                    extend "숟가락을 입에 넣어줘도 못 받아먹네.\n"
                    extend "게임 하고 싶은거 맞아?"
                    Mirae "왜 그래 진일아... 그냥 게임이잖아"
                    Hyunjae "진정해 ㅋㅋ 다음판 이기면 되지"
                    Daehyun "그래 다음판은 꼭 이기자"

                    scene black
                    "2시간 뒤"

                    stop music fadeout 1.0
                    show pcbangstreet at truecenter
                    Daehyun "아~ 그래도 피시방 오랜만에 오니까 재밌네"
                    Jinil "뻔대야 게임 잘 못하면 말하지~\n"
                    extend "내가 다음번엔 제대로 가르쳐줄게"
                    Mirae "... 뻔대야 너무 신경쓰지마!"

                    scene black at truecenter
                    "친구들이 게임을 잘해서 많이 이긴 것 같다.\n그래도 다같이 재밌게 게임한 것 같다."
                    "진일이는 오늘 '리그 오브 전설'을 할 수 있어서 전반적으로 행복해했던 것 같다.\n
                    하지만 나는 진일이의 눈치를 봐야해서 힘들었다."
                    #진일이와의 친밀도 UP, 멘탈 DOWN
                    $ jinil.parameter += 20
                    $ mental_point -= 20
                    call parameter_maxmin_check from _call_parameter_maxmin_check_30

                "현재가 좋아하는 '쇼핑카트 라이더'를 한다":
                    play music "music/4.11_pcbang_kartrider.mp3"
                    show kartrider at truecenter
                    Hyunjae "오케이~ '쇼핑카트 라이더' 가즈아~~~!"

                    scene black
                    "3시간 뒤"

                    scene kartrider_end at truecenter
                    Daehyun "아 치사하게 마지막에 아이템 쓰는거 뭐냐"
                    Mirae "ㅋㅋㅋㅋ 이것도 실력이라구~"
                    Hyunjae "와 미래 뭐야? 엄청 잘하네"
                    Daehyun "근데 진일이는 카트 오늘 처음함?\n"
                    extend "개못하던데 ㅋㅋㅋㅋ"
                    Jinil "..."

                    stop music fadeout 1.0
                    scene pcbangstreet at truecenter
                    Mirae "ㅋㅋㅋㅋ 내 운전실력 다시는 무시하지마라~"
                    Hyunjae "와 근데 뻔대도 진짜 잘하던데??\n"
                    extend "오늘 나 한번도 1등 못함 얘 때문에!"
                    Mirae "맞아맞아 장난 아니더라\n"
                    extend "프로 게이머인줄?"
                    Jinil "'쇼핑카트 라이더'도 재밌네\n"
                    extend "'리그 오브 전설'했으면 더 재밌었겠지만"

                    scene black
                    "오늘 카트라이더를 오랜만에 해서 너무 재밌었다.\n
                    다 같이 더 친해진 것 같다."
                    "하지만 진일이는 오늘 '리그 오브 전설'을 못해서 그런지 기분이 좋지 않은 것 같다."

                    #진일이와의 친밀도 DOWN, 멘탈 UP
                    $ jinil.parameter -= 10
                    $ mental_point += 10
                    call parameter_maxmin_check from _call_parameter_maxmin_check_31


        "정중히 거절하고 예정된 계획대로 하루를 보낸다" :
            ""
            #과활동 패러미터 DOWN
            $ gwa_parameter -= 3
            call parameter_maxmin_check from _call_parameter_maxmin_check_32
            call normal_weekday_evening from _call_normal_weekday_evening_1

    return
