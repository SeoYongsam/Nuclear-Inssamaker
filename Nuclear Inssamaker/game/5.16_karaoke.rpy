image school2 = "karaoke/school.jpg"
image karaoke = "karaoke/karaoke.jpg"
image score_30 = "karaoke/score_30.jpg"
image score_83 = "karaoke/score_83.jpg"
image score_95 = "karaoke/score_95.jpg"
image score_100 = "karaoke/score_100.jpg"
image wild_flower = "karaoke/wild_flower.jpeg"
image are_you_happy = "karaoke/are_you_happy.jpg"
image sicha = "karaoke/sicha.jpg"
image kasi = "karaoke/kasi.jpg"

# 노래방 5월 16일 월요일 저녁 month == 5 and week == 3 and day == 1 저녁
label karaoke:
    $ day_schedule[2][17] = 5
    show school2 at truecenter
    Player "우리 오늘 공부도 안되는데 코노 ㄱ?"
    Samyong "좋은데?\ㅜ"
    extend "오랜만에 첨밀밀 한 번 불러봐야지"
    Jinil "오... 나도 껴줘!"
    Jangjung "녹두 ㄱㄱ"

    show karaoke at truecenter
    "노래방 기계" "박효신 야생화 예약하셨습니다"
    "친구들" "오오... 누구냐?"
    Player "흠흠... 목 좀 풀어볼까?"
    "친구들" "노래방 점수로 밥 내기!"

    show wild_flower at truecenter
    Player "나 피우리라.... 라.... 라..."

    play sound "sound/fanfare.mp3"
    show score_83 at truecenter
    "친구들" "이거 뭐냐 ㅋㅋㅋㅋㅋ"
    Player "코노비 확정이네... 하..."
    Jinil "다음에 나다!"
    "친구들" "오 뭔데뭔데"

    "진일이가 노래를 부르는 동안 무엇을 할까?"
    menu:
        "점수를 높게 낼 수 있는 노래를 찾는다":
            $ jinil.parameter -= 10
            "진일이가 자꾸 리액션을 바라는 것 같은데..?"
        "진일이가 노래를 부르는 동안 리액션을 한다":
            $ jinil.parameter += 10
            "진일이가 기분이 좋아보인다"

    show are_you_happy at truecenter
    Jinil "좋니 사랑해서~ 사랑을 시작할 떄~\n"
    extend "네가~ 얼.. (쿨럭) 마 ㄴr... 예쁜지 모르찌이이이~"
    "친구들" "ㅋㅋㅋㅋ 김진일 목 나갔다 ㅋㅋㅋㅋㅋ"

    play sound "sound/fanfare.mp3"
    show score_30 at truecenter
    "친구들" "ㅋㅋㅋㅋㅋㅋ 이게 뭐냐\n"
    extend "너 코노비 확정이다"
    Jinil "와... 기계가 이상한 것 같은데"

    show sicha at truecenter
    Jangjung "Love & Peace"
    "친구들" "욜~ 힙찔이네"
    Jangjung "mic check 1,2... 1,2...\n"
    extend "그뤠이~\n"
    extend "밤새 모니터에 흐른 침이 마르기도 전에..."

    "장중이랑 같이 랩을 할까?"
    menu:
        "친구들이 놀릴 것 같으니 거절한다":
            $ jangjung.parameter -= 10
            $ mental_point += 20
            "장중이가 아쉬워하는 것 같지만, 괜히 같이했다가 점수 낮게 나오면 코노비를 내야할지도 모르니까..."
        "장중이랑 같이 랩을 한다":
            $ jangjung.parameter += 10
            $ mental_point -= 20
            "장중이가 같이해서 더 신났다고 한다, 근데 나 박치인거 다 들통났네 ㅠㅠ"

    play sound "sound/fanfare.mp3"
    show score_95 at truecenter
    Jangjung "봤냐? 힙알못들아\n"
    extend "코노비 낼 준비나 해라"
    Samyong "나 중국노래 해도 돼???"
    "친구들" "에이... 에바지"

    "삼용이에게 중국노래 하라고 할까?"
    menu:
        "분위기 갑분싸 될 것 같으니 거절한다":
            $ samyong.parameter -= 11
            $ gwa_parameter += 2
            "삼용이는 아쉬워하지만 분위기를 위해서는 어쩔 수 없지"

        "삼용이가 바라는 것 같으니까 부르라고 한다":
            $ samyong.parameter += 11
            $ gwa_parameter -= 2
            "분위기는 쳐졌지만, 삼용이는 행복해하니..."

    show kasi at truecenter
    Samyong "우예에에이ㅣ에에이~"
    "친구들" "오~~ 동삼용~~!!"

    play sound "sound/fanfare.mp3"
    show score_100 at truecenter
    Samyong "(거만한 표정)\n"
    extend "뭐 이 정도 ㅎ"
    "친구들" "어우 재수없어...\n"
    extend "벌써 세 시간이나 했네 ㅋㅋㅋ\n"
    extend "진일아 네가 코노비 해결해 우리 먼저 나가있을게 ㅋㅋㅋㅋ"
    Jinil "와... 진짜 그냥 간다고???"
    "친구들" "노래 못하면 조용히 하자"
    Jinil "야 기계가 이상한거야"
    "친구들" "네 다음 음치"

    return
