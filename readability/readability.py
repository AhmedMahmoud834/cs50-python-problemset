def main():
    text = input("Text: ")
    letters, words, sentences = calc_w_l_s(text)

    L = float(letters) / words * 100
    S = float(sentences) / words * 100
    index = (0.0588 * L) - (0.296 * S) - 15.8

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {int(round(index))}")


def calc_w_l_s(text: str):
    letters = 0
    spaces = 0
    sentences = 0
    for char in text:
        if char.isalpha():
            letters += 1
        elif char == " ":
            spaces += 1
        elif char in ["!","?","."]:
            sentences += 1
    return letters, spaces + 1, sentences

if __name__ == "__main__":
    main()
