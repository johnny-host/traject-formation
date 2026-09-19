while True:
    try:
        n, r = map(int, input().split())
        retornaram = set(map(int, input().split()))
        
        if n == r:
            print("*")
        else:
            for i in range(1, n + 1):
                if i not in retornaram:
                    print(f"{i} ", end="")
            print()
    except EOFError:
        break
