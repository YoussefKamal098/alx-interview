#!/usr/bin/python3
"""
Lockboxes Problem

This script defines the function `canUnlockAll` that determines if all boxes
in a set of `n` locked boxes can be unlocked. Each box is numbered sequentially
from 0 to `n - 1` and contains keys to other boxes.

Function:
    canUnlockAll(boxes): Returns True if all boxes can be unlocked, else False.

The first box (box 0) is always unlocked. The function checks whether you can
unlock all the boxes using the keys found within the boxes.
"""


def canUnlockAll(boxes):
    """
    Determines whether all boxes can be unlocked.

    Args:
        boxes (list[list[int]]): A list where each sublist represents a box,
                                and each box contains integers representing
                                keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.

    Methodology:
        - We use a depth-first search (DFS) approach to unlock all possible
          boxes starting from box 0.
        - A helper function `tryUnlockBoxes` is used to recursively unlock
          boxes and mark them as unlocked.
        - After trying to unlock boxes, we verify if every box is unlocked
          by checking a list that tracks the unlocking status of each box.
    """

    # Get the total number of boxes
    boxes_number = len(boxes)

    """
     A list to track the unlocking status of each box;
     initially all boxes are locked (False)
    """
    unlocked_boxes = [False] * boxes_number

    def tryUnlockBoxes(key):
        """
        Recursively unlocks boxes based on the keys found within.

        Args:
            key (int): The index of the box to unlock.

        This function marks the current box (indexed by 'key') as unlocked,
        and then checks the keys inside this box to recursively unlock
        any other boxes.
        """
        # Mark the current box as unlocked
        unlocked_boxes[key] = True

        # Iterate over all the keys inside the current box
        for key in boxes[key]:
            """
            If the key corresponds to a valid box index and
            that box hasn't been unlocked yet
            """
            if key < boxes_number and not unlocked_boxes[key]:
                # Recursively unlock the box corresponding to this key
                tryUnlockBoxes(key)

    # Start unlocking from box 0 (which is always unlocked)
    tryUnlockBoxes(0)

    """
    After attempting to unlock all possible boxes,
    check if all boxes have been unlocked
    """
    return all(unlocked_boxes)
