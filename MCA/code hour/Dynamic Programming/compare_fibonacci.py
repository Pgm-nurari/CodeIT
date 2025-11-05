"""Compare and benchmark three Fibonacci implementations.

This script benchmarks:
 - naive recursion (`fibonacci_naive`)
 - memoized recursion (`fibonacci_memoized`)
 - tabulated bottom-up (`fibonacci_tabulated`)

Usage:
  python compare_fibonacci.py 6 --repeats 3 [--include-naive]

By default naive is skipped for n > 10 to avoid very long runs.
"""

from time import perf_counter
import argparse
import sys

# Import local implementations (same directory)
from fibonacci import fibonacci_naive
from fibMemiization import fibonacci_memoized
from fibTabulation import fibonacci_tabulated


def bench(func, n, repeats=3):
    """Run `func(n)` `repeats` times and return (min_time, avg_time, result).

    Assumes func returns the Fibonacci value.
    """
    times = []
    result = None
    for _ in range(repeats):
        t0 = perf_counter()
        result = func(n)
        t1 = perf_counter()
        times.append(t1 - t0)
    return min(times), sum(times) / len(times), result, times


def run_benchmarks(n, repeats=3, include_naive=False):
    print(f"Benchmarking Fibonacci implementations for n={n} (repeats={repeats})\n")

    results = {}

    # Tabulated (fast)
    t_min, t_avg, res_tab, all_tab = bench(lambda x: fibonacci_tabulated(x, verbose=False, show_bars=False), n, repeats)
    results['tabulated'] = {'min': t_min, 'avg': t_avg, 'result': res_tab, 'times': all_tab}
    print(f"tabulated: result={res_tab}, min={t_min:.6f}s, avg={t_avg:.6f}s")

    # Memoized (fast)
    t_min, t_avg, res_memo, all_memo = bench(lambda x: fibonacci_memoized(x, memo=None, depth=0, verbose=False), n, repeats)
    results['memoized'] = {'min': t_min, 'avg': t_avg, 'result': res_memo, 'times': all_memo}
    print(f"memoized : result={res_memo}, min={t_min:.6f}s, avg={t_avg:.6f}s")

    # Naive (may be slow) - only run if requested or n is small
    if include_naive or n <= 10:
        t_min, t_avg, res_naive, all_naive = bench(fibonacci_naive, n, repeats)
        results['naive'] = {'min': t_min, 'avg': t_avg, 'result': res_naive, 'times': all_naive}
        print(f"naive    : result={res_naive}, min={t_min:.6f}s, avg={t_avg:.6f}s")
    else:
        print("naive    : skipped (use --include-naive to force)")

    # Verify all computed results (for methods run) agree
    computed = {k: v['result'] for k, v in results.items()}
    if len(set(computed.values())) == 1:
        print("\nAll methods produced the same result.")
    else:
        print("\nWARNING: Methods produced different results:")
        for k, v in computed.items():
            print(f"  {k}: {v}")

    return results


def parse_args(argv):
    p = argparse.ArgumentParser(description="Compare Fibonacci implementations")
    p.add_argument('n', type=int, nargs='?', default=6, help='Index n for Fibonacci')
    p.add_argument('--repeats', '-r', type=int, default=3, help='Number of repeats per method')
    p.add_argument('--include-naive', action='store_true', help='Include naive recursive method even for larger n')
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    if args.n < 0:
        print("Please provide a non-negative n")
        return
    if args.n > 30 and not args.include_naive:
        print("Note: naive recursion skipped by default for n > 10. Use --include-naive to force naive run.")

    run_benchmarks(args.n, repeats=args.repeats, include_naive=args.include_naive)


if __name__ == '__main__':
    main()
