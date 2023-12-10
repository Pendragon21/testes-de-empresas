## LeetCode Challenge 1044: Longest Duplicate Substring

**Challenge:**

Given a string `s`, find the longest duplicate substring.

**Solution Approach:**

This repository presents a Python solution for LeetCode Challenge 1044: Longest Duplicate Substring.

This solution utilizes a binary search approach combined with a custom `has_duplicate` function to efficiently identify the longest repeating substring within the given string.

**Function Breakdown:**

- **`has_duplicate(s: str, length: int) -> bool`:**

  - This function iterates through the string using a sliding window of length `length`. It checks if the current substring exists in a previously encountered set of substrings.
  - If a duplicate is found, it returns `True` and the duplicate substring. Otherwise, it adds the current substring to the set and returns `False` and an empty string.

- **`longestDupSubstring(self, s: str) -> str`:**

  - This function employs binary search to find the largest value of `length` where a duplicate substring exists.
  - The search range starts with `[0, len(s)]` and narrows down with each iteration by checking for duplicates at the midpoint.

**Complexity:**

- Time Complexity: O(log(n) \* n)
- Space Complexity: O(n)

**Further Enhancements:**

- Implement rolling hash functions for faster substring comparisons.
- Utilize Bloom filters for improved space efficiency with large strings.

**Contribution:**

Feel free to contribute to this repository by:

- Suggesting improvements for edge cases.
- Implementing alternative solutions and comparing their performance.
- Sharing your insights and knowledge on this challenge.
