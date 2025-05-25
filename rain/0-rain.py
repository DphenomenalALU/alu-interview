#!/usr/bin/python3

"""
Calculate how many square units of water will be retained after it rains.
"""

def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.
    
    Args:
        walls: List of non-negative integers representing wall heights
        
    Returns:
        Integer indicating total amount of rainwater retained
    """
    if not walls:
        return 0
        
    n = len(walls)
    water = 0
    
    # For each element, find the maximum height to its left and right
    for i in range(1, n - 1):
        # Find maximum height to the left
        left_max = max(walls[:i])
        
        # Find maximum height to the right
        right_max = max(walls[i + 1:])
        
        # The water trapped at current position is min of left_max and right_max
        # minus the height of current wall (if positive)
        min_height = min(left_max, right_max)
        if min_height > walls[i]:
            water += min_height - walls[i]
            
    return water
