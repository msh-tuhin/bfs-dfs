import utils
import copy

class State:
    id = 1
    tile_positions = list()
    empty_position = 0
    parent = None
    possible_actions = list()
    pre_action = ''
    # children = list()
    cost = 0
    key = ''
    depth = 0

    def __init__(self, board_config, parent=None, key='', cost=0, id=1, pre_action=''):
        self.tile_positions = board_config
        self.parent = parent
        self.key = key
        self.cost = cost
        self.id = id
        self.pre_action = pre_action
        if parent is not None:
            self.depth = parent.depth + 1

    def get_empty(self):
        for i in range(0, len(self.tile_positions)):
            if self.tile_positions[i] == 0:
                self.empty_position = i

    def get_possible_actions(self, method):
        pa = copy.copy(utils.actions[self.empty_position])
        if method == 'dfs':
            pa.reverse()
        self.possible_actions = pa
        return pa


class Queue:
    elems = dict()
    front = 1
    rear = 0

    def add(self, node):
        self.elems[node.id] = node
        self.rear = node.id

    def remove(self):
        elem = self.elems[self.front]
        del self.elems[self.front]
        self.front += 1
        return elem




    def isEmpty(self):
        if len(self.elems.keys()) == 0:
            return True
        return False


    pass


class Stack:
    elems = []

    def add(self, node):
        self.elems.append(node)

    def remove(self):
        return self.elems.pop()

    def isEmpty(self):
        if len(self.elems) == 0:
            return True
        return False
