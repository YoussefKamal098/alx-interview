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
        boxes (list of lists): A list where each sublist represents a box, and
                               each box contains integers representing keys
                               to other boxes.

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
    boxes_number = len(boxes)

    # List to track which boxes are unlocked; initially, all boxes are locked
    unlocked_boxes = [False] * boxes_number

    def tryUnlockBoxes(key):
        """
        Recursively unlocks boxes based on the keys found within.

        Args:
            key (int): The index of the box to unlock.
        """
        # Unlock the current box
        unlocked_boxes[key] = True

        """
        Try to unlock all boxes that can be opened with
        the keys in the current box
        """
        for key in boxes[key]:
            if key < boxes_number and not unlocked_boxes[key]:
                tryUnlockBoxes(key)

    # Start unlocking from the first box (box 0)
    tryUnlockBoxes(0)

    # Check if all boxes are unlocked
    for key in unlocked_boxes:
        if not key:  # If any box is still locked, return False
            return False

    # If all boxes are unlocked, return True
    return True
