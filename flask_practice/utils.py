def testfun(x: int, y: int) -> int:
    return x + y

if __name__ == "__main__":
    print(__name__)
    print("This is sample.")

    x = 1
    y = 2
    result = testfun(x, y)
    print(result)
