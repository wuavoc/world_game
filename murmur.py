import sys
import random

file = open("word_rus1.txt", "r")
wordlist = file.readlines()
file.close

UsedWords = []
LastLiteralBot = ""
WhoStartsRandom = random.randrange(0, 2)
def StartBot():
    BotWord = wordlist[random.randrange(0, len(wordlist))]
    print(BotWord)
    if (BotWord[-2] == 'ь'):
            LastLiteralBot = BotWord[-3]
    else:
            LastLiteralBot = BotWord[-2]
    UsedWords.append(BotWord)
    
while True:
    if (WhoStartsRandom == 1):
        StartBot()
        WhoStartsRandom = "none"
    if (WhoStartsRandom == 0):
        print("Введите слово")
        WhoStatsRandom = "none"
    MyWord = input()
    if (MyWord == " "):
        print("Пожалуйста, введите слово.")
        continue
    if(MyWord[0] != LastLiteralBot and LastLiteralBot != ""):
        print("Слово должно начинаться на букву", LastLiteralBot)
        continue
    if (MyWord[-1] == 'ь'):
        MyLastLiteral = MyWord[-2]
    else:
        MyLastLiteral = MyWord[-1]
    if ((MyWord.isalpha()) == False):
        print("В строке присутствует что-то кроме букв, повторите ввод.")
        continue
    #if ((MyWord+'\n' in wordlist) == False):
        #print("Слово отсутствует в словаре. Это точно существительное?")
    if ((MyWord in UsedWords) == True):
        print("Ты проиграл! Слово уже использовалось.")
        sys.exit()

    StartOfRange = 0
    EndOfRange = -1
    for WordNumber, ListWorld in enumerate(wordlist):
        if (ListWorld[0] == MyLastLiteral):
            if (StartOfRange == 0):
                StartOfRange = WordNumber
            EndOfRange = WordNumber
    if (EndOfRange == -1):
        print("Слов не найдено. Ты выиграл!")
        sys.exit()  
    BotWord = wordlist[random.randrange(StartOfRange, EndOfRange+1)]
    print (BotWord)  
    if (BotWord[-2] == 'ь'):
        LastLiteralBot = BotWord[-3]
    else:
        LastLiteralBot = BotWord[-2]
    UsedWords.append(MyWord)
    UsedWords.append(BotWord)
