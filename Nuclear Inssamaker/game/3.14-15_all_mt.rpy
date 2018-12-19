#이미지 선언
#image jangbal = "all_mt/jangbal.jpg"
image bus = "all_mt/bus.jpg"
image bus_inside = "all_mt/bus_inside.jpg"
image arriving = "all_mt/arriving.jpg"
image small_room = "all_mt/small_room.jpg"
image big_room = "all_mt/big_room.jpg"
image gogi = "all_mt/gogi.png"
image setting = "all_mt/setting.jpg"
image rice_kimchi = "all_mt/rice_kimchi.jpg"
image leaving = "all_mt/leaving.jpg"
image soondae = "all_mt/soondae.jpg"
image subway = "all_mt/subway.jpg"

# 3월 13일-14일 금-토 총엠 이벤트
# month3 week2 day5
label all_mt:
    scene black
    "오늘은 과 총MT가 있는 날이다.\n"
    extend "나는 아침부터 MT에서 먹을 음식, 과자, 술을 사는 역할인 장발대로 나왔다."

    show jangbal at truecenter
    Jangjung "너네들도 장발대로 나왔냐?"
    Jinil "다들 술 도수 낮은걸로만 살까봐 감시하러 왔지"
    Samyong "난 술 안주 고르게! 내가 오늘 MT가서 취두부 요리 해줄게!"
    Player "취두부?!?! 야 누가 삼용이 좀 말려봐..."
#    Jinil "삼용아"
#    Samyong "응?"
#    Jinil "너 코에 취두부 박히기 싫으면 가만히 있어"
#    Samyong "응..."
#    Player "야 그건 너무 심하잖아 ㅋㅋㅋ"

    "장을 다 보고 나서는 근처 식당에서 다같이 점심을 먹기로 했다.\n"
    extend "이후 짐을 나눠들어 MT장소까지 가는 버스를 타러 가기로 했다."

    show bus at truecenter
    "버스를 탔다.\n"
    extend "아직 입학한지 얼마 안된 3월 초이지만 벌써부터 친한 무리들이 생기기 시작한 것 같다."
#    "하나 둘 씩 아는 사람 옆에 앉는 사람들이 있는 반면 아직 친해지지 못해 누구가 옆에 앉기만을 기다리는 사람들도 있다."
    "이미 자리가 차있어서 앉을 자리가 얼마 없지만 삼용이, 진일이, 그리고 장중이의 옆자리가 각각 비어있다.\n"
    extend "누구 옆에가서 앉을까?"

    menu:
        "진일이 옆":
            show bus_inside at truecenter
            Jinil "한눈에 알아보고 인싸 자리에 앉았네 뻔대?"
            extend "역시 사람 볼줄 알아~ 우리 지금부터 한잔 하는거 어때 ㅋㅋㅋ"
            Player "버스 안에서 술을 어떻게 마셔 ㅋㅋㅋㅋㅋ"
            Jinil "불가능은 없다!!!"

            # 진일 파라미터 +
            $ jinil.parameter += 20
            call parameter_maxmin_check

        "장중이 옆":
            show bus_inside at truecenter
            Jangjung "뻔대쓰~ 자리 선정 오지구여~ "
            Player "장중이~ 뭐해!!!"
            Jangjung "나 그냥 핸드폰으로 우리 동기들끼리 나중에 할 수 있는거 찾아보고 있었어 ㅋㅋㅋ"
            Player "벌써부터 다음에 놀거 생각하고 있어??\n"
            extend "대단하다..."
            Jangjung "우리의 청춘을 허되게 낭비할수는 없으니깐!!!"

            # 장중 파라미터 +
            $ jangjung.parameter += 20
            call parameter_maxmin_check

        "삼용이 옆":
            show bus_inside at truecenter
            Samyong "야야 여기 얼른 와봐!"
            Player "응? 무슨일이야?"
            Samyong "지금 현재랑 미래 같이 앉은거 보여?\n"
            extend "저 둘 수상해~"
            Player "그럴수도 있지 왜 ㅋㅋㅋ 둘이 친한가보지"
            Samyong "아니야... 만리장성 걸고 저 둘이 뭔가 있어"

            # 삼용 파라미터 +
            $ samyong.parameter += 20
            call parameter_maxmin_check

    show arriving at truecenter

    "드디어 MT 장소에 도착했다.\n"
    extend "애들이랑 얘기하면서 왔더니 시간이 금방 지나갔다."
    "한것은 없지만 벌써부터 피곤하다." #선배들이 다 같이 할 레크리에이션을 강당에서 짤 동안 후배들은 숙소에 들어가서 잠깐 쉬라고 했다."
    "친구들과 빨리 친해지고 놀고싶지만 아침부터 추운 밖을 누비다가 따뜻한 방에 누워있으니까 졸리기 시작한다..."

    scene black

    "음… 아 얼마동안 잔거지??"

    $ day_or_evening = "evening"

    show small_room at truecenter

    Player "대현아 지금 몇시야??"

    Daehyun "오후 5시! 이제 후발대로 오는 사람들 곧 도착한대\n"
    extend "우리도 이제 슬슬 나가서 저녁 먹을 준비하자!"

    show arriving at truecenter

    "사람들이 하나 둘 도착하면서 어느 덧 숙소 밖은 사람들로 차있다."
    "바깥에 비치되어있는 간이책상에 모여서 식기를 셋팅하는 사람들,\n고기를 굽기 위해 불을 지피는 사람들,\n밥과 반찬을 방 부엌에서 준비하고 있는 사람들이 보인다."
    "나도 도와야할텐데 어디로 갈까?"

    menu:
        "식기 셋팅":
            show setting at truecenter
            Jangjung "뻔대야 얼른 와 식기 셋팅 개꿀임 ㅋㅋㅋ"
