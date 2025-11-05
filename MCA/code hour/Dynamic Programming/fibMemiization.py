
"""Fibonacci with memoization and verbose tracing.

This script provides a `fibonacci_memoized` function that can print
every recursive call, the current memo table, and values computed.

Usage: run the script and enter a small positive integer (e.g., 6).
Be careful with large n: the trace grows quickly.

Usage: run the script and enter a small positive integer (e.g., 6).
Be careful with large n: the trace grows quickly.
"""



def fibonacci_memoized(n, memo=None, depth=0, verbose=True):
    """Compute fibonacci(n) with memoization and optional step tracing.

    Args:   
        n (int): non-negative integer index.
        memo (dict|None): dictionary to reuse across recursive calls.
        depth (int): recursion depth used for indentation in traces.
        verbose (bool): if True, prints step-by-step trace.

    Returns:
        int: Fibonacci number F(n).
    """
    if memo is None:
        memo = {}

    indent = '  ' * depth
    if verbose:
        print(f"{indent}Call: fibonacci({n}) | memo keys: {sorted(memo.keys())}")

    # Check memoized result first
    if n in memo:
        if verbose:
            print(f"{indent}  -> Found in memo: {n} = {memo[n]}")
        return memo[n]

    # Base cases
    if n <= 1:
        result = n
        if verbose:
            print(f"{indent}  -> Base case: fibonacci({n}) = {result}")
    else:
        # Recurse with increased depth so traces align visually
        a = fibonacci_memoized(n-1, memo, depth+1, verbose)
        b = fibonacci_memoized(n-2, memo, depth+1, verbose)
        result = a + b
        if verbose:
            print(f"{indent}  -> Computed: fibonacci({n-1}) + fibonacci({n-2}) = {a} + {b} = {result}")

    memo[n] = result
    if verbose:
        print(f"{indent}  -> Store memo[{n}] = {result}\n")
    return result


def main():
    try:
        n = int(input("Enter a small non-negative integer (e.g. 6): "))
    except Exception:
        print("Invalid input. Please enter a non-negative integer.")
        return

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    if n > 30:
        print("Warning: large n will produce a lot of output. Consider n <= 20 for readable traces.")

    print(f"Tracing fibonacci_memoized({n})...\n")
    from time import perf_counter
    t0 = perf_counter()
    result = fibonacci_memoized(n, memo=None, depth=0, verbose=True)
    t1 = perf_counter()
    print(f"Result: Fibonacci({n}) = {result}")
    print(f"Time: {t1 - t0:.6f}s")


if __name__ == "__main__":
    main()