# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_group_talk :
    if month == 3 :
        if week == 1 :
            if day == 0 :
                $ grouptalk.add("날짜|3월 1일 일요일")

            elif day == 1 :
                $ grouptalk.add("날짜|3월 2일 월요일")
                $ grouptalk.add("장중|테스트")
                $ grouptalk.add("연속|잘 되려나\n되겠지")
                $ grouptalk.add("진일|안녕")
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
                $ grouptalk.add("날짜|3월 15일 일요일")
                $ grouptalk.add("주인공|이것도 테스트")
                $ grouptalk.add("주인공|이것도 테스트ㅁㄴㅇ러ㅏㅣㅁ넝라ㅣㅓㅁ나ㅣㅇ러미나")
                $ grouptalk.add("주인공|ㅁㄴ어라ㅣ먼아리ㅓㅁㄴ이러미ㅏㄴ어라ㅣㅁ넝리ㅏㅁㄴㅇ러ㅣㅁㄴㅇㄹ")
                $ grouptalk.add("현재|아 총엠에서 마신 술 아직도 안깬듯 ㅠㅠ")
                $ grouptalk.add("미래|그러게 조절하며 마시지 현재야아아아~~~ ㅠㅠㅠ")
                $ grouptalk.add("금지|얘들아 나 벌써 과제 나왔어…")
                $ grouptalk.add("삼용|맞아… 근데 총엠에서 선배들 과잠 조녜드라!")
                $ grouptalk.add("대현|헐 나도 그 생각!!!우리도 얼른 맞췄으면 좋겠다!!!과잠 가즈아~")
                $ grouptalk.add("장중|야 우리는 과잠 안맞추냐 뻔대야")
                $ grouptalk.add("진일|일해라 노예야 ㅋㅋ")

            elif day == 1 :
                $ grouptalk.add("날짜|3월 16일 월요일")
                $ grouptalk.add("장중|우리 그래서 과잠은 언제 맞추나여ㅕㅕㅕㅕㅕ")
                $ grouptalk.add("진일|과잠준비위원회라는 걸 따로 만드는게 좋지 않을까?")
                $ grouptalk.add("대현|오! 그게 좋을듯")
                $ grouptalk.add("미래|응응 그래야 뭐라도 진행될것 같아 ㅠㅠ")
                $ grouptalk.add("삼용|와 심리학과는 벌써 과잠 맞췄다는데??? 이거 봐봐. 진짜 잘 맞췄다 ㅠㅠㅠ")

                $ grouptalk.add("현재|와 진짜 예쁘다… 우리도 그럼 얼른 과준위 만들자. 일단 그럼 XX랑 나 할래 ㅋㅋㅋ 또 하고싶은 분?")
                $ grouptalk.add("삼용|나나나나나나나나")
                $ grouptalk.add("진일|과잠 디자인이면 또 내가 나설 차례가 왔군")
                $ grouptalk.add("장중|오케이~ XX야 너가 톡방 파")

