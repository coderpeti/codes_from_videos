def manacher_length_only(s: str) -> str:
    # Return an empty string if input is empty
    if not s:
        return ""
   
    # Transform the string to handle odd-length palindromes uniformly
    T = "#" + "#".join(s) + "#"

    # Get the length of the transformed string
    n = len(T)

    # Array to store the radius of the palindrome centered at each index
    P = [0] * n

    # Variables to track the center and the right boundary of the current palindrome
    C = R = 0

    # Iterate over the transformed strin
    for i in range(n):
        # Mirror index of 'i' (symmetric about center 'C')
        mirror = 2 * C - i

        # If we're inside the rightmost palindrome, try to use its symmetry
        if i < R:
            P[i] = min(R - i, P[mirror])

        # Expand around the center 'i' as long as characters match
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Update the center 'C' and the right boundary 'R' if necessary
        if i + P[i] > R:
            C = i
            R = i + P[i]

    # Find the maximum length palindrome and its center
    max_len = max(P)
    center = P.index(max_len)

    # Calculate the starting index of the palindrome in the original string
    start = (center - max_len) // 2
    
    # Return the longest palindromic substring from the original string
    return s[start:start + max_len]
    

print(manacher_length_only("abba"))  # Output: 'abba'
print(manacher_length_only("racecar"))  # Output: 'racecar'
print(manacher_length_only("abcde"))  # Output: 'a'