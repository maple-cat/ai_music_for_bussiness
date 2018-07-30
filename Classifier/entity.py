class Entity(object):

    def __init__(self, entity_type, entity_value, score, start_index, end_index):
        self.entity_type = entity_type
        self.entity_value = entity_value
        self.score = score
        self.start_index = start_index
        self.end_index = end_index


    def __eq__(self, other):
        """
        define entity1 == entity2
        :param other:
        :return:
        """
        if self.entity_type == other.entity_type and self.entity_value == other.entity_value and \
                self.start_index == other.start_index and self.end_index == other.end_index:
            return True
        else:
            return False


    def __ne__(self, other):
        """
        define entity1 != entity2
        :param other:
        :return:
        """
        if self.start_index > other.end_index or self.end_index < other.start_index:
            return True
        else:
            return False


    def contain(self, entity_other):
        """
        define entity1 contain entity2
        :param other:
        :return:
        """
        if self.entity_type == entity_other.entity_type and self.start_index <= entity_other.start_index and self.end_index >= entity_other.end_index:
            return True
        else:
            return False