#            Player" 응? 뭐가 개꿀이야??"
#            Jangjung "식기 셋팅하러 온거 아니야? 이거 할거 별로 없어 ㅋㅋ
#            그리고 고기 받을 수 있는 좋은 자리 먼저 차지 할 수 있어 ㅋㅋㅋ"
            Player "올~ 장중이 예리한데??\n"
            extend "빨리 셋팅하고 저기 고기 불판 쪽으로 가자"
            Jangjung "가즈아~"
            "장중이하고 좀 친해진 것 같다."

            # 장중 파라미터 +
            $ jangjung.parameter += 20
            call parameter_maxmin_check

        "고기 굽기":
            show gogi at truecenter
            Jinil "마침 사람 부족했는데 잘됐다\n"
            extend "뻔대야 여기 와서 같이 고기나 굽자"
            Player "뭐야 여기 왜 사람이 너 밖에 없어?"
            Jinil "몰라 다들 고기 굽기 싫어서 식기 셋팅하러 빠진것 같아"
            Player "그렇네 ㅋㅋ..."
            Jinil "너라도 여기 와서 그래도 좀 낫네\n"
            extend "역시 뻔대는 다르다"
            "진일이하고 좀 친해진 것 같다."

            # 진일 파라미터 +
            $ jinil.parameter += 20
            call parameter_maxmin_check

        "밥/반찬 준비하기":
            show rice_kimchi at truecenter
#            Samyong "아무나 여기 김치랑 밥좀 가져가~"
#            Player "삼용아 이리 줘 내가 애들한테 전달할게!"
            Samyong "뻔대 넌 언제 여기 왔어!"
            Player "나 방금!"
            Samyong "잘됐다\n"
            extend "그러면 내가 밥 퍼서 애들한테 전달할테니까 넌 여기서 김치 좀 썰고있어줘\n"
            extend "혼자 하려니까 너무 힘드네"
