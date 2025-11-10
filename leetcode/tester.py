"""
Simple method to run examples for LeetCode problems
"""
def test(inputs: list, expected, method: callable):
    actual = method(*inputs)
    print(f'Expected: {expected} - Actual: {actual} - Passed? {expected == actual}')

def test_inplace(inputs: list, expected, method: callable, inplace_comparison_selector: callable):
    result = method(*inputs)
    if result is not None:
        actual = [result, inplace_comparison_selector(inputs, result)]
    else:
        actual = inplace_comparison_selector(inputs)
    print(f'Expected: {expected} - Actual: {actual} - Passed? {expected == actual}')
