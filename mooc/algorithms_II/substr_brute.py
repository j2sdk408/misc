"""
implementation of brute force search
"""


def search(pattern, text):
    """search pattern in text"""

    for i in xrange(len(text) - len(pattern)):
        for j in xrange(len(pattern)):
            if text[i + j] != pattern[j]:
                break
        else:
            return i

    return len(text) + 1

if __name__ == "__main__":

    text = "this is supposed to be a writer's retreat."
    pattern = "be2"

    print search(pattern, text)

