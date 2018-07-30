import re
import ner_regex.config as config
from data_utils import DataUtils
from entity import Entity


class RegexNer:

    def __init__(self):
        self.default_rule_score = 1.0
        self.data_utils = DataUtils()
        self.init_common()


    def init_common(self):
        """
        predict labels, the operation of transfer words to id token is processed by tensorflow tensor.
        input words list, now, only support one element list.
        :return:
        """
        self.common_vocab = dict()
        with open(config.common_vocab_path, encoding='utf-8', mode='r') as data_file:
            for line in data_file:
                words = line.strip().split()
                if words and len(words) == 2:
                    if words[0] not in self.common_vocab:
                        self.common_vocab[words[0]] = set()
                    self.common_vocab[words[0]].add(words[1])

        self.common_regex = dict()
        with open(config.common_regex_path, encoding='utf-8', mode='r') as data_file:
            for line in data_file:
                words = line.strip().split()
                if words and len(words) == 2:
                    if words[0] not in self.common_regex:
                        self.common_regex[words[0]] = set()
                    self.common_regex[words[0]].add(words[1])


    def match_vocab(self, sentence, common_vocab):
        """
        vocab match word from sentence by using common_dict
        :param sentence:
        :param common_dict:
        :return:
        """
        entities = []
        sentence_upper = sentence.upper()
        for start_index in range(len(sentence_upper)):
            for end_index in range(start_index + 1, len(sentence_upper) + 1):
                sub_sentence_upper = sentence_upper[start_index: end_index]
                if sub_sentence_upper in common_vocab:
                    labels = common_vocab[sub_sentence_upper]
                    for label in labels:
                        entity = Entity(label, sentence[start_index: end_index], self.default_rule_score, start_index, end_index)
                        entities.append(entity)
        return entities


    def match_regex(self, sentence, common_regex):
        """
        regex match word from sentence by using common_dict
        :param sentence:
        :param common_dict:
        :return:
        """
        entities = []
        sentence_upper = sentence.upper()
        for word, labels in common_regex.items():
            for item in re.finditer(word, sentence_upper):
                start_index = item.regs[0][0]
                end_index = item.regs[0][1]
                for label in labels:
                    entity = Entity(label, sentence[start_index: end_index], self.default_rule_score, start_index, end_index)
                    entities.append(entity)
        return entities


    def predict(self, sentence):
        """
        predict entity from sentence by using Rule-based method
        :param sentence:
        :return:
        """
        vocab_entities = self.match_vocab(sentence, self.common_vocab)
        regex_entities = self.match_regex(sentence, self.common_regex)
        entities = []
        entities.extend(vocab_entities)
        entities.extend(regex_entities)
        return entities


def main():
    sentence = '2018年6月16号端午节期间，丹棱街5号办理438元可享受优惠'
    ner_regexp = RegexNer()
    entities = ner_regexp.predict(sentence)
    for entity in entities:
        print('EntityType: %s, EntityValue: %s, Score: %s, start_index: %s, end_index: %s' %
              (entity.entity_type, entity.entity_value, entity.score, entity.start_index, entity.end_index))


if __name__ == '__main__':
    main()
