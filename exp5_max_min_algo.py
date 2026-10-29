def minimax(depth, node_index, maximizing_player, values, height):
    if depth == height:
        return values[node_index]
    if maximizing_player:
        return max(
            minimax(depth+1, node_index*2, False, values, height),
            minimax(depth+1, node_index*2+1, False, values, height)
        )
    else:
        return min(
            minimax(depth+1, node_index*2, True, values, height),
            minimax(depth+1, node_index*2+1, True, values, height)
        )
values=[3,5,2,9,12,5,23,23]
import math
height= int(math.log2(len(values)))
optimal_value=minimax(0, 0, True, values, height)
print("optimal value:",optimal_value)