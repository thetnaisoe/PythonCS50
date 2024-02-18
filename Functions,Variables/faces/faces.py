def main():
    name = input()
    print(convert(name))


def convert(sentence):
    if ":)" in sentence:
        sentence = sentence.replace(":)", "🙂")
    if ":(" in sentence:
        sentence = sentence.replace(":(", "🙁")

    return sentence


main()