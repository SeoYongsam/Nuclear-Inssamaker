#이미지 선언
image dance = "dongsoze/dance.jpg"
image donga = "dongsoze/donga.jpg"
image perfo = "dongsoze/perfo.jpg"
# image dongsoze = "dongsoze/dongsoze.jpg"

# 3월 9일 닞 동소제 이벤트
# month3 week2 day 1
label dongsoze:
    scene black
    "오늘은 동아리 소개제가 있는 날이다.\n"
    extend "공강 시간을 이용해 동아리 소개제 구경을 가게 되었다."

    scene black
    "동소제를 둘러보던 중 앞쪽에 사람들이 모여 있는 모습을 발견하고 그 쪽으로 가보기로 했다."

    show donga at truecenter
    Player "어 동아다! 하이하이!"
    Dongah "오 뻔대 친구 아이가?\n"
    extend "바쁜 친구가 그래도 오긴 왔네?"
    Player "그래도 약속했는데 당연히 와야지!\n"
    extend "근데 니가 왜 여기서 기타치고 있냐?"
    Dongah "음? 그냥 이리저리 둘러보다가 여가 제일 분위기 좋아보여서\n"
    extend "저 짝에 있는 선배랑 얘기하다보니까 자연스럽게? 일케 됐다"
    Player "맞나? 그래도 분위기 꽤 좋나보네?"
    Dongah "엉, 선배들끼리도 되게 화목해보이고 실력도 다들 출중하셔가지고 괜찮드라"
    Dongah "어? 근데 뒤에는 친구들이가?\n"
    extend "그럼 친구들도 있는데 노래 한 곡 해줘야지 않겠나?"

    scene black
    "분위기에 휩쓸려 노래를 불렀다! 사람들의 시선이 느껴진다!"

    "노래가 끝난 후"

    show perfo at truecenter

    "와아아아아아! 최고다~"

    "동아리 선배" "와 새내기 노래 진짜 잘 부르시네요\n"
    extend "혹시 밴드에 관심있어요?"
    "동아리 선배" "새내기 정도면 저희쪽에서 스카웃 하고 싶은데\n"
    extend "혹시 저희 동아리 들어와 주실 수 있나요??"
    Player "아..네 뭐...친구도 있고 하니까 된다면 들어갈게요"
    "동아리 선배" "와!! 잘 선택하셨어요!!\n"
    extend "당장 이번주 목요일이 이번 학기 첫 정기 연습이니까 꼭 와주세요~!"
    Player "아 네넵!\n"
    extend "그럼 그 날 뵙겠습니다!"

    scene black

    "'동아리' 선택지가 추가되었습니다. 일정 계획에서 동아리를 선택할 수 있게 되었습니다."
    "3/12(목) 저녁 일정이 동아리 정기 연습으로 교체되었습니다."
    $ day_schedule[0][12] = 2

    return
