# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

image pcbang = "jongpa/bar_less.png"
image pcbang = "jongpa/bar_many.png"
image pcbang = "jongpa/bar_all.png"
image pcbang = "jongpa/table1.png"
image pcbang = "jongpa/table2.png"
image pcbang = "jongpa/bar_street.png"


label jongpa :
    "오늘은 종파가 있는 날. 다들 단톡에서는 종파에 대한 말은 없었지만,\n"

    #많이 왔을 때(과 파라미터 75 이상)
    if gwa_parameter >= 75 :
        extend "종파 장소에 가보니 아이들이 생각보다 많이 모여있었다."
        show bar_many at truecenter

        Jinil "오~ 오늘 사람들 진짜 많이 왔는데?"
        Jangjung "나 솔직히 별로 기대 안했는데 생각보다 사람 많네 ㅋㅋㅋ"
        Jinil "그니까 ㅋㅋ"
        Samyong "우리 과 사람들 거의 다 온거 아니야??"
        Hyunjae "이게 다 뻔대가 일을 잘해서 그런거지~"
        Samyong "ㅋㅋㅋ 뻔대 솔직히 과생활에 한학기 바쳤다"
        Player "에이~ 근데 인정!"
        Jangjung "ㅋㅋㅋㅋ 아오 칭찬을 못해주겠네"
        Hyunjae "뻔대야 빨리 와~ 얼른 마시자~"

    #적당히 왔을 때
    elif gwa_parameter >= 50 :
        extend "종파 장소에 가보니 아이들이 적당히 모여있었다."
        show bar_many at truecenter

        Jinil "뭐 사람들 올 만큼 왔네"
        Player "딱 생각한 만큼 온것 같아 ㅋㅋ"
        Samyong "그래도 아무도 안온것 보다는 낫지 ㅋㅋㅋㅋ"
        Jangjung "잘 안보이는 얼굴도 몇몇 보이네"
        Jinil "얼른 술이나 마시러 가자"
        Player "고고~"

    #적게 왔을 때
    else :
        extend "종파 장소에 가보니 아이들이 생각보다 적게 모여있었다."
        show bar_less at truecenter

        Jinil "뭐야 왜 사람이 없어?"
        Jangjung "우리 종파 망했는데? ㅋㅋㅋㅋ"
        Samyong "항상 보는 사람만 왔네"
        Player "어! 다들 왔네!\n"
        extend "(하… 나머지는 안 올 생각인가보네..)"
        Jinil "다른 애들은 더 안와"
        Player "아니야 애들 조금 늦는 걸 거야.. ㅋㅋ"
        Hyunjae "일단 애들 올 때까지\n"
        extend "우리 시험 끝난 기념으로 술이나 마시고 있자 ㅋㅋㅋㅋ"
        Player "그래그래! 건배~"

    "돌아다니며 친구들과 술을 마셨다"

    show bar_all at truecenter

    Player "오~ 여기 이번 학기 고생한 애들 밖에 없네\n"
    extend "근데 여기 왜 이렇게 조용해 ㅋㅋㅋ"
    extend "자자 이러지 말고 빨리 건배하고 술 마시자!"
    Jangjung "ㅋㅋㅋㅋ 그래그래"
    Hyunjae "ㅋㅋㅋㅋㅋㅋ 그거 진짜 웃기다 미래야 ㅋㅋㅋ"
    Mirae "그치 ㅋㅋㅋㅋㅋ\n"
    extend "나중에 우리끼리 있을 때 또 얘기해줄게 ㅋㅋㅋㅋ"
    Jinil "왜 니네 커플 둘만 얘기해 애들 외롭게~"
    extend "커플이라고 유난떠냐 ㅋㅋ"
    Mirae "응~ 쏠로는 조용히 하자~"
    Player "ㅋㅋㅋ 너네들 안되겠다\n"
    extend "이따가 자리 섞어야겠다"
    Samyong "얘들아 일단 뻔대가 같이 한 잔 하자고 했으니 짠 부터 하자"
    Samyong "그래도 한 학기 고생한 뻔대가 얘기하는데 집중 해줘야지"
    Hyunjae "아 미안 미래랑 얘기하느라 못 들었어 ㅋㅋㅋ"
    Player "역시 삼용이 밖에 없다~\n"
    extend "아무튼 종강 했는데 재밌게 마시자 ㅋㅋㅋ\n"
    extend "자자 짠 하자!"

    show table1 at truecenter

    "먼저 미래네 테이블로 갔다"

    Player "오~ 너네 아직까지 사귀네 ㅋㅋㅋ"
    Hyunjae "뻔대야 미래랑 얘기하다가 건배사 못들어서 미안 ㅋㅋㅋ"
    Mirae "맞아 ㅠㅠ 미안"
    Hyunjae "근데… 김진일이 우리 얘기하는걸로 뭐라하는건 좀 그렇지 않냐?\n"
    extend "네가 뭐라고 했으면 차라리 이해하겠는데 매번 왜 저러냐"
    Mirae "그러니까 내가 이래서 김진일이랑 같이 다니기 싫어"
    Ohduck "맞아 보쿠모 코토리쨔응과 연애해서 느끼는건데 연애가 더 중요하다"
    Player "에이~ 다음학기도 같이 지내야하는데 너무 그러지마\n"
    extend "짠하자 짠 ㅋㅋㅋ 나 그러면 저기도 갔다올게 ㅋㅋㅋ"
    Hyunjae "그래 ㅋㅋㅋ"

    show table2 at truecenter

    "다음 장중이네 테이블로 갔다"

    Player "야야~ 항상 준비위원회 해준 고정 멤버들 잘 마시고 있냐?"
    Jangjung "아니 우리 아직 소주 3병밖에 못마셨어 ㅠㅠ"
    Jinil "맞아 애들이 오늘 별로 안마시네"
    Daehyun "장중아 너 얼굴 지금 진짜 빨간데 ㅋㅋㅋㅋㅋ?"
    Jangjung "얼굴만 빨간거지 ㅋㅋㅋ\n"
    extend "한학기 동안 봤는데 내 주량 아직 모르냐?"
    Player "알지 너 주량 ㅋㅋㅋㅋ 간찌인거 알지"
    Jangjung "오늘 다이다이 하실???"
    Jinil "안돼 오늘 저 테이블 죽여야되니까 아껴둬"
    Jangjung "맞네 ㅋㅋㅋㅋ 오늘 유현재 노미래 정의구현해야지\n"
    extend "한 학기 동안 장소 안가리고 붙어있어서 짜증났었는데\n"
    extend "오늘도 종파와서 자기네들끼리만 얘기하는 것 보니깐 진짜 맘에 안들더라"
    Player "에이... 커플인데 그럴 수도 있지 너무 그러지마 ㅋㅋ\n"
    extend "오늘 즐겁게 마시자!!!!"


    "혼란했던 한 학기는 오늘 이 종파와 함께 드디어 끝을 맺었다."
    "어색했던 사이로 처음 만나 둘도 없는 친구로 지내는 애들도 있었지만\n
    끝까지 어색한 친구들도 아직 있었다."
    "물론 한 학기 안에 모두와 친해질 수는 없겠지만 그래도 뭔가 아쉽다."
    "친구들과 함께 술을 마시다가 어느새 종강파티가 끝이 나있었다."

    "여름 방학에는 애들을 못볼 것 같아 아쉬운데 몇몇 친구들을 붙잡고 2차를 가자고 해야겠다."

    #--------------------------------------------------------------------------
    #끝나고 한 잔 더하자고 제안

    #1 / 진일에게
    Player "진일아 이따가 끝나고 한잔 더 할까? ㅋㅋㅋ"
    #진일 >= ♥♥♥)
    if jinil.parameter >= 60 :
        Jinil "뻔대가 마시자면 콜이지~ 어디로 갈까?"
    #(Jinil < ♥♥♥)
    else :
        Jinil "아... 나 다른 약속도 있어서 가야해"

    #2 / Jangjung에게
    Player "장중아 종파 끝나고 더 마실래? ㅋㅋㅋ"
    #(Jangjung >= ♥♥♥)
    if jangjung.parameter >= 60 :
        Jangjung "ㅋㅋㅋㅋ 나도 그 말 할라고 했는데 ㄱㄱㄱ"
    #(Jangjung < ♥♥♥)
    else :
        Jangjung "음… 나는 요즘 술을 너무 많이 마셨다 ㅠ 다음에 마시자"

    #3 / Samyong에게
    Player "삼용아 이따가 끝나고 고량주 ㄱㄱ?"
    #(Samyong >= ♥♥♥)
    if samyong.parameter >= 60 :
        Samyong "그렇지 않아도 너랑 마시려고 집에서 하나 들고왔어 ㅋㅋㅋㅋ 내 방에서 마실까? ㅋㅋㅋㅋ"
    #(Samyong < ♥♥♥)
    else :
        Jangjung "나 내일 집에 가야되서 오늘은 그만 마실게 비행기 놓칠 수도 있어 ㅠㅠ"


    #If 아무도 안마시면(셋 다 하트 세개 이하면)
    if jinil.parameter <= 60 and jangjung.parameter <= 60 and samyong.parameter <= 60 :
        #Scene 혼자 술먹는 배경
        Player "그래도 한 학기 동안 일도 열심히 했다고 생각하는데\n"
        extend "학기 끝나고 술 한 잔 마실 사람이 없네"
        Player "하... 너무 외롭다"

        "혼자라도 술을 마셔야겠다"
        "작은 포차에 들어가 소주를 마시고 있으니 술이 평소보다 더 쓴 것 같다."

        "아 근데.. 나 너무 많이 마셨는데... 아 졸려..."


    #If 셋 다 하트 세개 이상이면
    elif jinil.parameter >= 60 and jangjung.parameter >= 60 and samyong.parameter >= 60 :
        Player "와.. 다들 2차 가는거 실화?"
        Jangjung "빼앰~ 뻔대쓰 한 학기 잘해쓰~ 이거 실화쓰~"
        Jinil "ㅋㅋㅋㅋ 한 학기 수고 했다"
        Samyong "맞아 ㅋㅋㅋ 너무 고생했어 우리 오늘 밤 새 마시자"
        Player "가즈아~~~~"

    #If 1명이라도 하트가 3개면
    elif jinil.parameter >= 60 or jangjung.parameter >= 60 or samyong.parameter >= 60 :
        "술을 더 마시자고 친구들을 붙잡았을 때 친구들이 흔쾌이 가자고 해줘서 너무 고마웠다."
        "이런 친구들이 있다는 것 보니 내가 그래도 대학생활을 허투루 하지는 않았나보다."
        "이제와서 하는 말이지만 대학생활 생각보다 재밌는 것 같다."

        "아 근데.. 나 너무 많이 마셨는데... 아 어지러워..."


    jump ending


    return
