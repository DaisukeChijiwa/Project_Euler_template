from time import perf_counter

def main():
    ans = 0
    return ans

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(round((perf_counter() - start) * 1000, 2), "ms")