image friend_2 = "fun_mt/friend_2.jpg"
image friend_3 = "fun_mt/friend_3.jpg"
image friend_4 = "fun_mt/friend_4.jpg"
image friend_5 = "fun_mt/friend_5.jpg"

label friend_2:
    "삼용이와 술을 마시기로 결정했다."

    show friend_2 at truecenter
    Samyong "오오~ 고생한 우리뻔대! 술이라도 한 잔 받어~"
    Samyong "진짜 고생 많았어!!"
    Player "에이 나 혼자만 한 건 아니지.."
    Player "진짜 너희한테는 고마움 밖에 없다.."
    Samyong "ㅋㅋㅋ그래 언제든 맡겨만 줘"
    Samyong "열심히 도와줄게~"

    scene black
    "삼용이와 얘기를 하며 소주 1병 정도를 더 비웠다."

    #삼용이와 파라미터 +
    return

label friend_3:
    "장중이와 술을 마시기로 결정했다."

    show friend_3 at truecenter
    Jangjung "예에 문정과에서 제일 고생하는 뻔대~ 술 한 잔 해야지!"
    Jangjung "넌 진짜 나 없었으면 어쩔 뻔 했냐? ㅋㅋㅋ"
    Player "ㅋㅋㅋ 진짜로 맞는 말이다"
    Player "너 처럼 과에 일 있을 때마다 도와주는 애들 있어서 힘낼 수 있는 듯"
    Jangjung "에이 과찬이야~ 일단 짠하자 짠!"
    Player "짠!"
    Jangjung "캬~ 오늘 따라 술이 다네"
    Player "진짜 달다! 재밌어서 그런가 봐"
    Jangjung "ㅋㅋㅋㅋ 맞음 맞음 더 마시자, 짠!"
    Player "짠!"

    scene black
    "장중이와 이야기를 하며 소주 1병 정도를 더 비웠다."

    #장중이와 파라미터 +
    return

label friend_4:
    "진일이를 찾으러 나가기로 결정했다."
    "다행히 진일이는 숙소 바로 앞에 있었다."

    show friend_4 at truecenter
    Player "야 김진일! 또 사라져서 깜짝 놀랐잖아!"
    Jinil "아 뻔대냐? 아 그냥 바람 좀 쐬러 나왔지."
    Player "어디 딴 데 가지말고 이 주변에만 있어랔ㅋㅋㅋ"
    Jinil "에이 이제 딴 데 안가지. 나온 김에 나랑도 한 잔 마셔야지, 잔 들고 와라"
    Player "엌ㅋㅋㅋ 그 소주는 어디서 나온거냐. 잠시만 기다려봐"
    Jinil "아 아니다 여기 잔 많이 남아있네, 여기서 마시자, 자 잔 드시고~"
    Player "엌ㅋㅋ 감사 감사~"
    Jinil "크~ 술 맛 좋다~ 뻔엠 준비하느라 고생많았다 뻔대야. 학기 초에 행사 많아서 바빴을텐데 항상 열심히 하더라."
    Player "아냐 너 없었으면 진짜 힘들었을 걸...애들도 투표 잘 안하고..."
    Jinil "크 그래그래 너도 이 형님이 고생하는 거 아네, 일단 한 잔 더 짠!"
    Player "엌ㅋㅋㅋㅋㅋ"
    Jinil "뭐 앞으로도 과에 일 생기거나 하면 편하게 말해. 계속 도와줄거니까."
    Player "크~ 앞으로는 갓 진일이라고 부를게. 잘 부탁함!"
    Jinil "그래그래."

    scene black
    "진일이와 말을 주고 받으면서 소주 1병 정도를 더 비웠다."
    #진일이와 파라미터 +
    return

label friend_5:
    "장중, 진일, 용삼의 술자리에 합류하기로 결정했다."
    "...뭔가 땅이 흔들리는 것 같다."

    show friend_5 at truecenter
    Player "으어..얘들아 여기서 뭐하고 있었냐..."
    Jangjung "엌ㅋㅋㅋㅋㅋㅋ 이 친구 많이 취했네, 야 괜찮냐?"
    Player "어...아마도 괜찮은듯??"
    Jinil "아니 전혀 안 괜찮아 보이는데, 아 뻔대 많이 약하네;;"
    Samyong "조절해 가면서 마셔야지.."
    Player "앗! 누가 술을 남기냐~ 내가 마셔야지?"
    Jangjung "엇"
    Jinil "하..."
    Player "크으~ 맛있다!!"
    Samyong "어휴..뭐 이런 거 하루이틀 보는 것도 아니고 적당히 마셔주자"
    Jangjung "오키오키"
    Jinil "뭐 애들도 거의 자러 간 거 같고, 뻔대는 우리가 챙겨야지"
    Player "...웁!"
    Jangjung "야야야!!! 여기서 토하면 안 됨!!!"
    Samyong "화장실! 화장실!!"
    Jinil "하...."

    scene black
    "애들이 내 몸을 씻겨주는 것 같다...이후 정신을 잃었다."
    #개별 파라미터 변화 없음
    $rest_point -= 1
    return
