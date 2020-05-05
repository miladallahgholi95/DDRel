
import Preprocessing as P
from gensim.models.word2vec import Word2Vec
import time



numbersFile= 13

for i in range (1,numbersFile+1):
    print("====================== File "+str(i)+" ======================")

    Input = []
    print("1. Reading and Preprocessing ...")
    with open("output" + str(i) + ".txt", encoding="utf-8") as file:
        for line in file:
            Input += P.Preprocessing(line)

    print("2. Learning ...")
    if i == 1:
        model.build_vocab(Input)
        model.train(Input, total_words=model.corpus_total_words, epochs=model.epochs)
    else:
        model.build_vocab(Input, update=True)
        model.train(Input, total_words=model.corpus_total_words,epochs=model.epochs)

    file.close()
    del Input
    print("3. Sleeping ...")
    time.sleep(20)


print("====================== Save ======================")
model.save("model.bin")
