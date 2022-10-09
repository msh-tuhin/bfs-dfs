import state
import copy

actions = [['Down', 'Right'],
           ['Down', 'Left', 'Right'],
           ['Down', 'Left'],
           ['Up', 'Down', 'Right'],
           ['Up', 'Down', 'Left', 'Right'],
           ['Up', 'Down', 'Left'],
           ['Up', 'Right'],
           ['Up', 'Left', 'Right'],
           ['Up', 'Left']]


def get_empty(tiles):
    for i in range(0, len(tiles)):
        if tiles[i] == 0:
            return i


def goalTest(node):
    # index = 0
    # for i in node.tile_positions:
    #     if i != index:
    #         return False
    #     index += 1
    # return True

    if node.key == '012345678':
        return True
    else:
        return False


def key_gen(a):
    key = ''
    for i in a:
        key += str(i)
    return key


def transitor(node, frontier, explored, keys_to_id, id):
    flag=0
    # print(node.possible_actions)
    for act in node.possible_actions:
        if act == 'Up':
            tiles = copy.copy(node.tile_positions)
            index = node.empty_position
            tiles[index] = node.tile_positions[index-3]
            tiles[index-3] = node.tile_positions[index]
            key = key_gen(tiles)
            # if key not in keys_to_id.keys():
            try:
                keys_to_id[key]
            except:
                flag = 1
                id += 1
                new_node = state.State(tiles, parent=node, key=key,
                                       id=id, pre_action='Up')
                new_node.get_empty()
                keys_to_id[key] = id
                # explored[key] = id
                frontier.add(new_node)
                # print(new_node.id)
        elif act == 'Down':
            tiles = copy.copy(node.tile_positions)
            tiles[node.empty_position] = node.tile_positions[node.empty_position + 3]
            tiles[node.empty_position + 3] = node.tile_positions[node.empty_position]
            key = key_gen(tiles)
            # if key not in keys_to_id.keys():
            try:
                keys_to_id[key]
            except:
                flag = 1
                id += 1
                new_node = state.State(tiles, parent=node, key=key,
                                       id=id, pre_action='Down')
                new_node.get_empty()
                keys_to_id[key] = id
                # explored[key] = id
                frontier.add(new_node)
                # print(new_node.id)

        elif act == 'Left':
            tiles = copy.copy(node.tile_positions)
            tiles[node.empty_position] = node.tile_positions[node.empty_position - 1]
            tiles[node.empty_position - 1] = node.tile_positions[node.empty_position]
            key = key_gen(tiles)
            # if key not in keys_to_id.keys():
            try:
                keys_to_id[key]
            except:
                flag = 1
                id += 1
                new_node = state.State(tiles, parent=node, key=key,
                                       id=id, pre_action='Left')
                new_node.get_empty()
                keys_to_id[key] = id
                # explored[key] = id
                frontier.add(new_node)
                # print(new_node.id)

        elif act=='Right':
            tiles = copy.copy(node.tile_positions)
            tiles[node.empty_position] = node.tile_positions[node.empty_position + 1]
            tiles[node.empty_position + 1] = node.tile_positions[node.empty_position]
            key = key_gen(tiles)
            # if key not in keys_to_id.keys():
            try:
                keys_to_id[key]
            except:
                flag = 1
                id += 1
                new_node = state.State(tiles, parent=node, key=key,
                                       id=id, pre_action='Right')
                new_node.get_empty()
                keys_to_id[key] = id
                # explored[key] = id
                frontier.add(new_node)
                # print(new_node.id)
    return id, node.depth+1, flag

def path_finder(node):
    rev_path = []
    while node.parent is not None:
        rev_path.append(node.pre_action)
        node = node.parent

    return rev_path



