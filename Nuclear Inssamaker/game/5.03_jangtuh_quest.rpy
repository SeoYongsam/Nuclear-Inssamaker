#pre_event 이미지 선언
image poster = "jangtuh/poster.png"
image meeting = "jangtuh/meeting.png"
image menu_pan = "jangtuh/menu_pan.png"
image shopping = "jangtuh/shopping.png"

#이미지 선언
image college = "jangtuh/college.png"
image jangtuh = "jangtuh/jangtuh.png"
image order = "jangtuh/order.png"
image cooking = "jangtuh/cooking.png"
image other_jangtuh = "jangtuh/other_jangtuh.png"
image after = "jangtuh/after.png"
image cheers = "jangtuh/cheers.png"


# 5월 3일 화요일 낮밤 장터 이벤트
# month5 week1 day2
label jangtuh:

    show college at truecenter
    "오늘은 어쩔수 없이 수업을 못갔다."
    "장터를 총괄하는 역할을 뻔대인 내가 맡기로 했기 때문이다."
    "장터 준비는 어제 전부 끝났고 장사를 시작했다."
    "점심시간까지는 학생들이 학교 캠퍼스에 별로 없었어서 그런지 바쁘지는 않았다."

    "하지만 이제 곧 대망의 점심시간! 사람들이 하나 둘 몰려오기 시작한다!"

    play sound "sound/grill_fry.mp3"
    show order at truecenter
    Jinil "이랏샤이마세~ 주문 뭘로 하실건가요??"
    "고객1" "저는 파전이랑 막걸리 하나씩이요!"
    Jinil "네~ 6000원이요~ 감사합니다! 다음이요!"
    "고객2" "저는 김치전 하나, 치킨너겟 하나, 그리고 막걸리 하나요~"
    Jinil "김치전, 치킨너겟, 막걸리 하나씩 해서 10,000원입니다. 넵 감사합니다!"

    Player "와..진일이 너도 진짜 수고한다 ㅠㅠㅠ"
    Jinil "야 나 밖에 없지? 일찍 부터 도와주는 사람 거의 없네 ㅋㅋㅋ"
    Player "애들 수업 때문에 다 바쁜가봐 ㅋㅋ"
    Jinil "누구는 수업 없냐~"
    Player "ㅋㅋ"

    show jangtuh at truecenter
    Samyong "얘들아 나 왔어!!! 뭐하면 돼??"
    Player "얼른 와!! 지금 요리하는 사람이 별로 없어서 주문이 밀리고 있어 ㅠㅠ
    \n 너가 요리 좀 해줘!"
    Samyong "나만 믿어! 나 별명이 요리왕 삼룡이잖아 ㅋㅋㅋ"
    Jinil "알았으니까 빨리가서 일해"
    Samyong "으...으응"

    scene black
    "점심시간 이후로도 우리 장터에 사람들은 계속 많았다. 삼용이는 정말로 요리를 잘했다. "
    "어디서 준비를 해온지는 모르겠지만 자신이 쓰던 웍을 들고 온 후 사람들이 보는 앞에서 불쇼도 하며 고객들을 더욱 끌어모았다."

    show cooking at truecenter
    Jinil "아 애들 진짜 언제 오는거냐 바빠 죽겠는데"
    Samyong "진일아 다음 메뉴!!!"
    Jinil "김치전 넷, 파전 다섯, 봉골레 하나 빨리빨리 안하냐~!"
    Samyong "봉골레는 또 뭐야!!!"
    Jinil "아 몰랑 기획자들이 칠 드립이 없어서 그냥 넣었나봐"
    Samyong "일단 알겠어!"
    Jinil "뻔대야 애들 진짜 안오냐?? 거의 우리 셋이서만 일하는데?"

    show jangtuh at truecenter
    Jangjung "잘 하고 있냐??"
    Player "왜 이렇게 늦게 왔어 ㅠㅠㅠㅠ 얼른 가서 일 도와줘"
    Jangjung "ㅋㅋㅋㅋ 잘 하고 있구만 왜"
    Player "너 2시까지는 온다며… 벌써 3시야"
    Jangjung "아 나 수업 끝나고 애들이랑 팀플하느라 늦었어 ㅠㅠ"
    Player "하.. 알겠어 얼른 가서 진일이 도와줘"
    Jangjung "나 뭐하면 돼?"
    Player "지금 요리는 삼용이가 빨리빨리 잘해주고 있어서 괜찮은데 주문은 지금 워낙 많아서 진일이 혼자 감당하기 힘들어 ㅠㅠ 가서 얼른 진일이 도와줘"
    Jangjung "오케이~"
    Jinil "야 해장중 너 빨리 와서 좀 도와"

    scene black
    "장중이에 이어서 현재, 미래, 대현, 덕현이도 장터현장에 도착하기 시작했다."
    "일찍부터 일한 나, 진일, 삼용은 드디어 다른 친구들에게 일을 맡기고 쉴 수 있었다. "

    "오후 4시부터는 고객들이 하나 둘 씩 줄어들면서 장터현장이 한가해졌다."
    stop sound fadeout 1.0

    show jangtuh at truecenter
    Jangjung "야 뻔대야 우리 이제 정리할까?"
    Jinil "너네들 일 얼마나 했다고 벌써 정리해"
    Daehyun "근데 고객이 없으니까 정리해도 되지 않나?"
    Hyunjae "다 정리하지는 말고 메뉴판이랑 요리도구만 치워도 되지 않을까?"
    Samyong "그래도 사람들 더 올 수도 있으니까 6시까지는 놔두자"
    Ohduck "굳이…"
    Jinil "야. 솔직히 말해서 우리는 아침 일찍 손님 없을때부터 와서 계속 자리 지키고 일했는데 그럼 우리도 그때 치울걸 그랬네?"
    Player "왜 그래 얘들아…"
    Samyong "맞아 뻔대도 오늘 이거 하느라 고생많이 했어 ㅠㅠㅠ"
    Jinil "하…"
    Hyunjae "알겠어… 우리가 미안해 얘들아"
    Daehyun "그런 뜻으로 말 한게 아닌데… 미안해"
    Ohduck "고멘네…"
    Mirae "미안해 ㅠㅠㅠ 너네들 말이 맞아"
    Hyunjae "그래 우리 6시에 치우기 시작하자!"
    Daehyun "그러자!"
    Mirae "좋아!"
    Ohduck "요시!"
    Samyong "조금만 더 수고해 ㅋㅋ"

    "갑자기 장중이가 일하다 말고 나한테 따로 와서 이야기를 한다."

    Jangjung "뻔대야 우리 사람 진짜 안오는데 그냥 딴 장터 같이 갈래?"
    Jangjung "너도 오늘 일 많이 했는데 다른 장터 잠깐 가서 빠르게 먹고 오자."
    Jangjung "지금 다른 장터도 끝날 시간이라 음식이랑 술도 엄청 싸게 파는것 같아 ㅋㅋㅋ"

    menu:
        "간다":

            Player "그래 ㅋㅋ 우리 과 장터가 아직 끝나지는 않았지만 오늘 일을 열심히 했으니깐 잠깐 놀고 와도 괜찮지 않을까?"

            Jangjung "오케이~ 역시 우리 뻔대!!!
            그리고 거기서 술 싸게 팔면 사서 우리 애들이랑 같이 마시게 사오자.
            애들도 엄청 좋아할듯!"

            show other_jangtuh at truecenter

            "장중이와 술을 마시고 있는데 갑자기 전화가 울린다. 진일이다."
            Jinil "야 너 어디냐? 이제 곧 정리 할려고 하는데 얼른 와."
            Player "아 그래?? 헐 벌써 6시구나 알겠어 나 갈게!!"
            Jinil "해장중 얘는 또 어디갔냐… 혹시 둘이 지금 같이 있어?"
            Player "아...어"
            Jinil "둘이서 어디 갔…"
            Player "여보세요?"

            "진일이와 통화를 하다 갑자기 전화가 끊겼다. 불길한 예감이 들어 장중이에게 돌아가자고 할 무렵."

            Jinil "니들 여기 있었냐..?"

            Player "어….어"
            Jangjung "진일아 얼른 와 여기 장터 개 혜자야 ㅋㅋㅋㅋㅋ"

            Jinil "지금 나랑 장난쳐? 뭐하는거야 지금"
            Jinil "애들 다 우리 장터 정리하려고 도와주고 있는데 해장중 넌 여기서 뭐하냐?"
            Jinil "뻔대는 오전부터 수고했으니까 그렇다쳐도 넌 여기서 놀면 안되는거 아니냐?"

            Jangjung "아 알겠어 지금 가서 도와주면 되지 뭘 또 화를 내고 그래"

            Jinil "뻔대 너도 오늘 쉬고싶은건 이해하는데 그래도 해장중은 일하게 했어야지"

            Player "미안…"

            Jinil "아 일단 모르겠고 우리 장터 가서 정리하는거 도와주기나 해"

            Player "응.."

            #장중 파라미터 급격히 오름"
            $ jangjung.parameter += 40

            #진일 삼용 파라미터 내림"
            $ jinil.parameter -= 20
            $ samyong.parameter -= 20
            call parameter_maxmin_check from _call_parameter_maxmin_check_1

        "안간다":

            Player "아직 우리 과 장터가 안끝나서 지금 가기는 조금 그런데…"

            Jangjung "아 뻔대 뭐냐~ 실망이네. 어짜피 장터에 사람도 안오고 정리할때 맞춰서 오면 애들한테 피해도 안주는건데…"

            Player "미안 ㅠㅠ 그래도 혹시나 무슨일 생기면 총괄자가 있어야하니깐 나는 여기 있어야할 것 같아 ㅠㅠ"

            #장중 파라미터 내림
            $ jangjung.parameter -= 20

    $ day_or_evening = "evening"
    "오후 6시가 되었다. 여러가지 우여곡절이 있었지만 결국 장터는 무사히 끝났다."

    #장터 뒷풀이"
    play music "music/5.03_jangtuh_end.mp3"
    show cheers at truecenter
    "장터현장을 정리하고 우리는 다같이 뒷풀이를 하러 술집에 왔다"
    "장터에 도와주지 못한 친구들도 하나 둘씩 나타나며 뒷풀이에 참가하여 꽤 많은 인원이 모였다."

    Jinil "자자 주목~! 오늘 뻔대가 우리 학번중에 가장 열심히 일 했으니까 건배사 한답니다!!!"

    Hyunjae "올~~~~~"
    Jangjung "뻔대 멋있다!!!"
    Mirae "와!!!!"
    Samyong "한마디 해라!!!"
    "모두" "뻔대! 뻔대! 뻔대!"

    Player "오늘 모두 수고했고 열심히 번 돈으로 방학 때 좋은 곳으로 MT나 한번 더 가자!!! 자 문정과 하면 화이팅!"

    Player "문정과!!!"

    "모두" "화이팅!!!!!!"

    show after at truecenter

    Jinil "뻔대야 진짜 수고했다 ㅋㅋㅋ 너, 나 그리고 삼용이 아침부터 하느라 힘들었는데 마시고 죽자"

    Samyong "내일 수요일이야 ㅋㅋㅋ 우리 죽으면 안돼"

    Jangjung "ㅋㅋㅋ 맞아 역시 일하고 마시는 술은 꿀맛이다!"

    Jinil "넌 나중에 사람 없을 때 와서 개꿀 빨았잖아~ 그래서 술이 꿀맛인건가??"

    Jangjung "야 그래도 정리할때 일 개많이 했거든?"

    Jinil "응 그것도 점심 때에 비하면 아무것도 아님~"

    Player "ㅋㅋㅋ 모두 다 수고했어 얘들아"

    "장중이가 말한것 처럼 일하고 마신 술은 예상외로 진짜 맛있었다."
    "아침 일찍부터 저녁까지 일하고 술을 마신것은 처음이라서 그런가?"
    "나 말고 모두 다 그렇게 느꼈던 건지 예상외로 술자리가 길어지고 술값은 늘어났다."
    "아 모르겠다. 그래도 이번 학기 큰 행사가 막이 내려서 다행이다."

    scene black
    "정산을 했다. 장터가 성공적이었길 바라면서... 두근두근한 마음을 감출수가 없다."
    if jangtuh_pre_event == 4 :
        "장터 준비를 빠짐없이 참여하고 체계적으로 준비해서인지 엄청난 흑자가 났다."

        "장터 순이익 : 200만원\n뒷풀이 비용 : 50만원\n장터 후 총 금액 : 150만원"
        "장터 성적 : A, 과 분위기가 아주 좋아졌다."
        $ gwa_parameter += 5
        call parameter_maxmin_check from _call_parameter_maxmin_check_2

    elif jangtuh_pre_event == 3 or jangtuh_pre_event == 2 :
        "장터 준비를 조금 빠져서인지 겨우 흑자가 났다."

        "장터 순이익 : 100만원\n뒷풀이 비용 : 50만원\n장터 후 총 금액 : 50만원"
        "장터 성적 : B, 과 분위기가 좋아졌다."
        $ gwa_parameter += 3
        call parameter_maxmin_check from _call_parameter_maxmin_check_3

    elif jangtuh_pre_event == 1 :
        "장터 준비를 많이 빠져서인지 본전만 뽑았다."

        "장터 순이익 : 50만원\n뒷풀이 비용 : 50만원\n장터 후 총 금액 : 0원"
        "장터 성적 : C, 흑자는 아니지만 과 사람들이 서로 돈독해진 것 같다."
        $ gwa_parameter += 1
        call parameter_maxmin_check from _call_parameter_maxmin_check_4

    else :
        "뻔대 주제에 장터 준비를 다 빠져서인지 망했다."

        "장터 순이익 : 0원\n뒷풀이 비용 : 50만원\n장터 후 총 금액 : -50만원"
        "장터 성적 : D, 과 분위기 망했다."
        $ gwa_parameter -= 3
        call parameter_maxmin_check from _call_parameter_maxmin_check_5

    stop music fadeout 1.0
    #순이익 금액으로 장터가 성공했는지 판단

    ##장터 전 이벤트 4개 다 참여했을 시 순이익 200만원
    ##장터 전 이벤트 2,3개 참여했을 시 순이익 100만원
    ##장터 전 이벤트 1개 참여했을 시 순이익 50만원
    ##장터 전 이벤트 0개 참여했을 시 순이익 0원
    ##뒷풀이 비용은 항상 50만원으로 세팅

    ###화면에 나올것
    ###장터 순이익: ___원
    ###뒷풀이 비용: 50만원
    ###장터 후 총 금액: ___원
    ###장터 성적: A (4개), B (2,3개), C (1개),D (0개)

    call weekday_SNS from _call_weekday_SNS
    return
