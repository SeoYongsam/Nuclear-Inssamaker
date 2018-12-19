# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_jangjung_talk :
    if month == 3 :
        if week == 2 :
            if day == 1 :
                $ jangjung.add("날짜|3월 9일 월요일")
                $ jangjung.add("해장중|오올 뻔대~ 노래 엄청 잘하던데??")
                $ jangjung.add("연속|겸사 겸사 사투리도 잘하던데?? ㅋㅋㅋㅋ")
                $ jangjung.add("주인공|엌ㅋㅋㅋㅋ 그래도 호응해주고 같이 돌아봐줘서 고마웠음")
                $ jangjung.add("해장중|ㄴㄴㄴ 뭐 나도 동소제 관심 있었으니까")
                $ jangjung.add("연속|여튼 너 공연하면 꼭 갈게 ㅋㅋㅋㅋㅋ")
                $ jangjung.add("연속|동아리도 뻔대도 파이팅이다!")
                $ jangjung.add("주인공|ㄱㅅㄱㅅ")

            elif day == 4 :
                $ jangjung.add("날짜|3월 12일 목요일")
                $ jangjung.add("해장중|동아리 뒤풀이 끝나면 여기로 붙어~")
                $ jangjung.add("주인공|?? 여기가 어딘데?")
                $ jangjung.add("해장중|선배가 추천해준 곳인데")
                $ jangjung.add("연속|청두 거리에 임꺽정이라고")
                $ jangjung.add("연속|막걸리 맛있는 곳 있어")
                $ jangjung.add("주인공|오옹...그래 살아 남으면 갈게")
                $ jangjung.add("해장중|지금 여기 나말고 진일이랑 대현이도 있으니까 올 때 연락주삼~")
                $ jangjung.add("주인공|ㅇㅋㅇㅋ")

            elif day == 6 :
                $ jangjung.add("날짜|3월 14일 토요일")
                $ jangjung.add("해장중|뭐여 순환선 한바퀴 실화냐..")
                $ jangjung.add("연속|엌ㅋㅋㅋㅋ 난 그래도 집 슬슬 도착했는데")
                $ jangjung.add("연속|힘내서 집에는 잘 들어가고")
                $ jangjung.add("연속|총엠 고생했다ㅋㅋㅋㅋㅋ")
                $ jangjung.add("연속|다음주에 보자")

        elif week == 3 :
            if day == 1 :
                $ jangjung.add("날짜|3월 16일 월요일")
                $ jangjung.add("해장중|야 우리 진짜 과잠 맞추자")

            # elif day == 2 :
            #     $ jangjung.add("날짜|3월 17일 화요일")
            #     $ jangjung.add("해장중|너 미팅 해봤냐?? ㅋㅋㅋㅋ")

        elif week == 4 :
            if day == 0 :
                $ jangjung.add("날짜|3월 22일 일요일")
                if gwazam_finished == False :
                    # 투표 진행
                    $ jangjung.add("해장중|이거 투표로 되면 진짜 할거야? 하…. 걱정되네")

                else :
                    # 강제 종료
                    $ jangjung.add("해장중|과잠 맡느라 진짜 고생했어 ㅋㅋㅋ 우리 조만간 술 마시자")

            elif day == 4 :
                $ jangjung.add("날짜|3월 26일 목요일")
                $ jangjung.add("해장중|우리 뻔엠가자아아아아")
                $ jangjung.add("연속|뻔엠 지금쯤 추진하는거 어때 ㅋㅋㅋㅋ")

    elif month == 4 :
        if week == 1 :
            # if day == 1 :
            #     $ jangjung.add("날짜|4월 2일 월요일")
            #     $ jangjung.add("진일|엠티는 당연히 대별리지~")
            #     $ jangjung.add("연속|신숲은 무슨 거기로 하면 술마시다가 애들 다 도망간다니까?")
            #     $ jangjung.add("연속|뻔대야 너도 대별리가 좋지??")
            #     $ jangjung.add("연속|대별리 뽑아줘ㅋㅋㅋㅋ")

            if day == 6 :
                $ jangjung.add("날짜|4월 7일 토요일")
                $ jangjung.add("해장중|으어ㅓㅓ 진짜 죽을 것 같다..")
                $ jangjung.add("연속|뻔대야 너는 괜찮냐?")
                $ jangjung.add("주인공|아니..나도 죽을거 같음")
                $ jangjung.add("해장중|엌ㅋㅋㅋㅋㅋ 근데 진짜")
                $ jangjung.add("연속|마지막 기억이 언젠지 가물가물하다")
                $ jangjung.add("해장중|혹시 기억 남??")
                $ jangjung.add("주인공|ㄴㄴ 나도 죽어서 기억안남")
                $ jangjung.add("해장중|그렇냐...뭐 일단 푹 쉬어~")
                $ jangjung.add("연속|고생했슈~~")

        elif week == 3 :
            if day == 2 :
                $ jangjung.add("날짜|4월 17일 화요일")
                $ jangjung.add("해장중|으아아아아아아 공부 하기 싫어")
                $ jangjung.add("연속|으아아아아아")
                $ jangjung.add("연속|으아.아아아아아아.아아")
                $ jangjung.add("주인공|그만.")
                $ jangjung.add("해장중|ㅇㅋ")
                $ jangjung.add("주인공|공부해.")
                $ jangjung.add("해장중|ㅇㅋ")
                $ jangjung.add("주인공|ㅋㅋㅋㅋㅋㅋㅋ공부 안되면")
                $ jangjung.add("주인공 |잠깐 숨 좀 돌릴겸 CU가실?")
                $ jangjung.add("해장중|좋지좋지 곧 나감 ㄱㄷ")
                $ jangjung.add("주인공|ㅇㅋㅇㅋ")

        elif week == 4 :
            if day == 0 :
                $ jangjung.add("날짜|4월 22일 일요일")
                $ jangjung.add("해장중|우리 과도 장터 하지??")
                $ jangjung.add("주인공|아마 그럴 것 같은데?")
                $ jangjung.add("해장중|아 ㅇㅋㅇㅋ")
                $ jangjung.add("연속|다른 과 벌써 장터 시작한것 같아서")
                $ jangjung.add("연속|우리는 언제하나 해서 ㅋㅋ")
                $ jangjung.add("주인공|내가 한번 알아보고")
                $ jangjung.add("주인공|내일 단톡에 말할게 ㅋㅋㅋ")
                $ jangjung.add("해장중|오케이~")

    elif month == 5 :
        if week == 1 :
            if day == 0 :
                $ jangjung.add("날짜|5월 1일 일요일")
                $ jangjung.add("해장중|우리 내일 장보러 몇시에 가?")
                $ jangjung.add("연속|나 생각해보니까 수업 때문에 못갈 것 같아서 ㅠㅠ")
                $ jangjung.add("주인공|수업끝나고 갈 것 같은데??")
                $ jangjung.add("해장중|몇시?")
                $ jangjung.add("주인공|정하지는 않았는데 아마 오후 5시 쯤?")
                $ jangjung.add("해장중|아")
                $ jangjung.add("연속|조금 빠듯할것 같은데")
                $ jangjung.add("연속|가도록 노력해볼게 ㅋㅋ")

            elif day == 2 :
                $ jangjung.add("날짜|5월 3일 화요일")
                $ jangjung.add("해장중|야 나 몇시에 가면 되냐?")
                $ jangjung.add("주인공|시간 빌 때!!!")
                $ jangjung.add("해장중|정확히 언제?")
                $ jangjung.add("주인공|그냥 비는 시간 다... 일손이 계속 부족해 ㅠㅠ")

            elif day == 5 :
                $ jangjung.add("날짜|5월 6일 금요일")
                $ jangjung.add("해장중|오늘 술 레알로 ㄱㄱ?")
                $ jangjung.add("연속|우리 최근에 안마셔서")
                $ jangjung.add("연속|오늘 달리게 ㅋㅋㅋ")
                $ jangjung.add("주인공|나 오늘은 이미 늦은듯 ㅠㅠ")
                $ jangjung.add("해장중|꼭 그렇게...")
                $ jangjung.add("연속|단칼에 거절해야만 했....냐!!!!!!!!!!")
                $ jangjung.add("주인공|ㅋㅋㅋㅋ 술 맛있게 먹어")

        elif week == 2 :
            if day == 3 :
                $ jangjung.add("날짜|5월 11일 수요일")
                $ jangjung.add("해장중|우리 운동회 종목 뭐뭐있어?")
                $ jangjung.add("주인공|아직 다른반이랑 얘기 안해봐서 모르겠네")
                $ jangjung.add("해장중|막 뛰는거나 그런것 밖에 없으려나")
                $ jangjung.add("주인공|하고 싶은거 있어??")
                $ jangjung.add("해장중|나 그냥 운동을 별로 안좋아함 ㅋㅋㅋ")

            elif day == 6 :
                $ jangjung.add("날짜|5월 14일 토요일")
                $ jangjung.add("해장중|오늘 밤에 술 ㄱㄱ?")

        elif week == 3 :
            if day == 0 :
                $ jangjung.add("날짜|5월 15일 일요일")
                $ jangjung.add("해장중|뻔대야 우리 꼭 뒷풀이 다른 과 애들이랑 같이 해야돼?")
                $ jangjung.add("연속|나는 그냥 우리끼리 마셨으면 좋겠는데")

            elif day == 1 :
                $ jangjung.add("날짜|5월 16일 월요일")
                $ jangjung.add("해장중|김진일 백퍼 갠톡해서 우리 뭐라했지?")
                $ jangjung.add("연속|나한테도 왔더라 ㅋㅋㅋ")

            elif day == 5 :
                $ jangjung.add("날짜|5월 20일 금요일")
                $ jangjung.add("해장중|내일 둘이 한 잔 하자... 할 말도 있고")

        elif week == 4 :
            if day == 0 :
                $ jangjung.add("날짜|5월 22일 일요일")
                $ jangjung.add("해장중|와... ㅅㅂ")
                $ jangjung.add("연속|너 술먹고 꼴아서")
                $ jangjung.add("연속|나한테 업혀서 택시 탄거 기억나냐")
                $ jangjung.add("연속|너 진짜 진상 장난아니드라...")
                $ jangjung.add("연속|다음에 밥이나 사라")

            elif day == 6 :
                $ jangjung.add("날짜|5월 28일 토요일")
                $ jangjung.add("해장중|뻔대야")
                $ jangjung.add("연속|동아리 연습 잘 되가냐?")
                $ jangjung.add("연속|너 바빠서")
                $ jangjung.add("연속|내가 뻔모 추진하려고 하는데")
                $ jangjung.add("연속|불만 없지?")

    elif month == 6 :
        if week == 1 :
            if day == 0 :
                $ jangjung.add("날짜|6월 1일 일요일")
                $ jangjung.add("해장중|너는 오늘 못오지??")
                $ jangjung.add("연속|혹시 올 수 있으면 연락해")

            elif day == 4 :
                $ jangjung.add("날짜|6월 5일 목요일")
                $ jangjung.add("해장중|내일 기말고사라고 공연 못가")
                $ jangjung.add("연속|미안해")

        elif week == 2 :
            if day == 0 :
                $ jangjung.add("날짜|6월 8일 일요일")
                $ jangjung.add("해장중|너도 같이 공부할래??")
                $ jangjung.add("연속|아 인생 노답 진짜...")

            elif day == 4 :
                $ jangjung.add("날짜|6월 12일 목요일")
                $ jangjung.add("해장중|너 혹시 심개 족보 있냐 ㅋㅋㅋ")
                $ jangjung.add("연속|관악 족보 암기 대회라는데")
                $ jangjung.add("연속|아직 못 구했다ㅋㅋㅋ")

        elif week == 3 :
            if day == 2 :
                $ jangjung.add("날짜|6월 17일 화요일")
                $ jangjung.add("해장중|뻔대야")
                $ jangjung.add("연속|혹시 진일이 종파 온댔나??")
                $ jangjung.add("연속|진일이 오면 나도 가려고 ㅋㅋㅋㅋ")
                $ jangjung.add("연속|아 그리고")
                $ jangjung.add("연속|금지 오면 우리 좀 뭐라 하자")
                $ jangjung.add("연속|솔직히 너무 꼴보기 싫더라...")
                $ jangjung.add("연속|네가 분위기 좀 잡아줘")
    return
