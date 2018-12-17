image playground = "olympic/playground.png"
image soccer_bench = "olympic/soccer_bench.png"
image pigoo = "olympic/pigoo.png"
image sool = "olympic/sool.png"
image conversation = "olympic/conversation.jpg"

# 노래방 5월 21일 토요일 month == 5 and week == 3 and day == 6 낮-저녁
label olympic:
    show playground at truecenter
    Player "오늘 날씨 진짜 좋다!!! 오늘 심리학과 발라버리자~~\n"
    Jinil "가즈아~~~~\n"
    Jangjung "오늘 경기 뭐뭐한댔지?"
    Player "오늘 축구랑 피구, 계주할거야 ㅋㅋㅋ\n"
    extend "벌써 11신데....\n"
    extend "온다는 얘들이 좀 늦네...."
    Jinil "걔들 좀 늦는데 ㅋㅋㅋ\n"
    extend "축구 안나오는 얘들은 자기 경기 할 때 올 것 같은데"
    Player "아 레알???\n"
    extend "연락도 안하고 음....\n"
    extend "연락해봐야겠다...ㅠ"

    show soccer_bench at truecenter
    Jangjung "뻔대야\n"
    extend "나는 언제 들어가??\n"
    extend "나 10시부터 왔는데 계속 벤치에만 있다\n"
    extend "나도 뛰고 싶어"
    Player "이게 내가 감독이 아니라서\n"
    extend "현재한테 물어봐야할 것 같은데"
    Jangjung "에이... 뻔대가 그 정도는 결정할 수 있지\n"
    extend "네가 현재한테 얘기 좀 해봐"

    "장중이의 부탁을 들어 주시겠습니까?"
    menu:
        "들어준다":
            show conversation at truecenter

            Player "저기 현재야...\n"
            extend "우리 몇대 몇이지??"
            Hyunjae "2 : 0..."
            Player "오... 잘하고 있네!! 그러면...."
            Hyunjae "우리가 0이야\n"
            extend "쟤네들 생각보다 잘하네"
            Player "아 그러면 우리 분위기 전환이 필요할 것 같지 않아?\n"
            extend "장중이 넣는건 어때?"
            Hyunjae "아... 장중이는 좀...\n"
            extend "넣으면 분위기 더 안 좋아질 것 같아\n"
            extend "장중이가 자기 좀 넣어달래?"
            Player "아 그건 아냐 ㅋㅋㅋ\n"
            extend "일단 알겠어!!!"

            #과 파라미터 - / 장중 파라미터 +
            $ gwa_parameter -= 10
            $ jangjung.parameter += 20
            call parameter_maxmin_check

        "거절한다":
            show soccer_bench at truecenter
            Player "네가 직접 가서 부탁해봐 장중아\n"
            extend "내가 결정하기는 좀 그렇다 ㅠ"
            Jangjung "아 그래…\n"
            extend "이럴거면 10시까지 와달라고 하지 말지 그랬냐\n"
            extend "하....."

            #장중 파라미터 -
            $ jangjung.parameter -= 20
            call parameter_maxmin_check

    show pigoo at truecenter
    Player  "미래 안오나\n"
    extend "벌써 짝피구 할 시간인데...\n"
    extend "어어 저기 미래 온다 휴…"
    Mirae "아직 시작 안했지?\n"
    extend "나 딱 맞춰서 오려고했어 ㅋㅋㅋ\n"
    extend "앞에는 내가 너무 할 게 없어서 ㅠ"
    Player "좀 늦긴 했지...\n"
    extend "여튼 빨리 하자"
    Mirae "근데 나 현재가 짝피구 하지 말라는데 어쩌지?\n"
    extend "다른 사람이랑 붙어 있는 거 싫다고 해서 ㅠ\n"
    extend "혹시 나 빠질 수 있을까?\n"

    screen schedule_highlight
    "미래의 부탁을 들어 주시겠습니까?"
    menu:
        "들어준다":
            show pigoo at truecenter
            Player "심리학과 과대님....\n"
            extend "혹시 저희 피구 인원 1명 줄일 수 있을까요?\n"
            extend "참여한다고 한 친구가 남친이 못하게 한다네요 ㅠㅠ\n"
            extend "정말 죄송합니다..."
            "심리학과 과대" "그건 좀 곤란한데...\n"
            extend "저희 짝피구하려고 지금까지 기다린 친구들이 있어서요\n"
            extend "갑자기 이렇게 바꾸려고 하시면 저희도 좀 당황스럽네요;;;\n"
            "심리학과 과대" "죄송하지만 안될 것 같아요\n"
            extend "10명대 11명으로 하시죠"

            #과 파라미터 -
            $ gwa_parameter -= 10
            call parameter_maxmin_check

        "거절한다":
            show playground at truecenter
            Player "그러면 애초에 지원을 하지 말았어야지\n"
            extend "다른 과하고 다 얘기 해 놓은건데 갑자기 이러면 어떡해\n"
            extend "나는 못빼줘"
            Mirae "아 그럼 몰라 나도 안해\n"
            extend "나 그냥 집 갈래"
            Player "야 노미래! 노미래!!!!!!"

            #과 파라미터 --
            $ gwa_parameter -= 20
            call parameter_maxmin_check

    show playground at truecenter
    Jinil "아... 우리 계속 지네\n"
    extend "우리 달리기라도 꼭 이기고 싶다\n"
    extend "뻔대야 내가 마지막 주자로 들어가면 안되냐"
    Player "진일아 너 몇번째지?"
    Jinil "나 세번째\n"
    extend "근데 이거 순서를 뽑기로 한거잖아\n"
    extend "내가 제일 빠르니까 이기려면 내가 마지막에 해야한다고 생각해"
    Player "아직 순서 제출 안하기는 했는데..."

    "진일이의 부탁을 들어 주시겠습니까?"

    menu:
        "들어준다":
            show playground at truecenter
            Jinil "내가 진짜 열심히 뛰어서 우리 팀 우승 시킬게"
            "엔트리 제출"
            Jangjung "야\n"
            extend "내가 왜 마지막 주자 아니야?\n"
            extend "김진일이 마지막이네?\n"
            extend "어이가 없네"
            Player "우리 운동회 지고 있으니까 이거라도 이겨야지\n"
            extend "진일이가 제일 빠르잖아\n"
            extend "네가 이해 좀 해줘..."
            Jangjung "아 진짜 이럴거면 왜 뽑은거야 ㅅㅂ"
            #진일 +, 장중 -, 과 -
            $ jinil.parameter += 20
            $ jangjung.parameter -= 20
            $ gwa_parameter -= 10
            call parameter_maxmin_check

        "거절한다":
            show playground at truecenter
            Player "진일아 그래도 이미 정해진 걸 바꿀 수는 없는 것 같아\n"
            extend "너도 동의하고 뽑기로 순서 정한거잖아\n"
            extend "또 달리기 이기면 어떻고 지면 어떠냐 ㅋㅋㅋㅋ\n"
            extend "재밌게 놀다가면 되지"
            Jinil "아니... 내가 우리과가 밀릴 줄 알았냐\n"
            extend "너는 자존심도 안 상해?\n"
            extend "이것도 지면 얘들이 얼마나 쪽팔리겠냐?\n"
            extend "어휴 난 모르겠다..."
            #진일 -, 과 -
            $ jinil.parameter -= 20
            $ gwa_parameter -= 10
            call parameter_maxmin_check

    $ day_or_evening = "evening"
    show sool at truecenter
    Player "오늘 다들 수고 너무 많았어!!\n"
    extend "비록 우리가 졌지만 재밌게 놀았다 ㅋㅋㅋㅋ\n"
    extend "다들 바빠서 뒷풀이는 별로 못와서 아쉽지만, 온 사람들끼리라도 한 잔 하자!!"
    Jinil "그래 뻔대도 고생 많았다"
    Player "내가 문정과하면 너희들이 가즈아~~해줘!!!\n"
    extend "문정과~~"
    "진일, 장중" "가즈아~~~"
    Player "와... 근데 진짜 뒷풀이 온 사람이 너무 없네\n"
    extend "너네라도 있어서 다행이다"
    Jangjung "그러니까 우리한테 잘하라고 ㅋㅋㅋ"
    Player "에이 내가 너네들한테 얼마나 잘하는데 ㅋㅋㅋ"
    Jangjung "음... 솔직히 말하면 나는 요즘 너한테 섭섭해\n"
    extend "아까 출전시켜달라고 했을때도 머뭇머뭇하고\n"
    extend "혹시 학기 초 과잠 만들때처럼 운동회 안 도와줘서 그러는거야?"
    Player "에이 그런건 아니지...\n"
    extend "나는 공정하게 진행하려고 한거야"
    Jangjung "그러니까\n"
    extend "학기 초에는 안 그랬잖아\n"
    extend "뻔대 일 잘 도와주는 사람들한테 더 고마워해야하는 것 아니야?"
    Player "매번 고마워하지\n"
    extend "그래서 내가 너네들한테 밥도 자주 사고 그러잖아\n"
    extend "네가 그렇게까지 말하니까 나도 섭섭하다 장중아"
    Jinil "솔직히 나도 장중이랑 좀 비슷한 느낌이야\n"
    extend "아까 달리기 순서 얘기 했을 떄 나한테도 되게 빡빡하게 굴었잖아\n"
    extend "우리는 그런게 섭섭한거야\n"
    extend "우리는 네 부탁 다 들어주는데 다른 사람들이랑 똑같이 대하잖아"
    Player "야 내가 너네랑만 몰려다니고 너네 좋아하는 티내고 이러면 과가 굴러가겠냐?\n"
    extend "나는 뻔대니까\n"
    extend "동기 전체가 과 생활에서 흥미를 느끼게 해야할 책임도 있잖아\n"
    Player "나라고 너네 부탁 안 들어주고 싶었겠어?\n"
    extend "그 정도는 너네가 이해해줘야지\n"
    extend "나도 학기말 되고 다들 바빠지고 이러면서 과 행사 기획하고 추진하는 일 다 내가 주로 하고 도와주는 사람들도 없는데 너무 지친다\n"
    Player "아 모르겠다....\n"
    extend "다 내 능력이 부족해서 그런가보다\n"
    extend "요즘 일하다가 공부도 잘 못하고, 동아리도 잘 못하고, 잠도 잘 못자고 너무 지친다\n"
    extend "빨리 종강이나 했으면 좋겠다"

    # HP -30, MP -30
    $ hp -= 60
    $ mental_point -= 30
    call parameter_maxmin_check

    call change_SNS
    $ day += 1
    jump weekday_SNS

    return
