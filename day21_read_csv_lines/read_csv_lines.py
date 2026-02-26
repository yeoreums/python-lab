def read_data(filename):
    lines = []
    with open(filename) as file:
        next(file)
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


def main():
    lines = read_data("sales.csv")
    print(lines)


if __name__ == "__main__":
    main()