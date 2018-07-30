import pickle
import numpy as np
import grpc
from sklearn import preprocessing
import ner_pb2
import ner_pb2_grpc

class SVM_Classifier(object):
    def __init__(self, music_model_name, genre_model_name, music_vocab_file, genre_vocab_file):
        self.svm = pickle.load(open(music_model_name, 'rb'))
        self.svm_genre = pickle.load(open(genre_model_name, 'rb'))
        self.genre_map = {0: 'antiquity', 1: 'sport', 2: 'miss'}

        self.vocab = {}
        with open(music_vocab_file, 'r', encoding='utf-8-sig') as reader:
            cnt = 0
            for line in reader:
                char = line.strip()
                self.vocab[char] = cnt
                cnt += 1

        self.genre_vocab = {}
        with open(genre_vocab_file, 'r', encoding='utf-8-sig') as reader:
            cnt = 0
            for line in reader:
                char = line.strip()
                self.genre_vocab[char] = cnt
                cnt += 1

        self.channel = grpc.insecure_channel('localhost:50052')
        self.stub = ner_pb2_grpc.NerStub(self.channel)

    def sentence2vector(self, sentence, music_flag):
        if music_flag:
            n = len(self.vocab)
            vector = [0] * n
            for char in sentence:
                if char in self.vocab:
                    vector[self.vocab[char]] += 1
            return [np.asarray(vector)]
        else:
            n = len(self.genre_vocab)
            vector = [0] * n
            for char in sentence:
                if char in self.genre_vocab:
                    vector[self.genre_vocab[char]] += 1
            return [np.asarray(vector)]


    def music_predict(self, sentence):
        sentence.encode('utf-8')
        vector = self.sentence2vector(sentence, True)
        vector = preprocessing.scale(vector)
        pred = self.svm.predict(vector)

        if pred[0] == 0:
            response = self.stub.process(ner_pb2.NerRequest(sentence=sentence))
            for entity in response.entities:
                print(entity.entity_value)
                if entity.entity_type == 'MUSIC':
                    pred[0] = 1
        # if pred[0]:
        if pred[0]:
            return 'music',entity.entity_value

        else:
            return 'non_music',''


    def genre_predict(self, sentence):
        sentence.encode('utf-8')
        vector = self.sentence2vector(sentence, False)
        vector = preprocessing.scale(vector)
        pred = self.svm_genre.predict(vector)
        genre = self.genre_map[pred[0]]
        return genre


def lyric(lyric):
    music_model_name = 'Music_Classifier.sav'
    genre_model_name = 'Lyric_Classifier.sav'
    music_vocab_file = 'music-vocab.txt'
    genre_vocab_file = 'vocab.txt'
    svm = SVM_Classifier(music_model_name=music_model_name,
                         genre_model_name=genre_model_name,
                         music_vocab_file=music_vocab_file,
                         genre_vocab_file=genre_vocab_file)


    # print('语句： ' + sentence)
    # print('歌词： ' + lyric)
    # print('语句判断： ' + svm.music_predict(sentence))
    # print('曲风判断： ' + svm.genre_predict(lyric))

    lyric_rec = svm.genre_predict(lyric)
    return lyric_rec

def sentence(sentence):
    music_model_name = 'Music_Classifier.sav'
    genre_model_name = 'Lyric_Classifier.sav'
    music_vocab_file = 'music-vocab.txt'
    genre_vocab_file = 'vocab.txt'
    svm = SVM_Classifier(music_model_name=music_model_name,
                         genre_model_name=genre_model_name,
                         music_vocab_file=music_vocab_file,
                         genre_vocab_file=genre_vocab_file)

    # print('语句： ' + sentence)
    # print('歌词： ' + lyric)
    # print('语句判断： ' + svm.music_predict(sentence))
    # print('曲风判断： ' + svm.genre_predict(lyric))

    sentence_rec= svm.music_predict(sentence)
    return sentence_rec


# if __name__ == '__main__':
    # main()

