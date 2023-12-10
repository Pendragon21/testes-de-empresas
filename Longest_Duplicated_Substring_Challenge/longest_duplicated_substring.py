class Solution:
    def has_duplicate(self, s: str, length: int) -> bool:

        # Create a set to store encountered substrings.
        substring_set = set()

        # Iterate through the string using a sliding window of length `length`.
        for i in range(len(s) - length + 1):
            # Extract the current substring.
            substring = s[i:i + length]

            # Check if the substring exists in the set.
            if substring in substring_set:
                return True, substring
            else:
                # If not found, add it to the set for future comparisons.
                substring_set.add(substring)

        # If no duplicate is found, return False and an empty string.
        return False, ""

    def longestDupSubstring(self, s: str) -> str:

        # Initialize search range and result variables.
        start, end = 0, len(s)
        result = ""

        # Use binary search to find the largest substring length with a duplicate.
        while start + 1 < end:
            # Calculate the midpoint of the search range.
            mid = start + (end - start) // 2

            # Check if a duplicate substring of length `mid` exists.
            is_found, candidate = self.has_duplicate(s, mid)

            # If found, update the search range and result.
            if is_found:
                start, result = mid, candidate
            else:
                # If not found, shrink the search range by excluding the right half.
                end = mid

        # Return the final result, the longest duplicate substring found.
        return result
