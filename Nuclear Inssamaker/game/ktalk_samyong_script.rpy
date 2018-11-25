# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_samyong_talk :
    if month == 3 :
        if week == 1 :
            if day == 1 :
                $ samyong.add("날짜|3월 2일 월요일")
                $ samyong.add("장중|테스트")
                $ samyong.add("연속|잘 되려나\n되겠지")
                $ samyong.add("진일|안녕")
                $ samyong.add("삼용|즐거운 하루가 되길")
                $ samyong.add("동아|으아악\n테스트")
                $ samyong.add("연속|잘 되려나\n되겠지")
                $ samyong.add("미래|난 현재 여친\nㅋㅋ")
                $ samyong.add("주인공|이것도 테스트")

            elif day == 2 :
                $ samyong.add("날짜|3월 3일 화요일")
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("날짜|3월 4일 수요일")
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("진일|테스트")

            elif day == 5 :
                $ samyong.add("미래|테스트")

            elif day == 6 :
                $ samyong.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("삼용|우리 과잠 잘 나오겠지ㅋㅋㅋ?? 내거 됐으면 좋겠다")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ samyong.add("삼용|이거 애들이 좋아할까?? 난 진짜 모르겠어 ㅋㅋㅋ 내가 투표 안한 애들 물어봤는데 지금 별로라서 투표 안하는거라던데")

            elif day == 1 :
                # 투표 종료
                $ samyong.add("삼용|뻔대야 우리끼리 조만간 같이 놀러 가자 ㅋㅋㅋ")

                # 투표 진행
                $ samyong.add("삼용|투표 안한 애들이 이거 별로라고 생각한다는데 어떡하지 하…. 다시 만들어야하나?")
            elif day == 2 :
                # 투표 종료
                $ samyong.add("삼용|내일 점모 중식 너무 좋다 ㅋㅋㅋ 나 배려해줘서 고마워")

                # 투표 진행
                $ samyong.add("삼용|금지는 갠톡왔는데 돈이 없어서 못살 것 같대… 33개만 주문하자")
            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")


    elif month == 4 :
        if week == 1 :
            if day == 0 :
                $ samyong.reset()
                $ samyong.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ samyong.add("날짜|3월 2일 월요일")
                $ samyong.add("장중|테스트")

            elif day == 2 :
                $ samyong.add("날짜|3월 3일 화요일")
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("날짜|3월 4일 수요일")
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("진일|테스트")

            elif day == 5 :
                $ samyong.add("미래|테스트")

            elif day == 6 :
                $ samyong.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

    elif month == 5 :
        if week == 1 :
            if day == 0 :
                $ samyong.reset()
                $ samyong.add("날짜|5월 1일 일요일")
            if day == 1 :
                $ samyong.add("날짜|3월 2일 월요일")
                $ samyong.add("장중|테스트")

            elif day == 2 :
                $ samyong.add("날짜|3월 3일 화요일")
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("날짜|3월 4일 수요일")
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("진일|테스트")

            elif day == 5 :
                $ samyong.add("미래|테스트")

            elif day == 6 :
                $ samyong.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

    elif month == 6 :
        if week == 1 :
            if day == 0 :
                $ samyong.reset()
                $ samyong.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ samyong.add("날짜|3월 2일 월요일")
                $ samyong.add("장중|테스트")

            elif day == 2 :
                $ samyong.add("날짜|3월 3일 화요일")
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("날짜|3월 4일 수요일")
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("진일|테스트")

            elif day == 5 :
                $ samyong.add("미래|테스트")

            elif day == 6 :
                $ samyong.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ samyong.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ samyong.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ samyong.add("삼용|테스트")

            elif day == 3 :
                $ samyong.add("장중|테스트")

            elif day == 4 :
                $ samyong.add("장중|테스트")

            elif day == 5 :
                $ samyong.add("장중|테스트")

            elif day == 6 :
                $ samyong.add("삼용|뻔엠 전에 과잠 안오면 어떡하지…?")
    return
