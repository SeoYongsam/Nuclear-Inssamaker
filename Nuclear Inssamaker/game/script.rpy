# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image room = "room.png"
image phone = "phone.png"
image planner = "planner.png"

# 게임에서 사용할 캐릭터를 정의합니다.
#define e = Character('아이린', color="#c8ffc8")
define s = Character('시스템', color="#c8ffc8")

# jump 문과 call 문 :
# label 로 대사 뭉치에 정해준 이름을 jump 에 사용하면 해당 레이블로 건너뛰게 됩니다.
# call 도 비슷한 기능을 하지만 다른 점이 있다면 jump 는 흐름이 아예 넘어가는 반면,
# call 은 해당 label 블록을 다 진행한 후 return 문을 만나면
# call 문이 적힌 다음 문장으로 다시 돌아간다는 것입니다.

# 여기에서부터 게임이 시작합니다.
label start:
    scene room at truecenter
    show phone at topleft
    show planner at topright

    s "Hi"
    "용삼""으악"
    s "새로운 렌파이 게임을 만들었군요."

    menu :
        "선택지1":
            "음핫핫"
            call 테스트

        "선택지2":
            "핫음음"
            call 테스트

#    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    return

label 테스트:
    "히히히"

    return