#           Player "알겠어!"
            "삼용이하고 좀 친해진 것 같다."

            # 삼용 파라미터 +
            $ samyong.parameter += 20
            call parameter_maxmin_check

    show big_room at truecenter
    "저녁식사는 엠티 분위기 덕분에 평소보다 더 맛있었던 것 같았다."
    "잠시 쉬다가 레크리에이션을 하고 술을 마시러 가볼까?!"

    call change_SNS
    $ day += 1
    if day < 7 :
        $ day_for_show = (week-1)*7 + day + 1
    $ YoIl = day_name[day]
    $ day_or_evening = "day"

    scene black
    "…..으음…. 응?"
    "난 분명 레크리에이션 하러 갔었는데 왜 방에 누워있지?"
    "잠깐 밖은 왜 밝지???? 뭐지????"

    show small_room at truecenter
    "방문이 열리며"
    Jinil "야 ㅋㅋㅋㅋㅋ 너 일어났냐?\n"
    extend "어제 장난 아니더라 ㅋㅋㅋㅋ"
    Player "아… 나 어제 도대체 얼마나 마신거냐"
    Samyong "기억 안나?\n"
    extend "너 갑자기 막 푸쉬업하고 술 계속 원샷하고 난리였어 ㅋㅋㅋㅋ"
    Jinil "진짜 상남자 ㅋㅋㅋ\n"
    extend "내가 인정 잘 안하는데 인정한다 뻔대야"
    Samyong "일단 우리 여기 정리하고 갈 준비하자"

    show leaving at truecenter
#    하지만 내가 가장 많이 피곤해 보였는지 사람들이 나를 볼때마다 괜찮냐고 물어본다."
#    "어제 술주정이 재밌었는지 날 보고 피식하며 웃는 동기, 선배들도 많았다."
    "숙소를 정리하고 엠티장소를 떠났다.\n남은 친구들 그리고 선배들과 함께 집에 가려고 버스를 탔다."
    "다들 술을 많이 마셔서 그런지 피곤해 보인다."

    show bus_inside at truecenter
    Jangjung "야 너네 근데 해장 안하냐?"
    Jinil "아 할까? 속 풀어야하긴 하는데"
#    Samyong "좋아!!! 근데 뭐먹지?? 해장으로는 마라탕이 최곤데"
#    Jinil "무슨 마라탕이야 ㅋㅋㅋ 그냥 뼈해장국이지"
#    Jangjung "나 멀리 못갈것 같아… 그냥 대충 아무때나 가서 먹자"
    Samyong "음... 그럼 버스 정류장 근처 순대국밥집 있는데 거기로 갈까?"
#    Jangjung "으아 빨리 가자"
    Jinil "뻔대야 너는 안가?"

    menu:
        "해장하러 간다":
            Player "가자... 나도 해장해야할 것 같아"

            show soondae at truecenter
            Jangjung "으어어~~ 시원하다~~"
            Jinil "으!!! 이거지"
            Samyong "와 순대국으로 해장하니까 좋네"
            Player "으아~ 너무 좋다"

            "집에 바로 가서 쉬지 못해서 좀 힘들었지만 친구들하고 다같이 친해졌다."
            #선택 간다 = 친구 파라미터 모두 업 + 체력 소모
            $ jangjung.parameter += 20
            $ jinil.parameter += 20
            $ samyong.parameter += 20
            $ hp -= 50
            call parameter_maxmin_check

        "집에 바로 간다":
            Player "아 나는 집에 빨리 들어가서 쉴래 ㅠㅠㅠ"
            Jangjung "야 속 풀고가야 집에가서도 안 괴로워"
            Samyong "근데 뻔대 많이 힘든것 같다... 보내주자"
            Jinil "뻔대 약한 모습 보기 안좋다~"
            "친구들의 따가운 눈총이 느껴진다."
            #안 간다 = 친구 파라미터 그대로 + 체력 유지 - 바뀌는 게 없음

    $ day_or_evening = "evening"

    show subway at truecenter
    "이제 드디어 집으로 간다!"
    "최대한 빨리 집에 가고싶지만 오늘따라 지하철에 사람이 많은것 같다."
    "그냥 순간이동 하고 싶다…"

    scene black

    call change_SNS
    $ day += 1
    if day < 7 :
        $ day_for_show = (week-1)*7 + day + 1
    $ YoIl = day_name[day]
    $ day_or_evening = "day"
    jump weekday_SNS

    return
