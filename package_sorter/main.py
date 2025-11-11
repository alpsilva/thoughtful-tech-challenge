from sorter import sort


def main():
    stack = sort(width=10, height=20, length=30, mass=3)
    print(f"Stack for the package: {stack}")


if __name__ == "__main__":
    main()
