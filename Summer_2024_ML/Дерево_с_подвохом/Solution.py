
def parse_input():
    f, c, n = map(int, input().split())
    tree = [list(map(float, input().split())) for _ in range(2 * n)]
    return f, c, n, tree


PATHS = []
def rec_build_tree(info, data, cur_path):
    if info == [-1, -1]:
        cur_path += '->' + str(data)
        PATHS.append(cur_path)
        return

    else:
        rec_build_tree()

def main():
    f, c, n, tree = parse_input()
    root = build_tree(tree)
    print(root)


if __name__ == '__main__':
    main()
