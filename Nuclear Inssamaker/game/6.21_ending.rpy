﻿# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label ending :
    play music "music/6.21_ending.mp3"

    "지난 3개월. 몸과 마음이 지쳐가며 열심히 살아온 당신. 괜찮았나요?"

    # 임의로 수치 부여함
    if study_parameter >= 50 :
        "[study_count]일동안 공부했는데 성적이 만족스럽습니다."
    else :
        "[study_count]일동안 공부했지만 성적이 생각보다 만족스럽지 않습니다."

    if club_parameter >= 50 :
        "동아리에서는 목이 터져라 [club_count]일간 노래했고\n동아리 사람들에게 인정받는 부원이 되었습니다."
    else :
        "동아리에서는 목이 터져라 [club_count]일간 노래했지만\n사람들에게 인정받지 못했습니다."

    "당신은 뻔대로써 과잠을 맞추고, 뻔엠을 기획했으며, 장터에서 아침부터 장을 보고 밤까지 일을 했으며, 친구들을 독려하며 운동회를 치러냈습니다."
    if gwa_parameter >= 50 :
        "그래서 동기들은 방학 때에도 바닷가로 엠티를 갈 것이라고 합니다."
    else :
        "하지만 당신이 뻔대 일을 잘 못했다는 말이 건너서 들려옵니다."

    if jangjung.parameter > 60 :
        "장중이와는 힘들때마다 술잔을 기울이는 사이가 되었고"
    else :
        "장중이와는 술 한잔 하지 않는 사이가 됐고"

    if jinil.parameter > 60 :
        "진일이와는 다음학기에도 수업을 같이 듣기로 하는 사이,"
    else :
        "진일이와는 마주치면 어색하게 인사하는 사이,"

    if samyong.parameter > 60 :
        "삼용이와는 방학때 중국여행을 같이 가기로 한 사이,"
    else :
        "삼용이와는 더 이상 갠톡하지 않는 사이,"

# 동아와는 다음학기부터 같이 자취하기로 한(♥ >3 ) /  더이상 속 얘기를 할 수 없는 사이가 됐습니다.(♥<=3)

    "고생했습니다. 분명 아쉽고 왜 이렇게 잘 하지 못했을까 자신을 탓할지도 모릅니다."
    "하지만, 누구에게나 처음은 어렵지요. 그 어려움을 이겨내고 지금에 이른 당신."
    "진심을 담아 너무나 수고하셨습니다. 다음에 겪게 될 처음들도 잘 이겨낼거에요."
    "행운을 빕니다. 당신도, 나도."

    stop music fadeout 1.0
    return
