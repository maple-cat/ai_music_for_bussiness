from entity import Entity


class DataUtils(object):

    def extract_model_label(self, words, labels, scores):
        """
        merge split label, example label-B label-M label-E label-S to label
        :param word_list:
        :param label_list:
        :return:
        """
        if not words or not labels or len(words) != len(labels) or len(words) != len(scores):
            return []

        entities = []
        record_word_list = []
        record_label = ''
        record_score = 0.0
        index = 0
        for (word, label, score) in zip(words, labels, scores):
            if word and label:
                if len(label) > 1 and label.find('-B') == len(label) - 2:
                    record_word_list.clear()
                    record_word_list.append(word)
                    record_label = label[0:-2]
                    record_score = score
                elif len(label) > 1 and label.find('-M') == len(label) - 2:
                    if record_label and record_label == label[0:-2]:
                        record_word_list.append(word)
                        if score < record_score:
                            record_score = score
                    else:
                        record_word_list.clear()
                        record_label = ''
                        record_score = 0.0
                elif len(label) > 1 and label.find('-E') == len(label) - 2:
                    if record_label and record_label == label[0:-2]:
                        record_word_list.append(word)
                        record_word = ''.join(record_word_list)
                        if score < record_score:
                            record_score = score
                        entity = Entity(record_label, record_word, record_score, index - len(record_word) + 1, index + 1)
                        entities.append(entity)
                    record_word_list.clear()
                    record_label = ''
                    record_score = 0.0
                elif len(label) > 1 and label.find('-S') == len(label) - 2:
                    record_label = label[0:-2]
                    entity = Entity(record_label, word, score, index, index + 1)
                    entities.append(entity)
                    record_word_list.clear()
                    record_label = ''
                    record_score = 0.0
                else:
                    record_word_list.clear()
                    record_label = ''
                    record_score = 0.0
                index += 1
            else:
                print('Input data exists empty element.')
                return []
        return entities


    def remove_duplicated_entity(self, entities):
        """
        remove duplicated entity
        :param entities:
        :return:
        """
        new_entities = []
        for entity in entities:
            add_flag = True
            index = 0
            while new_entities and index < len(new_entities):
                if new_entities[index].contain(entity):
                    add_flag = False
                    break
                elif entity.contain(new_entities[index]):
                    del new_entities[index]
                else:
                    index += 1
            if add_flag:
                new_entities.append(entity)
        return new_entities
