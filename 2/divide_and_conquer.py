from timing import timing

def min_moves_to_good_string(s, c, start, end):
    if start == end:
        return 0 if s[start] == c else 1

    mid = (start + end) // 2
    next_char = chr(ord(c) + 1)

    left_changes = sum(1 for i in range(start, mid + 1) if s[i] != c)
    right_changes = sum(1 for i in range(mid + 1, end + 1) if s[i] != c)

    left_good = min_moves_to_good_string(s, next_char, mid + 1, end)
    right_good = min_moves_to_good_string(s, next_char, start, mid)

    return min(left_changes + left_good, right_changes + right_good)

@timing
def solve_a_good_string(s):
    n = len(s)
    return min_moves_to_good_string(s, 'a', 0, n - 1)

