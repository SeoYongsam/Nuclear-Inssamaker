# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# 캐릭터 일람 : 장중, 삼용, 현재, 동아, 진일, 미래, 주인, 0
# 양식 $ messages.extend([["캐릭터이름", "멘트"]])
# 줄바꿈은 \n로 실시한다
# 캐릭터이름이 0일 경우에(이 경우엔 큰따옴표 없음), 단타로 여러번 톡을 보낸 효과가 난다.


# 메시지 전부 삭제하는 기능. 그냥 연장하려면 빼고 작성
# $ del messages[:]
label change_ktalk_talk :
    if month == 3 :
        if week == 1 :
            if day == 0 :
                $ messages.extend([[0, "더미"]])

            elif day == 1 :
                $ messages.extend([["장중", "테스트"]])
                $ messages.extend([["진일", "안녕"]])
                $ messages.extend([["삼용", "즐거운 하루가 되길"]])
                $ messages.extend([["동아", "으아악\n테스트"]])
                $ messages.extend([[0, "잘 되려나\n되겠지"]])
                $ messages.extend([["미래", "난 현재 여친\nㅋㅋ"]])
                $ messages.extend([["주인공", "이것도 테스트"]])

            elif day == 2 :
                $ messages.extend([["삼용", "테스트"]])

            elif day == 3 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 4 :
                $ messages.extend([["진일", "테스트"]])

            elif day == 5 :
                $ messages.extend([["미래", "테스트"]])

            elif day == 6 :
                $ messages.extend([["주인공", "테스트"]])

        elif week == 2 :
            if day == 0 :
                $ messages.extend([["장중", "이건 실행이 됨"]])

            elif day == 1 :
                $ messages.extend([["장중", "캐릭터이름과 메시지를 변경하세요"]])

            elif day == 2 :
                $ messages.extend([["삼용", "테스트"]])

            elif day == 3 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 4 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 5 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 6 :
                $ messages.extend([["장중", "테스트"]])

        elif week == 3 :
            if day == 0 :
                $ messages.extend([["장중", "이건 실행이 됨"]])

            elif day == 1 :
                $ messages.extend([["장중", "캐릭터이름과 메시지를 변경하세요"]])

            elif day == 2 :
                $ messages.extend([["삼용", "테스트"]])

            elif day == 3 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 4 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 5 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 6 :
                $ messages.extend([["장중", "테스트"]])

        elif week == 4 :
            if day == 0 :
                $ messages.extend([["장중", "이건 실행이 됨"]])

            elif day == 1 :
                $ messages.extend([["장중", "캐릭터이름과 메시지를 변경하세요"]])

            elif day == 2 :
                $ messages.extend([["삼용", "테스트"]])

            elif day == 3 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 4 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 5 :
                $ messages.extend([["장중", "테스트"]])

            elif day == 6 :
                $ messages.extend([["장중", "테스트"]])
    return
