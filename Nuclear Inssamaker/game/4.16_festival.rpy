#이미지 선언
image fest_poong = "festival/fest_poong.jpg"
image fest_food = "festival/fest_food.jpg"
image fest_stage = "festival/fest_stage.jpg"
image cuprice = "festival/cuprice.jpg"
image shrimp = "festival/shrimp.jpg"
image steak = "festival/steak.jpg"
image soran = "festival/soran.jpg"

# 4월 16일 월요일 축제 이벤트
# month4 week3 day 1
label festival:
    scene black
    "오늘은 축제가 있는 날!"
    "소란 공연을 같이 보기로 한 친구들과 저녁을 같이 먹기로 하였다."

    show fest_stage at truecenter
    Player "으음 뭐 먹지?\n"
    extend "축제니까 주변에 있는 노점상에서 먹을까?"
    Jangjung "오오~ 난 그게 좋은 것 같은데?"
    Samyong "근데 먹을거 파는 곳이 생각보다 많다..우와 푸드트럭?"
    Mirae "오 푸드트럭 괜찮지!\n"
    extend "안 그래 현재야?"
    Hyunjae "미래가 괜찮으면 나도 당연히 괜찮지~"
    Jinil "....야 죽창 어딨냐 죽창!!"
    Mirae "꺄악~"
    Hyunjae "꺄악~"

    show fest_food at truecenter
    Player "자자 진정하고~\n"
    extend "그래서 보자 푸드트럭도 종류가 여러 개 있는 것 같은데 어디가 좋을까?"
    Samyong "난 스테이크!!\n"
    extend "저게 제일 맛있어 보이는데?"
    Jangjung "난 새우!\n"
    extend "새우에 맥주를 딱!"
    Jinil "저 컵밥도 괜찮지 않냐??\n"
    extend "뻔대야 너는 뭐 먹고 싶은데?"
    Player "음...나는..."

    menu:
        "나는 스테이크!!" :
            show steak at truecenter
            Samyong "그래 이런 날엔 고기지~"
            Jangjung "음...고기도 나쁘지는 않으니까"

            scene black
            "친구들과 함께 푸드트럭에서 스테이크를 사먹었다."
            "삼용이가 무척이나 기뻐한다."
            #삼용 파라미터 업
            $ samyong.parameter += 20
            call parameter_maxmin_check

        "난 새우~" :
            show shrimp at truecenter
            Jangjung "크~ 역시 뻔대면 새우를 고를 줄 알았어!"
            Jinil "그럼 맥주도 한 캔 사먹자!!"

            scene black
            "친구들과 함께 푸드트럭에서 새우를 사먹었다."
            "장중이가 무척이나 기뻐한다."
            #장중 파라미터 업
            $ jangjung.parameter += 20
            call parameter_maxmin_check

        "오늘은 컵밥이 땡기네~" :
            show cuprice at truecenter
            Jinil "그렇지! 컵밥이지!! 한국인은 밥심! 아니겠냐~"
            Daehyun "컵밥 괜찮지!!"

            scene black
            "친구들과 함께 푸드트럭에서 컵밥을 사먹었다."
            "진일이가 특히 맛있게 먹었다."
            #진일 파라미터 업
            $ jinil.parameter += 20
            call parameter_maxmin_check

    show fest_food at truecenter
    Player "아~ 배부르다~\n"
    extend "그럼 슬슬 공연장으로 갈까?"
    Mirae "맞아 맞아 곧 공연 시작하겠다!!"

    show fest_poong at truecenter
    "친구들과 함께 열심히 소리 지르면서 공연을 볼 수 있었다."

    return
