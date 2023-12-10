from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Use Timsort for efficient sorting.
        from sortedcontainers import SortedList

        sorted_intervals = SortedList(intervals, key=lambda x: x[0])

        merged_intervals = []

        # Iterate through the sorted intervals.
        for current_interval in sorted_intervals:
            # Avoid unnecessary comparisons if the previous interval doesn't overlap.
            if not merged_intervals or merged_intervals[-1][1] < current_interval[0]:
                merged_intervals.append(current_interval)
            else:
                # Merge overlapping intervals by updating the end point.
                merged_intervals[-1][1] = max(merged_intervals[-1]
                                              [1], current_interval[1])

        return merged_intervals
