# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_group_talk :
    if month == 3 :
        if week == 1 :
            if day == 1 :
                $ grouptalk.add("날짜|3월 2일 월요일")
                $ grouptalk.add("장중|테스트")
                $ grouptalk.add("연속|잘 되려나\n되겠지")
                $ grouptalk.add("진일|죽어라!!!")
                $ grouptalk.add("삼용|즐거운 하루가 되길")
                $ grouptalk.add("동아|으아악\n테스트")
                $ grouptalk.add("연속|잘 되려나\n되겠지")
                $ grouptalk.add("미래|난 현재 여친\nㅋㅋ")
                $ grouptalk.add("주인공|이것도 테스트")

            elif day == 2 :
                $ grouptalk.add("날짜|3월 3일 화요일")
                $ grouptalk.add("삼용|테스트")

            elif day == 3 :
                $ grouptalk.add("날짜|3월 4일 수요일")
                $ grouptalk.add("장중|테스트")

            elif day == 4 :
                $ grouptalk.add("진일|테스트")

            elif day == 5 :
                $ grouptalk.add("미래|테스트")

            elif day == 6 :
                $ grouptalk.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ grouptalk.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ grouptalk.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ grouptalk.add("삼용|테스트")

            elif day == 3 :
                $ grouptalk.add("장중|테스트")

            elif day == 4 :
                $ grouptalk.add("장중|테스트")

            elif day == 5 :
                $ grouptalk.add("장중|테스트")

            elif day == 6 :
                $ grouptalk.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ grouptalk.add ("현재|아 총엠에서 마신 술 아직도 안깬듯 ㅠㅠ")
                $ grouptalk.add ("미래|그러게 조절하며 마시지 현재야아아아~~~ ㅠㅠㅠ")
                $ grouptalk.add ("금지|얘들아 나 벌써 과제 나왔어…")
                $ grouptalk.add ("삼용|맞아… 근데 총엠에서 선배들 과잠 조녜드라!")
                $ grouptalk.add ("대현|헐 나도 그 생각!!! 우리도 얼른 맞췄으면 좋겠다!!! 과잠 가즈아~")
                $ grouptalk.add ("장중|야 우리는 과잠 안맞추냐 뻔대야")
                $ grouptalk.add ("진일|일해라 노예야 ㅋㅋ")
                $ grouptalk.add ("주인공|와 진짜 총엠 다녀오자마자 부려먹는다고? 하… 도비는 일해야지")

            elif day == 1 :
                $ grouptalk.add ("장중|우리 그래서 과잠은 언제 맞추나여ㅕㅕㅕㅕㅕ")
                $ grouptalk.add ("진일|과잠준비위원회라는 걸 따로 만드는게 좋지 않을까?")
                $ grouptalk.add ("대현|오! 그게 좋을듯")
                $ grouptalk.add ("미래|응응 그래야 뭐라도 진행될것 같아 ㅠㅠ")
                $ grouptalk.add ("삼용|와 심리학과는 벌써 과잠 맞췄다는데??? 이거 봐봐 진짜 잘 맞췄다 ㅠㅠㅠ")
                $ grouptalk.add ("현재|와 진짜 예쁘다… 우리도 그럼 얼른 과준위 만들자. 일단 그럼 XX랑 나 할래 ㅋㅋㅋ 또 하고싶은 분?")
                $ grouptalk.add ("삼용|나나나나나나나나")
                $ grouptalk.add ("진일|과잠 디자인이면 또 내가 나설 차례가 왔군")
                $ grouptalk.add ("장중|오케이~ XX야 너가 톡방 파")

            elif day == 2 :
                $ grouptalk.add ("대현|연대 경영이랑 미팅할 남자분 빠르게 2분 모십니다")
                $ grouptalk.add ("장중|오오…. 자리 있음?")
                $ grouptalk.add ("대현|알콜 중독자 불가능")
                $ grouptalk.add ("삼용|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("주인공|나는 가능?")
                $ grouptalk.add ("대현|뻔대는 노예라서 불가능")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("주인공|와 진짜 너무하닼ㅋㅋㅋㅋㅋㅋ")

            elif day == 3 :
                $ grouptalk.add ("주인공|애들아, 우리가 진짜 개멋있는 과잠 만들듯 ㅋㅋㅋ")
                $ grouptalk.add ("금지|와 진짜 기대된다! 빨리 사고 싶다 ㅋㅋㅋ")
                $ grouptalk.add ("대현|오오 예시 나옴?? 뭐있어 ㅋㅋㅋ")
                $ grouptalk.add ("진일|야 내가 미는게 제일 멋있다 그걸로 하자 ㅋㅋㅋ")
                $ grouptalk.add ("현재|개궁금하다 ㅋㅋㅋ")
                $ grouptalk.add ("주인공|기대해라 ㅋㅋㅋㅋ")

            elif day == 4 :
                $ grouptalk.add ("주인공|우리가 과잠 후보 3개 만들었는데, 올릴게 애들아")
                $ grouptalk.add ("대현|와 대박 진짜 빨리 올려줘 ㅋㅋㅋ")
                $ grouptalk.add ("주인공|이미지 1(), 이미지 2(), 이미지 3()")
                $ grouptalk.add ("장중|아무리 봐도 내게 제일 예쁘다 ㅋㅋㅋ 3번 투표해라 애들아")
                $ grouptalk.add ("진일|멋하면 카모 아니냐 ㅋㅋㅋ 야상과잠 존멋이다 2번 투표해줘 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|누가봐도 1번이 제일 예쁘다 ㅋㅋㅋ")
                $ grouptalk.add ("금지|어, 생각보다 별론데….?나 안사고 싶은데ㅠㅠ")
                $ grouptalk.add ("주인공|애들아 최대한 빨리 투표 해주라!")
                $ grouptalk.add ("미래|ㅇㅋㅇㅋ")
                $ grouptalk.add ("SYSTEM|투표 결과 1안 | 8 /  2안 | 6 / 3안 | 4")
                $ grouptalk.add ("SYSTEM|투표를 더 진행하시겠습니까? 투표 / 선택하기")
                $ grouptalk.add ("SYSTEM|어떤 과잠을 선택하시겠습니까?")

            elif day == 5 :
                # (강제 선택한 경우)
                $ grouptalk.add ("금지|ㅠㅠ 나는 안 살래… 돈이 너무 없어 ㅠ")
                $ grouptalk.add ("현재|음…. 그래도 고생했어 과준위 ㅎㅎㅎ")
                $ grouptalk.add ("미래|맞아맞아 ㅠㅠㅠ")
                $ grouptalk.add ("진일|야 진짜 어떻게 이러지 ㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("대현|에이....금지야ㅠㅠ 그래도 ㅠㅠ 첫 과잠인데 사자")
                # (투표 연장한 경우)
                $ grouptalk.add ("주인공|애들아 그래도 최대한 민주적으로 가려고 의견 수렴하니까 투표 빨리 해줘 ㅠㅠ 부탁할게!")
                $ grouptalk.add ("진일|빨리빨리 하자.")
                $ grouptalk.add ("장중|과잠위 고생했으니까 빨리 해주세요!!")
                $ grouptalk.add ("삼용|하오하오!")
                $ grouptalk.add ("미래|ㅋㅋㅋㅋ 근데 현재야 너 저거 잘 어울리겠는데?")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("대현|아 진짜 나가서 연애질해라 ㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|근데 대현이 모쏠 실화냐??ㅋㅋㅋㅋ")
                $ grouptalk.add ("대현|야 아니야 ㅋㅋㅋㅋ 나 연애해봤어 ㅋㅋㅋㅋ 어이가 없다")
                $ grouptalk.add ("진일|ㅋㅋㅋㅋㅋ 니들이 사랑을 아냐? ")
                $ grouptalk.add ("장중|와 진일이 갬성 빼앰~~~ ")
                $ grouptalk.add ("SYSTEM | 투표 결과 1안 | 11 /  2안 | 8 / 3안 | 5")
                $ grouptalk.add ("SYSTEM | 투표를 연장하시겠습니까? Y/ N ")

            elif day == 6 :
                # 강제 종료
                $ grouptalk.add ("장중|술~ 이 한잔 생각 나~는 밤")
                $ grouptalk.add ("현재|마치~ 있는 것 같아요~")
                $ grouptalk.add ("대현|그~ 좋았던 시~절들")
                $ grouptalk.add ("미래|이젠 모~두 한숨만 되네요~")
                $ grouptalk.add ("진일|??? 다들 갑자기 왜이래… 장중이 술 땡기면 ㄱㄱ?")
                $ grouptalk.add ("장중|이거 노래임 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|오 이거 무슨 노래야???")
                $ grouptalk.add ("주인공|임창정의 소주한잔!!!")

                # 투표 할 시에
                $ grouptalk.add ("주인공|근데 님들아 투표좀~~~~")
                $ grouptalk.add ("삼용|투표 가즈아~!!!!")
                $ grouptalk.add ("진일|아직도 B가 안될거라고 생각하는 흑두루미들 없재?")
                $ grouptalk.add ("대현|자하연 물 온도 몇도냐 ㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋ")

        elif week == 4 :
            if day == 0 :
            # 투표 진행시
                # 단톡
                $ grouptalk.add ("진일|역시 내게 제일 멋있네, b안이 제일 높네")
                $ grouptalk.add ("장중|투표 실화냐….")
                $ grouptalk.add ("현재|저걸 어떻게 입냐 ㅠㅠ")
                $ grouptalk.add ("삼용|애들아 a안 밀면 b안 이길 수 있어, 영차영차 외치자!, 영")
                $ grouptalk.add ("대현|차")
                $ grouptalk.add ("대현|영")
                $ grouptalk.add ("장중|차")
                $ grouptalk.add ("진일|영차한다고 되겠다 ㅉㅉ")
                $ grouptalk.add ("주인공|에이 진일아~")


            # 투표 강제 종료시
                # 단톡
                $ grouptalk.add ("대현|우리 과잠은 언제 나오지??")
                $ grouptalk.add ("주인공|아마 곧 나올 것 같은데 ㅋㅋㅋ 우리 과잠 진짜 예쁜 것 같아!")
                $ grouptalk.add ("금지|아닌 것 같은데….ㅠ")
                $ grouptalk.add ("진일|에이 입어보면 다르다 진짜 ㅋㅋㅋ")
                $ grouptalk.add ("미래|그래 ㅋㅋㅋ 예뻐도 안 예뻐도 우리가 같이 입는게 의미가 있지")
                $ grouptalk.add ("현재|역시 미래다 ㅋㅋㅋㅋ")
                $ grouptalk.add ("장중|으~ 진짜 너네 적당히해라")
                $ grouptalk.add ("현재|싫은데 싫은데???ㅋㅋㅋㅋ")

            elif day == 1 :
            # 투표 종료시
                #   단톡
                $ grouptalk.add ("주인공|애들아 우리 이제 우리끼리도 밥약하자 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|오 또 뻔대가 일한다 ㅋㅋㅋㅋ 나 완전 좋아 ㅋㅋㅋ 나는 이번주 월,화, 수, 목 12시 반 가능해")
                $ grouptalk.add ("장중|나도나도 ㅋㅋㅋㅋ 근데 나는 화, 수만 학교 와서 ㅋㅋㅋ 그때만 될 것 같아")
                $ grouptalk.add ("진일|와 장중이 주2 실화야??? 수요일 저녁에 출국하면 4박 5일로 여행가겠다 ㅋㅋㅋ")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋ 미래랑 나도 갈까? 갈 수 있을 것 같아")
                $ grouptalk.add ("대현|수 ㄱㄱㄱㄱ, 장중이 엄마한테 18학점이라고 하고, 절반 등록금깡한거 아니야?")
                $ grouptalk.add ("장중|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

            # 투표 지속시
                # 단톡
                $ grouptalk.add ("진일|애들아 곧 24일에 투표 마감인데 투표 아직 안한 사람은 해줘!")
                $ grouptalk.add ("주인공|지금까지 투표 안하면 뻔대가 곤란하다는게 학계의 정설")
                $ grouptalk.add ("장중|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("삼용|과준위가 힘빠진다는 것도 유력한 가설")
                $ grouptalk.add ("대현|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|빨리 해주자 애들아 ㅋㅋㅋㅋ")
                $ grouptalk.add ("주인공|저녁까지 안해주시면 갠톡들어갑니다~")


            elif day == 2 :
            #   투표 마감시
                # 단톡
                $ grouptalk.add ("현재|우리 과잠은 언제오지 ㅋㅋㅋ 빨리 입고 싶은데")
                $ grouptalk.add ("진일|ㅋㅋㅋ 진짜 간지다 누가 봐도 눈에 띌듯 ㅋㅋㅋㅋ")
                $ grouptalk.add ("금지|그게 문제지….ㅠㅠ")
                $ grouptalk.add ("주인공|에이 아직 안 입어봤는데 그러지 말자 ㅋㅋㅋㅋ")
                $ grouptalk.add ("장중|우리 내일 점모 맞지?")
                $ grouptalk.add ("대현|뭐 먹지?? 중국음식?")
                $ grouptalk.add ("삼용|헐… 개좋아")
                $ grouptalk.add ("주인공|ㅋㅋㅋㅋ 삼용이 배려로 내일은 중식먹자!")
                $ grouptalk.add ("현재|좋아!!")

            # 투표 지속시
                # 단톡
                $ grouptalk.add ("주인공|오늘이 투표 마지막 날입니다! 예쁜 과잠을 선택해주세요~")
                $ grouptalk.add ("장중|진짜 과준위 4일동안 회의하고 정한 과잠입니다ㅠ 여러분 투표 부탁드려요!")
                $ grouptalk.add ("진일|그래 애들아 투표 좀 해라")
                $ grouptalk.add ("삼용|지금 투표하면 내가 원하는 걸로 할 수 있어 애들아!!!")
                $ grouptalk.add ("금지|음…..")
                $ grouptalk.add ("대현|나는 했어 과준위 ㅠㅠ 너무 고생한다 애들아 투표하자!!")
                $ grouptalk.add ("주인공| 고마워 다들 ㅋㅋㅋㅋ 다들 후보들이 너무 예뻐서 고민하는거지 뭐 ㅋㅋㅋ 내가 봐도 어렵다 ㅋㅋㅋ 여튼 저녁까지는 투표 마감할게요! ")


            elif day == 3 :
                # 단톡
                $ grouptalk.add ("장중|이제 과잠바는 해결됬겠다 뻔엠 ㄱㄱ?")
                $ grouptalk.add ("현재|헐 맞다 우리 뻔엠도 가야되지??")
                $ grouptalk.add ("장중|ㅋㅋㅋㅋ 다들 까먹고 있었나 보네")
                $ grouptalk.add ("진일|에이~ 우리끼리 술마시는 행사인데 어떻게 까먹어 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|와 우리 뻔엠도 가?? 과잠 맞추자마자 뻔엠 계획도 세우고 이번학기 개잼!!!")
                $ grouptalk.add ("대현|가즈아~~!")
                $ grouptalk.add ("미래| 행사가 끊임없닼ㅋㅋㅋㅋ 넘좋아!")

            elif day == 4 :
                # 단톡
                $ grouptalk.add ("주인공|그럼 우리 내일 뻔엠 날짜 정할래??")
                $ grouptalk.add ("장중|말 나온김에 지금 어때?!!!")
                $ grouptalk.add ("미래|현재가 오늘 바빠서 카톡을 못볼 것 같아서...ㅠㅠ 오늘 말해놓고 내일 정하는게 좋을 것 같아 ")
                $ grouptalk.add ("장중|아 ㅇㅋㅇㅋ")
                $ grouptalk.add ("삼용|ㅇㅋㅇㅋ가 무슨 뜻이야??")
                $ grouptalk.add ("진일|아 맞다 얘 중국에서 왔지 ㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|ㅋㅋㅋㅋ ㅇㅋㅇㅋ  = 오키오키! 알았다는 말이야 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|아하!")
                $ grouptalk.add ("대현|앞으로도 모르는 말 있으면 물어봐 삼용쓰 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|ㅇㅋㅇㅋ")
                $ grouptalk.add ("주인공|얘들아 뻔엠 날짜 내일 정하는 걸로 한다??")
                $ grouptalk.add ("삼용|ㅇㅋㅇㅋ")
                $ grouptalk.add ("대현|굿굿")


            elif day == 5 :
                # 단톡
                $ grouptalk.add ("주인공|얘들아 우리 뻔엠 언제 갈래?!!!!")
                $ grouptalk.add ("장중|뻔엠!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                $ grouptalk.add ("대현|다들 언제가 좋아??")
                $ grouptalk.add ("현재|주중에는 수업이 있으니까 금,토 아니면 토,일??")
                $ grouptalk.add ("미래|져아져아~")
                $ grouptalk.add ("삼용|나도 좋아!!")
                $ grouptalk.add ("주인공|중간고사 전에 가는게 좋으니까 다음주 금,토로 정하는게 어때??")
                $ grouptalk.add ("진일|콜")
                $ grouptalk.add ("삼용|콜")
                $ grouptalk.add ("장중|콜")
                $ grouptalk.add ("대현|쿨")
                $ grouptalk.add ("현재|꿀")
                $ grouptalk.add ("미래|꿀꿀")
                $ grouptalk.add ("진일|그만해라~")

            elif day == 6 :

                # 단톡
                $ grouptalk.add ("삼용|우리 근데 뻔엠 전에는 과잠 오겠지??")
                $ grouptalk.add ("장중|으아아아아 과잠 기대된다!!!")
                $ grouptalk.add ("진일|ㅋㅋㅋ 좀 기다려 이 과잠무새들아 어떻게든 되겠지")
                $ grouptalk.add ("금지|난 과잠 주문 안했는데 ㅎㅎ")
                $ grouptalk.add ("미래|응??? 왜 주문 안했어 ㅠㅠㅠㅠ")
                $ grouptalk.add ("금지|그냥 그렇게 됐어 ㅋㅋㅋ")
                $ grouptalk.add ("미래|지금이라도 주문해 ㅠㅠㅠ")
                $ grouptalk.add ("금지|그럴까??")
                $ grouptalk.add ("대현|?")
                $ grouptalk.add ("삼용|이미 주문 들어가서 그건 안될것 같아…")
                $ grouptalk.add ("현재|ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ 까비…")
