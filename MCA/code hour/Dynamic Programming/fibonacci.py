"""Naive Fibonacci with an optional recursion visualizer.

This module contains the original naive recursive implementation and
an instrumented version that prints every call and return with
depth-based indentation. Run the file directly to try the visualizer:

  python fibonacci.py 5 --trace

Be careful: the naive recursion grows exponentially; keep n small (<= 10).
"""

from time import perf_counter
import sys


def fibonacci_naive(n):
    """Simple naive recursive Fibonacci (no tracing)."""
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_traced(n, depth=0, verbose=True, counter=None):
    """Naive Fibonacci with step-by-step tracing.

    Prints an entry line on call and a return line when the value is computed.
    A mutable `counter` dict may be passed to give unique call IDs across the
    entire recursion tree.
    """
    if counter is None:
        counter = {"id": 0}

    counter["id"] += 1
    cid = counter["id"]
    indent = "  " * depth
    if verbose:
        print(f"{indent}Call #{cid}: fibonacci({n})")

    if n <= 1:
        result = n
        if verbose:
            print(f"{indent}Return #{cid}: {result}")
        return result

    a = fibonacci_traced(n - 1, depth + 1, verbose, counter)
    b = fibonacci_traced(n - 2, depth + 1, verbose, counter)
    result = a + b
    if verbose:
        print(f"{indent}Return #{cid}: {result}")
    return result


def _cli_main():
    args = sys.argv[1:]
    trace = False
    n = None

    for a in args:
        if a in ("-t", "--trace"):
            trace = True
        else:
            if n is None:
                try:
                    n = int(a)
                except ValueError:
                    print(f"Invalid integer: {a}")
                    return

    if n is None:
        try:
            n = int(input("Enter a small non-negative integer (e.g. 5): "))
        except Exception:
            print("Invalid input")
            return

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    if n > 12 and trace:
        print("Warning: tracing large n will produce a lot of output. Consider n <= 10.")

    print(f"Computing fibonacci({n}) (trace={trace})\n")
    t0 = perf_counter()
    if trace:
        result = fibonacci_traced(n, depth=0, verbose=True, counter={"id": 0})
    else:
        result = fibonacci_naive(n)
    t1 = perf_counter()
    print(f"\nResult: Fibonacci({n}) = {result}")
    print(f"Time: {t1 - t0:.6f}s")


if __name__ == "__main__":
    _cli_main()