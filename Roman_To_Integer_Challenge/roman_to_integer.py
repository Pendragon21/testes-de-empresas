class Solution:
    def romanToInt(self, s: str) -> int:

        # Define a dictionary to map Roman symbols to their corresponding integer values.
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Initialize an integer variable to store the accumulated value.
        integer_value = 0

        # Iterate through each character in the Roman numeral string.
        for i in range(len(s)):

            # Get the current character and its corresponding integer value.
            current_value = roman_values[s[i]]

            # Check for special cases where a smaller symbol precedes a larger one.
            if i > 0 and current_value > roman_values[s[i - 1]]:
                # In such cases, the current symbol represents subtraction.
                # Account for subtraction by subtracting twice the previous symbol's value.
                integer_value -= 2 * roman_values[s[i - 1]]

            # Add the current symbol's value to the accumulated integer value.
            integer_value += current_value

        # Return the final integer value obtained after processing all characters.
        return integer_value
