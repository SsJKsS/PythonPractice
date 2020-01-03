tempSentence = []  # 宣告暫存句子列表(tempSentence)
words = ''  # 宣告空字串變數(words)

while 1:  # 無窮迴圈，直到break的出現才會停
    words = input().split()  # 輸入單字和單字順序 split()切割字串　讓words可以因為切割吃到兩個輸入 words轉為列表型態
    if words[0] == '0':  # 如果words的第一筆資料是0
        sentence = " ".join(tempSentence)  # 宣告句子列表(sentence) 並使用join()將列表轉為字串
        print(sentence + ".")  # 印出完整句子，句末須加"."
        break  # 因為偵測到0，所以跳出無窮迴圈
    else:
        tempSentence.insert(int(words[1]) - 1, words[0])  # 未偵測到0，所以可以持續輸入
        #  依照給的單字順序插入單字進暫存句子列表
        #  int(words[1]) - 1 須轉為數字型態 否則是字串型態 會無法使用insert()
        #  insert(a,b)可指定在列表的a位置插入b字串




