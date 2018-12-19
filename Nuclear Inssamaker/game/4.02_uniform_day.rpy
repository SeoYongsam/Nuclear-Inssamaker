#이미지 선언
image gyobok = "uniform_day/gyobok.jpg"
image jjangge = "uniform_day/jjangge.jpg"
image pizza = "uniform_day/pizza.jpg"

# 4월 2일 월요일 교복데이 이벤트
# month4 week1 day 1
label uniform_day:
    "어제는 만우절이었다. 그런데 일요일이었어서 오늘 과 동기들이 다같이 교복을 입고 등교를 했다."
    "과 동기들이 만우절 기념으로 점심식사를 함께 야외에서 배달음식을 먹자고 한다."
    "하지만 약속한 시간에 수업이 있다. 어떻게 할까?"

    menu:
        "수업을 째고 동기들과 점심을 먹으러 간다":
            #hp & 공부 파라미터-, 과 파라미터 up, 개별 캐릭터와 파라미터는 변함이 없고 과 친밀도가 올라감
            $ hp -= 20
            $ study_parameter -= 1
            $ gwa_parameter += 3
            call parameter_maxmin_check

            "수업을 째고 동기들이랑 점심을 먹으러 캠퍼스 안에 있는 잔디밭에 갔다."
            show gyobok at truecenter

            Hyunjae "얘들아 오늘 점심으로 뭐먹을까??"
            Daehyun "야외에서 시켜먹을 때는 중식이지!"
            Jinil "야 무슨소리야 밖에 나왔으면 들고 다니면서 먹을 수 있는 피자 먹어야지"
            Jangjung "아... 난 짬뽕 먹을래... "

            "친구들이 점심 메뉴를 두고 의견이 갈리고 있다."

            Jinil "야 뻔대! 넌 뭐먹을래? 그냥 너가 결정해라."


            menu:
                "(장중이와 삼용이가 좋아하는)짜장면, 짬뽕":
                    #장중이 + 삼용 파라미터 +
                    $ jangjung.parameter += 20
                    $ samyong.parameter += 20

                    show jjangge at truecenter
                    "중국집에서 음식을 시켰다."
                    "장중이는 어제 술을 마셨는지 짬뽕으로 해장을 하는 것 같다."
                    "삼용이도 오랜만에 중국 음식(?)을 먹어서 그런지 기분이 좋은것 같다."

                "(진일이가 좋아하는)피자":
                    #진일이 파라미터 ++
                    $ jinil.parameter += 40

                    show pizza at truecenter
                    "피자를 시켰다."
                    "진일이는 앞으로 착하게 살기로 한다며 피자를 종류별로 2개씩만 먹는다고 한다."

        "수업을 듣는다":
            return

    return
