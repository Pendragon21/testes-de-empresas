## Wildcard Pattern Matching with ? and \*

**Challenge:**

Implement wildcard pattern matching with support for:

- `?`: Matches any single character.
- `*`: Matches any sequence of characters (including the empty sequence).

The match should cover the entire input string (not partial).

**Solution:**

This solution uses two pointers and a backtracking strategy to achieve efficient wildcard pattern matching.

**Pointers:**

- `i`: Iterates through the string `s`.
- `j`: Iterates through the pattern `p`.

**Variables:**

- `last_match`: Stores the index of the last character in `s` that matched the pattern before encountering a `*`.
- `star`: Stores the index of the last encountered `*`.

**Algorithm:**

1. **Iterate:** Loop through both `s` and `p` using the pointers.
2. **Matching Characters or ?:** If characters match or `?` is encountered, move both `i` and `j` forward.
3. \*_Encountering _:
   - Store `i` as `last_match`.
   - Store `j` as `star`.
   - Increment `j`.
4. \*_Backtracking with _:
   - If a mismatch occurs and a `*` exists:
     - Move `j` to the position after `star`.
     - Move `i` to `last_match + 1` and update `last_match` for the next iteration.
5. **No Match:** If no match is found and no `*` exists, return `False`.
6. **Remaining Pattern:** After iterating through both strings, check if remaining characters in `p` are all `*`.
7. **Result:** Return `True` if both strings reach the end, `False` otherwise.

**Pattern:**

This solution utilizes a backtracking approach with two pointers and additional variables to track matches and handle `*` characters efficiently. This is similar to dynamic programming solutions but avoids building a table.

**Additional Notes:**

- The code assumes both `s` and `p` are lowercase English letters.
- The code is optimized for performance and conciseness.
- Further improvements can be explored, such as using memoization to enhance cache performance.
