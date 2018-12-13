image han_river_image = "han_river/hangang.jpg"
image han_river_image2 = "han_river/nadeuli.jpg"
image chicken = "han_river/chicken.png"
image back = "han_river/back.jpg"
image goodbye = "han_river/goodbye.jpg"
image school = "han_river/school.JPG"

# 한강 5월 10일 화요일 month == 5 and week == 2 and day == 2 낮-저녁
label han_river:
    show school at truecenter
    "해장중" "날씨도 좋은데 오늘 한강 놀러 갈까?\n"
    "주인공" "좋은데? 우리 한강 뻔모 한 번 할까?\n"
    "동삼용" "하오하오 따자하오"
    "유현재" "가면 진일이 오토바이 타고 있는거 아니냐 ㅋㅋㅋㅋ"
    "노미래" "ㅋㅋㅋㅋㅋ 태워달라고 해야겠다"

    "한강에 가시겠습니까?"
    menu:
        "간다" :
            $ day_or_evening = "evening"

            show han_river_image at truecenter

            "주인공" "와 날씨 대박이다"
            "유현재" "미래야 유채꽃 진짜 예쁘다!!"
            "노미래" "진짜로... 너랑 같이 와서 너무 좋다"
            "동삼용" "너네는 따로 가서 놀아라...."
            "유현재" "ㅋㅋㅋㅋ 이따가 알아서 사라질게"
            "박대현" "야 근데 저기 킥보드 타는 애 진일이 아니냐?ㅋㅋㅋㅋ"
            "친구들" "어디어디???"
            "박대현" "넝ㅋ담ㅋ"
            "김진일" "대현아 죽고싶냐 ㅋㅋㅋㅋㅋ"
            "친구들" "참아참아 ㅋㅋㅋㅋ"
            "주인공" "우리 돗자리 깔고 어디 앉아서 놀자!!"
            "친구들" "콜콜\n"
            extend "저기로 가자 ㅋㅋㅋ"
            #과 파라미터 + / 멘탈 + / 체력 -
            $ gwa_parameter += 10
            $ mental_point += 10
            $ hp -= 20
            call parameter_maxmin_check

            show han_river_image2 at truecenter
            "해장중" "와 날씨 죽인다\n"
            extend "치맥고?"
            "김진일" "완전 콜이지"
            "동삼용" "근데 여기까지 배달이 와?"

            show chicken at truecenter
            "시스템" "(열심히 치킨을 먹는다.)"
            "동삼용" "한국 배달 문화 진짜 짱이다...."
            "주인공" "와 진짜 JMT"
            "김진일" "JMT가 뭐냐??!"
            "친구들" "으 김진일 문찐이네.\n"
            extend "갑분싸 만드네"
            "김진일" "야이씨... 모를 수도 있지(발끈)"

            "친구들을 말리겠습니까?"
            menu:
                "말린다":
                    show chicken at truecenter
                    "주인공" "어 JMT가 뭐야??"
                    "친구들" "아 너도 모르냐 ㅋㅋㅋ"
                    "김진일" "ㅋㅋㅋㅋ 얘도 모르네\n"
                    extend "얘가 나보다 더하네 ㅋㅋㅋ"
                    "주인공" "김진일 너는 나한테 그런말 하면 안되지 ㅋㅋㅋ"
                    "김진일" "와 진짜 너무 고였다 ㅉㅉ"
                    "주인공" "(자기 편 들어줬더니....)"

                    show goodbye at truecenter
                    "주인공" "(하... 뻔대하기 힘들다)\n"
                    extend "(나는 제대로 놀지도 못하고 분위기만 좋게하려고 노력하네)"
                    "친구들" "오늘 너무 즐거웠어! 잘 들어가~"
                    "주인공" "응응 너도!!!"
                    #김진일과의 파라미터 ++ // 멘탈 -
                    $ jinil.parameter += 40
                    $ mental_point -= 10
                    call parameter_maxmin_check

                "일진이를 놀리는 것에 동참한다":
                    show chicken at truecenter

                    "주인공" "김진일 진짜 갑분싸 지렸다\n"
                    extend "진짜 너랑 같이 못다니겠다"
                    "친구들" "ㅋㅋㅋ 그러니까 김진일 부끄럽다 집에 가라"
                    "김진일" "야 너네 너무하다 진짜....\n"
                    extend "나 먼저 간다 재밌게 놀아라"

                    show back at truecenter

                    "친구들" "야 일진아... 일진아"

                    #일진 파라미타 -- / 과 ++
                    $ jinil.parameter -= 40
                    $ gwa_parameter += 20
                    call parameter_maxmin_check

        "거절한다":
            jump weekday_SNS
            #체력 + / 외로움 +
            return

    jump weekday_SNS
    return
