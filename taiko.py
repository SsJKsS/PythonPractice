beat = input()  # 設定節拍變數(beat)
beatList = list(beat)  # 設定節拍列表儲存(beat) list()將字串轉成列表形式，字元個別存入list
playerBeat = input()  # 設定玩家節拍變數(playerBeat)
playerBeatList = list(playerBeat)  # 設定玩家節拍列表儲存(playerBeat)
combo = 0  # 設定combo變數(combo)
tempCombo = 0  # 設定暫存combo變數(tempCombo)
highestCombo = 0  # 設定最高combo變數(highestCombo)
point = 0  # 設定分數變數(point)

for i in range(len(beatList)):  # 設定迴圈跑的範圍為節拍列表的長度 len()計算字串、列表長度 range()計算該長度範圍
    if beatList[i] =='-':  # 如果當下判斷的節拍是'-'就跳過
        pass  # pass為不做任何事，常用於if判斷式(因為if內一定要塞東西)
    elif beatList[i] == playerBeatList[i]:  # 如果當下判斷的節拍和玩家節拍一樣
        combo += 1  # combo + 1 (也可寫成combo = combo + 1)
        point += combo * 100  # 分數計算方式為 當下combo乘上100 (也可寫成point = point + combo * 100)
    else :  # 如果都不是上述兩個情形，也就是當下判斷的節拍和玩家節拍不一樣
        tempCombo = combo  # 先將當下combo數存到暫存combo，方便日後比較最高連擊數(highestCombo)
        combo = 0  # 因為節拍不同，所以連擊歸0重新計算
    highestCombo = max(tempCombo, combo)  # 比較出最高連擊數 max(a,b)比較a和b哪個數字較大並回傳大的數字

print(point,highestCombo)  # 印出總分和最高連擊數





