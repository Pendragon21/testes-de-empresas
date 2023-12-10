class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i, j = 0, 0  # Indices for iterating through s and p
        last_match, star = 0, -1  # Indices for tracking last match and star position

        while i < len(s):
            # Matching characters or '?' wildcard
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            # Encountering '*' wildcard
            elif j < len(p) and p[j] == '*':
                last_match = i  # Store the last match index
                star = j  # Store the star index
                j += 1
            # Backtracking with '*'
            elif star != -1:
                j = star + 1  # Move forward in p
                i = last_match + 1  # Move forward in s, adjusting for match
                last_match += 1  # Update last_match for next iteration
            # No match found
            else:
                return False

        # Check if remaining characters in p are all '*'
        while j < len(p) and p[j] == '*':
            j += 1

        # Return True if both strings reach the end
        return j == len(p)
