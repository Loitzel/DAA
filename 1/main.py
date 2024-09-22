import json
import random
from generate_problem import generate_random_tree
from brute_force_solver import count_valid_splits as bruteforce
from recursive_dp_solver import count_valid_splits as recursive_dp

def main():

    with open('tree_examples_bruteforce.json', 'r') as f:
        test_cases = json.load(f)

    results = []
    # Process each test case
    for test_case in test_cases:
        n = test_case['vertices']
        edges = test_case['edges']
        black_vertices = set(test_case['black_vertices'])
        correct_answer = test_case['solution']

        (valid_splits, time) = recursive_dp(n, edges, black_vertices)

        if valid_splits != correct_answer:
            raise Exception(f"Answers didn't match: Expected: {correct_answer}, Got: {valid_splits}")
        results.append({
                    "vertices": n,
                    "edges": edges,
                    "black_vertices": list(black_vertices),
                    "solution": valid_splits,
                    "time": time
                })

        with open("tree_examples_recursive_dp.json", "w") as f:
            json.dump(results, f, indent=4)
        
if __name__ == "__main__":
    main()
