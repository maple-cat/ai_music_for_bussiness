import grpc
import ner_pb2
import ner_pb2_grpc
import csv
from tqdm import tqdm


def run(input_file, output_file):
    channel = grpc.insecure_channel('localhost:50052')
    # channel = grpc.insecure_channel('10.172.119.66:50052')
    # channel = grpc.insecure_channel('10.150.148.144:50052')
    stub = ner_pb2_grpc.NerStub(channel)
    write_lines = []
    with open(input_file, 'r', encoding='utf-8-sig') as reader:
        for line in reader:
            sentence = line.strip()
            response = stub.process(ner_pb2.NerRequest(sentence=sentence))
            for entity in response.entities:
                print('EntityType: %s, EntityValue: %s, Score: %s, start_index: %s, end_index: %s' %
                    (entity.entity_type, entity.entity_value, entity.score, entity.start_index, entity.end_index))
                if entity.entity_type == 'MUSIC':
                    sentence = sentence + '\t' + '意图0' + '\n'
                    break
                sentence = sentence + '\t' + '意图1' + '\n'

            write_lines.append(sentence)


    with open(output_file, 'w', encoding='utf-8-sig') as writer:
        writer.writelines(write_lines)


if __name__ == '__main__':
    run('total.txt', 'music-result.txt')
