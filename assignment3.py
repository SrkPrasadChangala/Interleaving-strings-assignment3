import sys

def is_interleaving(s1, s2, s3):
    """
    Determine if s3 can be formed by interleaving s1 and s2 while preserving the required conditions.
    """
    len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
    
    # If lengths don't match, interleaving is not possible
    if len_s1 + len_s2 != len_s3:
        return False, 0, []

    # Dynamic Programming Table
    dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    dp[0][0] = True

    # Fill DP Table
    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i][j - 1]

    # If the bottom-right corner is False, interleaving is not possible
    if not dp[len_s1][len_s2]:
        return False, 0, []

    # Backtrack to find all interleaving sequences
    interleavings = []

    def backtrack(i, j, substrings_s1, substrings_s2, prev_source):
        # Ensure the absolute difference in the number of substrings is at most 1
        if abs(len(substrings_s1) - len(substrings_s2)) > 1:
            return

        if i == len_s1 and j == len_s2:
            interleavings.append((substrings_s1[:], substrings_s2[:]))
            return

        if i < len_s1 and dp[i + 1][j] and s1[i] == s3[i + j]:
            if prev_source == "s1" and substrings_s1:
                substrings_s1[-1] += s1[i]
            else:
                substrings_s1.append(s1[i])
            backtrack(i + 1, j, substrings_s1, substrings_s2, "s1")
            if prev_source == "s1":
                substrings_s1[-1] = substrings_s1[-1][:-1]  # Backtrack
            else:
                substrings_s1.pop()

        if j < len_s2 and dp[i][j + 1] and s2[j] == s3[i + j]:
            if prev_source == "s2" and substrings_s2:
                substrings_s2[-1] += s2[j]
            else:
                substrings_s2.append(s2[j])
            backtrack(i, j + 1, substrings_s1, substrings_s2, "s2")
            if prev_source == "s2":
                substrings_s2[-1] = substrings_s2[-1][:-1]  # Backtrack
            else:
                substrings_s2.pop()

    backtrack(0, 0, [], [], None)
    return True, len(interleavings), interleavings


def process_input(file_name):
    """
    Read the input file and parse the strings s1, s2, and s3.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
        s1 = lines[0].strip()
        s2 = lines[1].strip()
        s3 = lines[2].strip()
    return s1, s2, s3


def write_output(file_name, result):
    """
    Write the output to a file in the specified format.
    """
    with open(file_name, 'w') as file:
        exists, count, interleavings = result
        file.write(f"Interleaving exists: {exists}, Count of interleavings: {count}\n")
        if exists:
            # Output the first valid interleaving
            s1_substrs, s2_substrs = interleavings[0]
            file.write(f"s1 substrings: {', '.join(s1_substrs)}\n")
            file.write(f"s2 substrings: {', '.join(s2_substrs)}\n")


if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python interleaving.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace("Input","Output")  # Default output file name

    s1, s2, s3 = process_input(input_file)
    result = is_interleaving(s1, s2, s3)
    write_output(output_file, result)

    print(f"Results written to {output_file}")

