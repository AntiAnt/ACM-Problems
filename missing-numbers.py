import sys


if __name__ == "__main__":
    n = None
    step = 0
    missing = []
    mod = 0


    for i in sys.stdin:
        if n is None:
            n = int(i)
            continue

        
        
        expected = step + 1 + len(missing)

        if int(i) != expected:
            mod += abs(int(i) - expected)
            missing += range(int(i) - 1, expected - 1, -1)
 
        step += 1

        if step >= n:
            break

    if len(missing) == 0:
        print("good job")
    missing.sort()
    for m in missing:
        print(m)