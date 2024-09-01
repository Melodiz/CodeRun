def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


def seconds_to_time(seconds):
    h = (seconds // 3600) % 24
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"


def sntp(a, b, c):
    A = time_to_seconds(a)
    B = time_to_seconds(b)
    C = time_to_seconds(c)
    if A > C:
        C += 86400

    # Calculate the exact time
    exact_time = B + (C - A) / 2

    # Round to the nearest second
    exact_time = round(exact_time)

    # Convert back to hh:mm:ss format
    return seconds_to_time(exact_time)


def main():
    nums = [input().strip() for _ in range(3)]
    print(sntp(*nums))


if __name__ == "__main__":
    main()