#            elif day == 2 :
#                $ grouptalk.add("날짜|3월 17일 화요일")
#                $ grouptalk.add("주인공|과잠준비위원회 지원해주셔서 감사합니다!")
#                $ grouptalk.add("장중|동기가 일하는데 도와줘야지!")
#                $ grouptalk.add("진일|카모로하면 멋있을 것 같다 ㅋㅋㅋㅋ")
#                $ grouptalk.add("삼용|나는 빨간색에 용무늬가 들어갔으면 좋겠는데 ㅋㅋㅋ")
#                $ grouptalk.add("주인공|오 독특하고 좋은데? 근데 우리 손목에는 이름 적을거야?")
#                $ grouptalk.add("진일|별명으로 적자 ㅋㅋㅋ")
#                $ grouptalk.add("장중|아 에바야….")
#                $ grouptalk.add("삼용|일단 어떤 디자인으로 할지 예시부터 정해보자!")
#                $ grouptalk.add("장중|그러면 실제로 원단도 만져보고 업체랑 디자인 회의도 해야할 것 같은데? 내일 업체 가볼래??")
#                $ grouptalk.add("진일|아 무슨 귀찮게 그런걸 하냐.. 너무 멀다 ㅋㅋㅋ 언제 거기까지 가 ㅋ")
#                $ grouptalk.add("삼용|나는 찬성! 사진에서 예뻐보이는데 실제로는 별로일 수도 있어 ㅋㅋㅋㅋ")
#                $ grouptalk.add("진일|아니, 그럴 필요가 없다니까… 사진이랑 다르면 업체가 잘 안되지 ㅋㅋㅋ 여기 1위 업체라서 지금 주문도 밀렸다는데")
#                $ grouptalk.add("주인공|그러면 음…. 어떻게 해야되나  ")
#                $ grouptalk.add("주인공|그래도 빨리 만들어야하니까 내일 업체 방문할지 정할까?")

            elif day == 3 :
                $ grouptalk.add("날짜|3월 18일 수요일")
                $ grouptalk.add("주인공|애들아, 우리가 진짜 개멋있는 과잠 만들듯 ㅋㅋㅋ")
                $ grouptalk.add("금지|와 진짜 기대된다! 빨리 사고 싶다 ㅋㅋㅋ")
                $ grouptalk.add("대현|오오 예시 나옴?? 뭐있어 ㅋㅋㅋ")
                $ grouptalk.add("진일|야 내가 미는게 제일 멋있다 그걸로 하자 ㅋㅋㅋ")
                $ grouptalk.add("현재|개궁금하다 ㅋㅋㅋ ")
                $ grouptalk.add("주인공|기대해라 ㅋㅋㅋㅋ")

            elif day == 4 :
                $ grouptalk.add("날짜|3월 19일 목요일")
                $ grouptalk.add("주인공|우리가 과잠 후보 3개 만들었는데, 올릴게 애들아 ")
                $ grouptalk.add("대현|와 대박 진짜 빨리 올려줘 ㅋㅋㅋ")
                $ grouptalk.add("주인공|이미지 1(), 이미지 2(), 이미지 3()")
                $ grouptalk.add("장중|아무리 봐도 내게 제일 예쁘다 ㅋㅋㅋ 3번 투표해라 애들아")
                $ grouptalk.add("진일|멋하면 카모 아니냐 ㅋㅋㅋ 야상과잠 존멋이다 2번 투표해줘 ㅋㅋㅋ")
                $ grouptalk.add("삼용|누가봐도 1번이 제일 예쁘다 ㅋㅋㅋ")
                $ grouptalk.add("금지|어, 생각보다 별론데….?나 안사고 싶은데ㅠㅠ")
                $ grouptalk.add("주인공|애들아 최대한 빨리 투표 해주라!")
                $ grouptalk.add("미래|ㅇㅋㅇㅋ")

            elif day == 5 :
                $ grouptalk.add("날짜|3월 20일 금요일")

                $ grouptalk.add("날짜|투표 종료 시")
                $ grouptalk.add("금지|ㅠㅠ 나는 안 살래… 돈이 너무 없어 ㅠ")
                $ grouptalk.add("현재|음…. 그래도 고생했어 과준위 ㅎ")
                $ grouptalk.add("미래|맞아맞아 ㅠㅠㅠ")
                $ grouptalk.add("진일|야 진짜 어떻게 이러지 ㅋㅋㅋㅋㅋ")

                $ grouptalk.add("날짜|투표 연장 시")
                $ grouptalk.add("주인공|애들아 그래도 최대한 민주적으로 가려고 의견 수렴하니까 투표 빨리 해줘 ㅠㅠ 부탁할게!")
                $ grouptalk.add("진일|빨리빨리 하자.")
                $ grouptalk.add("장중|과잠위 고생했으니까 빨리 해주세요!!")
                $ grouptalk.add("삼용|하오하오!")
                $ grouptalk.add("미래|ㅋㅋㅋㅋ 근데 현재야 너 저거 잘 어울리겠는데?")
                $ grouptalk.add("현재|ㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add("대현|아 진짜 나가서 연애질해라 ㅋㅋㅋㅋㅋ")
                $ grouptalk.add("미래|근데 대현이 모쏠 실화냐??ㅋㅋㅋㅋ")
                $ grouptalk.add("대현|야 아니야 ㅋㅋㅋㅋ 나 연애해봤어 ㅋㅋㅋㅋ 어이가 없다")
                $ grouptalk.add("진일|ㅋㅋㅋㅋㅋ 니들이 사랑을 아냐?")
                $ grouptalk.add("장중|와 진일이 갬성 빼앰~~~")

            elif day == 6 :
                $ grouptalk.add("날짜|3월 21일 토요일")
                $ grouptalk.add("장중|술~ 이 한잔 생각 나~는 밤")
                $ grouptalk.add("현재|마치~ 있는 것 같아요~")
                $ grouptalk.add("대현|그~ 좋았던 시~절들")
                $ grouptalk.add("미래|이젠 모~두 한숨만 되네요~")
                $ grouptalk.add("진일|??? 다들 갑자기 왜이래… 장중이 술 땡기면 ㄱㄱ?")
                $ grouptalk.add("장중|이거 노래임 ㅋㅋㅋ")
                $ grouptalk.add("삼용|오 이거 무슨 노래야???")


        elif week == 4 :
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


    elif month == 4 :
        if week == 1 :
            if day == 0 :
                $ grouptalk.reset()
                $ grouptalk.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ grouptalk.add("날짜|3월 2일 월요일")
                $ grouptalk.add("장중|테스트")

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

        elif week == 4 :
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

    elif month == 5 :
        if week == 1 :
            if day == 0 :
                $ grouptalk.reset()
                $ grouptalk.add("날짜|5월 1일 일요일")
            if day == 1 :
                $ grouptalk.add("날짜|3월 2일 월요일")
                $ grouptalk.add("장중|테스트")

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

        elif week == 4 :
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

    elif month == 6 :
        if week == 1 :
            if day == 0 :
                $ grouptalk.reset()
                $ grouptalk.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ grouptalk.add("날짜|3월 2일 월요일")
                $ grouptalk.add("장중|테스트")

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

        elif week == 4 :
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
    return
