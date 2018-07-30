import tensorflow as tf
import ner_model.config as config
from data_utils import DataUtils


class DeepNer:
    def __init__(self):
        with open(config.ner_graph_pbtxt_path, mode='rb') as graph_file:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(graph_file.read())
        graph_out = tf.import_graph_def(graph_def, name='')
        self.sess = tf.Session(graph=graph_out)
        self.sess.run(self.sess.graph.get_operation_by_name('init_all_tables'))
        self.data_utils = DataUtils()


    def predict(self, sentence):
        """
        ner predict by model
        :param sentence: sentence without whitespace, example '438元自选套餐包含流量'
        :return: predict labels
        """
        if not sentence:
            return []
        words_upper = ' '.join([char for char in sentence.upper()])
        predict_labels, predict_scores = self.sess.run(['predict_labels:0', 'predict_scores:0'], feed_dict={'input_sentences:0': [words_upper]})

        predict_labels = predict_labels[0].decode('utf-8').split()
        predict_scores = predict_scores[0].decode('utf-8').split()

        words = [char for char in sentence]
        format_predict_labels = []
        for label in predict_labels:
            format_predict_labels.append(label)
        format_predict_scores = [float(score) for score in predict_scores]

        entities = self.data_utils.extract_model_label(words, format_predict_labels, format_predict_scores)

        return entities


def main(_):
    ner_model = DeepNer()

    sentence = '2018年6月16号端午节期间，丹棱街5号办理438元可享受优惠'
    entities = ner_model.predict(sentence)
    for entity in entities:
        print('EntityType: %s, EntityValue: %s, Score: %s, start_index: %s, end_index: %s' %
              (entity.entity_type, entity.entity_value, entity.score, entity.start_index, entity.end_index))


if __name__ == '__main__':
    tf.app.run()
