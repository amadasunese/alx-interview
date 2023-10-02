#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box (box 0) is initially unlocked

    queue = [0]  # Start with the first box in the queue

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited (unlocked)
    return all(visited)
