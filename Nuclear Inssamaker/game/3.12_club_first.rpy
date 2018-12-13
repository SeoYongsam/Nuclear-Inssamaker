#이미지 선언
image studentcenter = "club_first/studentcenter.jpg"
image prac = "club_first/1.png"
image clubroom = "club_first/clubroom.jpg"

# 3월 12일 저녁 동아리 첫 연습
# month1 week2 day4
label club_first :
    scene black
    "오늘은 동아리 첫 연습이 있는 날이다. 수업을 마친 동아와 만나 동아리 연습실로 찾아가게 되었다."

    show studentcenter at truecenter
    Dongah "와 이렇게 같이 연습 가는 거 중학생때 생각난다. 안 글나?"
    Player "그니까 그 때도 이렇게 같이 갔었는데"
    Dongah "그래도 우리 진짜 징하게 같이 다녔네 ㅋㅋㅋㅋ"
    Player "ㅋㅋㅋ 내말잌ㅋㅋㅋ"
    Dongah "뭐 여튼 들어가보자"

    show clubroom at truecenter
    "동아와 동아리 연습실에 들어갔다. 먼저 와 있는 선배들이 악기를 만지고 있는 모습이 보였다."

    "동아리 선배 1" "오~ 새내기들 오셨네요!! 반가워요!"
    "동아리 선배 2" "와 동소제 때 멋진 공연 보여준 친구들이네요!!"
    Player "안녕하세요! 문정과 19학번 주인공입니다! 잘 부탁드려요!"
    Dongah "안녕하세요! 소비자아동학과 19학번 이동아입니다! 잘부탁드립니다!"
    "동아리 선배들" "와아~!"
    "동아리 선배 1" "음 그럼 급작스럽긴 하지만, 온 김에 천천히 합주해볼까요??"
    Player "앗 넵 좋아요!"
    "동아리 선배 2" "무슨 노래로 해볼까요?? 혹시 제일 잘 부르는 노래 있나요?"
    Player "음…그럼 쏜애플의…"

    show prac at truecenter
    "동아리원들과 즐겁게 합주를 하였다!"

    scene black

    return
