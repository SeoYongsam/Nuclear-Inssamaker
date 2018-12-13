image friend_2 = "fun_mt/friend_2.jpg"
image friend_3 = "fun_mt/friend_3.jpg"
image friend_4 = "fun_mt/friend_4.jpg"
image friend_5 = "fun_mt/friend_5.jpg"

label friend_2:
    "삼용이와 술을 마시기로 결정했다."

    show friend_2 at truecenter
    "삼용이와 얘기를 하며 소주 1병 정도를 더 비웠다."
    "삼용이와의 관계가 좋아진 것 같다."

    #삼용이와 파라미터 +
    $ samyong.parameter += 20
    return

label friend_3:
    "장중이와 술을 마시기로 결정했다."

    show friend_3 at truecenter
    "장중이와 이야기를 하며 소주 1병 정도를 더 비웠다."
    "장중이와의 관계가 좋아진 것 같다."

    #장중이와 파라미터 +
    $ jangjung.parameter += 20
    return

label friend_4:
    "진일이를 찾으러 나가기로 결정했다."
    "다행히 진일이는 숙소 바로 앞에 있었다."

    show friend_4 at truecenter
    "진일이와 말을 주고 받으면서 소주 1병 정도를 더 비웠다."
    "진일이와의 관계가 좋아진 것 같다."

    #진일이와 파라미터 +
    $ jinil.parameter += 20
    return

label friend_5:
    "장중, 진일, 용삼의 술자리에 합류하기로 결정했다."
    "...뭔가 땅이 흔들리는 것 같다."

    show friend_5 at truecenter
    scene black
    "친구들과 얘기를 하다가 토를 한 것 같다. \n애들이 내 몸을 씻겨주는 것 같다..."
    "분위기가 싸해진 것을 느끼면서 정신을 잃었다."

    #과 파라미터 감소
    $ gwa_parameter -= 10
    call parameter_maxmin_check

    $rest_point -= 1
    return
