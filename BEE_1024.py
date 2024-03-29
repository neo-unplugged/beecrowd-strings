def ascii_shift(txt, step):
    shifted_text = "".join(list(map(lambda c: chr(ord(c) + step) if (65 <= ord(c.upper()) <= 90) else c, txt)))
    return shifted_text


def ascii_shift_all(txt, step):
    shifted_text = "".join(list(map(lambda c: chr(ord(c) + step), txt)))
    return shifted_text


def main():
    N = int(input())

    for _ in range(N):
        text = input()
        shifted_text = ascii_shift(text, 3)
        shifted_text_reversed = shifted_text[::-1]
        half = len(shifted_text_reversed) // 2
        last_half_txt = shifted_text_reversed[half:]
        last_half_all_shifted = ascii_shift_all(last_half_txt, -1)
        print(shifted_text_reversed[:half] + last_half_all_shifted)


if __name__ == "__main__":
    main()
