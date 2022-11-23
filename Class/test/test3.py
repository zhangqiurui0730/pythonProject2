while True:
    try:
        s = input().split(' ') #先把句子切分成单词列表
        len_s = len(s)
        for i in range(len_s): #从反方向分别打印列表里的单词
            print(s[len_s-1-i], end = ' ')
        print('')
    except:
        break