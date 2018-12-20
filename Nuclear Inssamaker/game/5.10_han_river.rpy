image han_river_image = "han_river/hangang.jpg"
image han_river_image2 = "han_river/nadeuli.jpg"
image chicken = "han_river/chicken.png"
image back = "han_river/back.jpg"
image goodbye = "han_river/goodbye.jpg"
image school = "han_river/school.JPG"

# 한강 5월 10일 화요일 month == 5 and week == 2 and day == 2 저녁
label han_river:
    show school at truecenter
    Jangjung "날씨도 좋은데 오늘 한강 놀러 갈까?"
    Player "좋은데?\n"
    extend "우리 한강 뻔모 한 번 할까?"
    Samyong "하오하오 따자하오"

    "한강에 가시겠습니까?"
    menu:
        "간다" :
            $ day_schedule[2][10] = 5
            play music "music/5.10_han_river.mp3"
            $ day_or_evening = "evening"
            show han_river_image at truecenter

            Player "와 날씨 대박이다"
            Hyunjae "미래야 유채꽃 진짜 예쁘다!!"
            Mirae "진짜로... 너랑 같이 와서 너무 좋다"
            Player "우리 돗자리 깔고 어디 앉아서 놀자!!"
            "과 분위기가 좋아진 것 같다. 내 마음도 따뜻해진다."

            #과 파라미터 + / 멘탈 + / 체력 -
            $ gwa_parameter += 2
            $ mental_point += 10
            $ hp -= 20
            call parameter_maxmin_check from _call_parameter_maxmin_check_33

            show chicken at truecenter
            "(열심히 치킨을 먹는다.)"
            Samyong "한국 배달 문화 진짜 짱이다..."
            Player "와 진짜 JMT"
            Jinil "JMT가 뭐냐??!"
            "친구들" "으 김진일 문찐이네"
            Jinil "야이씨... 모를 수도 있지(발끈)"

            "진일이를 못 놀리게 친구들을 말리겠습니까?"
            menu:
                "말린다":
                    show chicken at truecenter
                    Player "어 JMT가 뭐야??"
                    "친구들" "아 너도 모르냐 ㅋㅋㅋ"
                    Jinil "ㅋㅋㅋㅋ 얘도 모르네"
                    extend "얘가 나보다 더하네 ㅋㅋㅋ"
                    Player "김진일 너는 나한테 그런말 하면 안되지 ㅋㅋㅋ"
                    Jinil "와 진짜 뻔대 너무 고였다 ㅉㅉ"
                    Player "(자기 편 들어줬더니....)"

                    show goodbye at truecenter
                    Player "(하... 뻔대하기 힘들다)\n"
                    extend "(나는 제대로 놀지도 못하고 분위기만 좋게하려고 노력하네)"
                    "친구들" "오늘 너무 즐거웠어! 잘 들어가~"
                    Player "응응 너도!!!"

                    "진일이가 나한테 내심 고마워하는 것 같긴 한데, 어쩐지 난 기분이 찝찝하다."
                    #김진일과의 파라미터 ++ // 멘탈 -
                    $ jinil.parameter += 20
                    $ mental_point -= 20
                    call parameter_maxmin_check from _call_parameter_maxmin_check_34

                "진일이를 놀리는 것에 동참한다":
                    show chicken at truecenter

                    Player "김진일 진짜 갑분싸 지렸다\n"
                    extend "진짜 너랑 같이 못다니겠다"
                    "친구들" "ㅋㅋㅋ 그러니까 김진일 부끄럽다 집에 가라"
                    Jinil "야 너네 너무하다 진짜...\n"
                    extend "나 먼저 간다 재밌게 놀아라"

                    show back at truecenter

                    "친구들" "야 진일아... 진일아"

                    "진일이가 많이 속상해한다. 괜히 미안해진다."
                    "...그래도 진일이의 희생으로 과 분위기가 좋아진 것 같은데...?"

                    stop music fadeout 1.0
                    #일진 파라미타 - / 과 ++
                    $ jinil.parameter -= 10
                    $ gwa_parameter += 4
                    call parameter_maxmin_check from _call_parameter_maxmin_check_35

        "거절한다":
            # 체력 + / 멘탈 --
            "애들이 한강에 갈 시간에 원래 일정을 소화했다."
            # $ hp += 20
            # $ mental_point -= 5
            call normal_weekday_evening from _call_normal_weekday_evening_2

    jump weekday_SNS
    return
