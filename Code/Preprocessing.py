def cleanText(text):
    ignoreList = ["@", "#", "$", "%", "^", "&", "*", "_", "+", "/", "=", ",", "×", "٪", "(", ")", "[", "]", "{",
                  "}", "\xa0"]
    for char in ignoreList:
        text = text.replace(char, "")
    text = text.replace("\n", ".").replace(":", ".").replace(";", ".").replace("?", ".").replace("!", ".").replace("؟",".")
    return text


def filterLen(text):
    newText = []
    for sentence in text:
        if len(sentence) > 1:
            newText.append(sentence)
    return newText


def Lowercase(text):
    return text.lower()


def Stemming(text):
    from stemming.porter2 import stem
    return stem(text)


def devideToSentence(text):
    #print("\tCleaning...")
    text = cleanText(text)  # Clean
    #print("\Lowering...")
    text = Lowercase(text)  # Lower
    #print("\stemming...")
    text = Stemming(text)  # stemming
    #print("\tSpliting Sentence...")
    text = text.split(".")
    #print("\tFiltering...")
    text = filterLen(text)  # filter
    return text



def StopWordsDelete(TextList):
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []
    for w in TextList:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


def tokenization(text):
    text = devideToSentence(text)
    #print("\tTokenization and StopWord delete...")
    for i in range(text.__len__()):
        text[i] = text[i].replace("  ", " ")
        text[i] = text[i].split(" ")
        n = text[i].__len__();
        j = 0
        while j < n:
            if text[i][j] == '':
                del (text[i][j])
                j -= 1
                n = n - 1
            j += 1
        text[i] = StopWordsDelete(text[i])
    return text


def Preprocessing(text):
    return tokenization(text)



