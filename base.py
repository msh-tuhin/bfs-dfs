import state
import utils
# 0,8,7,6,5,4,3,2,1
# initial = [0,1,2,3,4,5,7,6,8]
# initial = [1,2,5,3,4,0,6,7,8]
# initial = [6,1,8,4,0,2,7,3,5]
initial = [8,6,4,2,1,3,5,7,0]
# initial = [3,1,2,0,4,5,6,7,8]
# init_list = list(initial)

method = 'bfs'
root = state.State(initial)
root.key = utils.key_gen(root.tile_positions)
root.get_empty()

if method == 'bfs':
    frontier = state.Queue()
else:
    frontier = state.Stack()
frontier.add(root)
explored = dict()
keys_to_id = dict()
keys_to_id[root.key] = root.id
id = 1
node_expanded = 0
max_depth = 0
while not frontier.isEmpty():
    node = frontier.remove()
    # keys_to_id[node.key] = node.id
    # explored[node.key] = node
    if utils.goalTest(node):
        print("successful")
        print("cost_of_path: ", node.depth)
        path = utils.path_finder(node)
        path.reverse()
        print("path_to_goal: ", path)
        break
    else:
        node_expanded += 1
        # print(node_expanded)
        node.get_possible_actions(method)
        id, depth, flag = utils.transitor(node, frontier, explored, keys_to_id, id)
        if depth > max_depth and flag == 1:
            max_depth = depth

print("node_expanded: ", node_expanded)
print("max_search_depth", max_depth)








