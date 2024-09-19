#!/usr/bin/python3
def canUnlockAll(boxes):
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
