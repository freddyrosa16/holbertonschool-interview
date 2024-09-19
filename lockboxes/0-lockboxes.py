#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    unlocked = set()
    to_explore = [0]

    while to_explore:
        box = to_explore.pop()
        if box not in unlocked:
            unlocked.add(box)
            for key in boxes[box]:
                if key not in unlocked and key < len(boxes):
                    to_explore.append(key)

    return len(unlocked) == len(boxes)
