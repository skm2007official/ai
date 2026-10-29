import math

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or isinstance(node, int):
        return node

    if maximizing_player:
        best_value = -math.inf

        for child in node:
            value = alpha_beta(
                child, depth - 1, alpha, beta, False
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                break

        return best_value

    else:
        best_value = math.inf

        for child in node:
            value = alpha_beta(
                child, depth - 1, alpha, beta, True
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                break

        return best_value


# Game tree
tree = [
    [3, 5],
    [6, 9]
]

result = alpha_beta(
    tree, 2, -math.inf, math.inf, True
)

print("Optimal value:", result)