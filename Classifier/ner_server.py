import time
import grpc
import ner_pb2
import ner_pb2_grpc
from concurrent import futures
from ner_model.ner_predict import DeepNer
from ner_regex.ner_predict import RegexNer
from data_utils import DataUtils

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Ner(ner_pb2_grpc.NerServicer):
    def __init__(self):
        self.ner_model = DeepNer()
        self.ner_regexp = RegexNer()
        self.data_utils = DataUtils()


    def process(self, request, context):
        sentence = request.sentence
        sentence = ''.join(sentence.strip().split())
        print('------------------------------------')
        print('Receive sentence : %s' % sentence)
        if not sentence:
            return ner_pb2.NerReply(entities=[])
        # ner model
        model_entities = self.ner_model.predict(sentence)
        # ner regexp
        regex_entities = self.ner_regexp.predict(sentence)

        entities = []
        entities.extend(model_entities)
        entities.extend(regex_entities)
        entities = self.data_utils.remove_duplicated_entity(entities)

        pb_entities = []
        for entity in entities:
            pb_entity = ner_pb2.Entity(entity_type=entity.entity_type, entity_value=entity.entity_value,
                                           score=entity.score, start_index=entity.start_index, end_index=entity.end_index)
            pb_entities.append(pb_entity)
            print('EntityType: %s, EntityValue: %s, Score: %s, start_index: %s, end_index: %s' %
                  (entity.entity_type, entity.entity_value, entity.score, entity.start_index, entity.end_index))

        return ner_pb2.NerReply(entities=pb_entities)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ner_pb2_grpc.add_NerServicer_to_server(Ner(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
