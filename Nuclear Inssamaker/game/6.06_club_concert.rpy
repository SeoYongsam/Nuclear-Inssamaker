# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#6월 6일
## month 6 week 1 day 5
label club_concert :
    "오늘은 동아리 공연 날이다."
    "동아리 활동을 하면서 연습을 했지만 그래도 조금씩 긴장된다."
    "과 친구들도 공연을 보러 온다고 하니 실수하지 않고 공연을 잘 끝내고 싶은 생각 밖에 안든다."
    "엇 이제 공연 시작한다..!"


    #공연 성공적
    if club_parameter >= 50 :
        python :
            mental_point += 30
            club_parameter += 5

        "드디어 공연이 끝났다."
        "한 학기동안 동아리 연습을 많이 했어서 그런지 실수 안하고 공연을 성공적으로 끝마쳤다."
        Dongah "와 니 장난 아니데"
        Dongah "니 연습 얼마나 했길래 고음도 그렇게 깔끔하게 올라가는데 ㅋㅋㅋ"
        Player "그만해라 부끄럽다 ㅋㅋ 니도 기타 솔로 장난 아니더만"
        Dongah "아무튼 오늘 공연정리 끝나고 밴드 애들이 시간되면 놀자는데 얼른 과 친구들 만나고 가능하면 온나"
        Player "알겠다 ㅋㅋ"

    #공연 실패
    else :
        $ mental_point -= 50

        "드디어 공연이 끝났다."
        "한 학기동안 동아리 연습을 많이 안해서 공연때 실수를 계속해서 했다. 오늘 공연은 성공적이지 못했다."
        Dongah "수고했다 ㅋㅋ"
        Player "미안… 니랑 동아리원들 다 열심히 준비했는데 내가 실수 많이 해서 공연 망친 것 같네..."
        Dongah "그냥 연습 조금만 더 하지… "
        Player "..."
        Dongah "아무튼 저기 니 친구들 기다리고 있는 것 같은데 얼른 가서 놀아라 ㅋㅋ"
        Player "그래 들어가라"


#동아리 공연에 사람이 많이 옴
    if club_parameter <= gwa_parameter:
        "동아리 공연이 끝나고 친구들이 있다는 곳으로 갔다"
        "생각보다 친구들이 많이 와줘서 엄청 뿌듯했다"

        Player "와 너네들 안 올것 처럼 하더니 많이 왔네?"
        Samyong "온다 했잖아~"
        Jinil "뻔대가 공연한다는데 안갈리가 있나"
        Daehyun "우리가 안오면 누가 오냐!"
        Ohduck "후훗"
        Jangjung "진짜 수고했다 뻔대야 ㅋㅋㅋ 동아리 공연도 이제 끝이니까 우리랑도 놀아줘라~"
        Jinil "그런 의미에서 오늘 술 ㄱ?"
        Daehyun "여기 온 사람들 다 오늘은 진짜 술 마시러 가야된다"
        Jangjung "진심"
        Samyong "오늘은 도수 높은걸로? 고량주로 달릴까?!"
        Ohduck "이쿠욧!"

        "애들이 많이 공연보러 와서 감동이었다. 내가 그래도 과생활은 열심히 했다는 생각이 들었다."

        python :
            mental_point += 20
            gwa_parameter += 4

    #동아리 공연에 사람이 거의 안옴
    else :
        "동아리 공연이 끝나고 친구들이 있다는 곳으로 갔다"
        "친구들이 온다는 말은 들었지만 어디 있는지 잘 못 찾아서 헤맸다"

        Samyong "뻔대야 여기!"
        Player "오!! 삼용이 왔구나!! 다른 애들은?"
        Samyong "장중이랑 진일이는 보다가 중간에 갔고 다른 애들은 바쁘다고 못왔어…"
        Player "아… 그래도 너라도 와줘서 고마워 삼용아"
        Samyong "그래 ㅋㅋㅋ 이제 동아리 공연도 끝났으니깐 동아리 말고 과에도 조금 더 신경써줘"

        "심용이 말고는 아무도 공연을 끝까지 보러 오지 않아서 슬펐다. 과생활을 열심히 한다고 했지만 충분하지 않았나보다. 오늘은 조금 외롭다."

        $ mental_point -= 30

    #동아리 파라미터 일정 이하면 동아리 활동 사라짐
    if club_parameter < 50 :
        "내가 공연을 망친 것 같아서 더 이상 동아리에 나가기가 부끄럽다. 당분간 동아리에는 못 갈 것 같다."
        $ club_open = False
