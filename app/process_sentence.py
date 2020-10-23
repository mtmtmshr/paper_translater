import sys


def process_sentence(text):
    lines = text.split("\r\n")
    processed_sentence = ""
    for line in lines:
        if not line:
            continue
        if line[-1] == "-":
            line = line.rstrip("-")
            processed_sentence += line
        else:
            processed_sentence += line + " "
    processed_sentence = processed_sentence.replace(" ", "%20")
    return processed_sentence


if __name__ == "__main__":
    text = sys.argv[1]
