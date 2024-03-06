from typing import Optional
from collections import deque

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def build_tree_from_level_order(values: list) -> Optional[Node]:
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root])
    is_left = True

    for val in values[1:]:
        curr = queue.popleft()
        new = Node(val)

        if is_left:
            curr.left = new
            queue.appendleft(curr)
        else:
            curr.right = new

        queue.append(new)
        is_left = not is_left

    return root


def traverse_level_order(root: Optional[Node]):
    if not root:
        return None

    result = []
    queue = [root]

    while queue:
        next_queue = []
        level = []
        for node in queue:
            level.append(node.value)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

        result.extend(level)
        queue = next_queue

    return result


def is_valid_bst(root: Optional[Node]):
    def _is_valid_recursive(node: Optional[Node], min_seen: float, max_seen: float):
        if not node or (not node.left and not node.right):
            return True

        is_in_range = min_seen < node.value < max_seen
        return is_in_range and _is_valid_recursive(node.left, min_seen, node.value) and _is_valid_recursive(node.right, node.value, max_seen)

    return _is_valid_recursive(root, float('-inf'), float('inf'))


values = [5, 3, 7, 1, 4, 5, 9]
tree = build_tree_from_level_order(values)
result = traverse_level_order(tree)
is_valid = is_valid_bst(tree)
