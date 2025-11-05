"""Fibonacci by tabulation with optional step-by-step visualization.

Functions:
  fibonacci_tabulated(n, verbose=False, show_bars=False)

Run as a script to pass n and flags, e.g.:
  python fibTabulation.py 6 --verbose --bars
"""

import sys
from time import perf_counter


def _bar(v, max_width=40):
    # Simple bar for visualization; cap width to avoid huge lines
    w = min(v, max_width)
    return "|" + ("#" * w)


def fibonacci_tabulated(n, verbose=False, show_bars=False):
    """Compute Fibonacci using bottom-up tabulation.

    If verbose is True, prints each iteration and the dp array so far.
    If show_bars is True, prints a simple bar graph of dp values.
    """
    if n <= 1:
        if verbose:
            print(f"n={n} -> base case -> {n}")
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    if verbose:
        print(f"init: dp = {dp}")

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        if verbose:
            print(f"i={i}: dp[{i-2}]={dp[i-2]}, dp[{i-1}]={dp[i-1]} => dp[{i}]={dp[i]}")
            print(f"  dp so far: {dp[:i+1]}")
            if show_bars:
                bars = ' '.join(_bar(v) for v in dp[:i+1])
                print(f"  bars: {bars}")

    if verbose:
        print(f"final dp: {dp}")
    return dp[n]


def _cli_main():
    args = sys.argv[1:]
    verbose = False
    show_bars = False
    n = None

    for a in args:
        if a in ("-v", "--verbose"):
            verbose = True
        elif a in ("-b", "--bars"):
            show_bars = True
        else:
            # first non-flag arg is n
            if n is None:
                try:
                    n = int(a)
                except ValueError:
                    print(f"Invalid integer: {a}")
                    return

    if n is None:
        # fallback to interactive prompt
        try:
            n = int(input("Enter a small non-negative integer (e.g. 6): "))
        except Exception:
            print("Invalid input")
            return

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    if n > 50 and show_bars:
        print("Note: bars may be very large; they will be capped.")

    print(f"Computing fibonacci_tabulated({n}) (verbose={verbose}, bars={show_bars})\n")
    t0 = perf_counter()
    result = fibonacci_tabulated(n, verbose=verbose, show_bars=show_bars)
    t1 = perf_counter()
    print(f"Result: Fibonacci({n}) = {result}")
    print(f"Time: {t1 - t0:.6f}s")


if __name__ == "__main__":
    _cli_main()