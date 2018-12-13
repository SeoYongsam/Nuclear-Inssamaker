# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_jinil_talk :
    if month == 3 :
        if week == 1 :
            if day == 1 :
                $ jinil.add("날짜|3월 2일 월요일")
                $ jinil.add("장중|테스트")
                $ jinil.add("연속|잘 되려나\n되겠지")
                $ jinil.add("진일|안녕")
                $ jinil.add("삼용|즐거운 하루가 되길")
                $ jinil.add("동아|으아악\n테스트")
                $ jinil.add("연속|잘 되려나\n되겠지")
                $ jinil.add("미래|난 현재 여친\nㅋㅋ")
                $ jinil.add("주인공|이것도 테스트")

            elif day == 2 :
                $ jinil.add("날짜|3월 3일 화요일")
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("날짜|3월 4일 수요일")
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("진일|테스트")

            elif day == 5 :
                $ jinil.add("미래|테스트")

            elif day == 6 :
                $ jinil.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("진일|뻔대야 카모 진짜 멋있지 않냐 ㅋㅋㅋ 이걸로 가자")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                # 투표 진행
                $ jinil.add("진일| ㅋㅋㅋㅋㅋ 내가 애들이 이거 좋아할거라고 했지? 아.. 근데 혹시 내가 단톡방에서 좀 오버했나??	")

                # 강제 종료
                $ jinil.add("진일|과잠 예쁜 것 같아 빨리 입고 싶다ㅋㅋㅋㅋ")

            elif day == 1 :
                # 강제 종료
                $ jinil.add("진일|우리 과잠은 언제오지???")

                # 투표 지속
                $ jinil.add("진일|내가 애들한테 갠톡 돌려볼게!")

            elif day == 2 :
                #투표 지속
                $ jinil.add("진일|아 진짜 애들 너무한 것 같아 하….")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")


    elif month == 4 :
        if week == 1 :
            if day == 0 :
                $ jinil.reset()
                $ jinil.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ jinil.add("날짜|3월 2일 월요일")
                $ jinil.add("장중|테스트")

            elif day == 2 :
                $ jinil.add("날짜|3월 3일 화요일")
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("날짜|3월 4일 수요일")
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("진일|테스트")

            elif day == 5 :
                $ jinil.add("미래|테스트")

            elif day == 6 :
                $ jinil.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

    elif month == 5 :
        if week == 1 :
            if day == 0 :
                $ jinil.reset()
                $ jinil.add("날짜|5월 1일 일요일")
            if day == 1 :
                $ jinil.add("날짜|3월 2일 월요일")
                $ jinil.add("장중|테스트")

            elif day == 2 :
                $ jinil.add("날짜|3월 3일 화요일")
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("날짜|3월 4일 수요일")
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("진일|테스트")

            elif day == 5 :
                $ jinil.add("미래|테스트")

            elif day == 6 :
                $ jinil.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

    elif month == 6 :
        if week == 1 :
            if day == 0 :
                $ jinil.reset()
                $ jinil.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ jinil.add("날짜|3월 2일 월요일")
                $ jinil.add("장중|테스트")

            elif day == 2 :
                $ jinil.add("날짜|3월 3일 화요일")
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("날짜|3월 4일 수요일")
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("진일|테스트")

            elif day == 5 :
                $ jinil.add("미래|테스트")

            elif day == 6 :
                $ jinil.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ jinil.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jinil.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jinil.add("삼용|테스트")

            elif day == 3 :
                $ jinil.add("장중|테스트")

            elif day == 4 :
                $ jinil.add("장중|테스트")

            elif day == 5 :
                $ jinil.add("장중|테스트")

            elif day == 6 :
                $ jinil.add("장중|테스트")
    return
