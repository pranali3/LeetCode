# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    if not h or not word:
        return -1

    n = len(word)
    maxHeight = float("-inf")

    for ch in word:
        maxHeight = max(h[ord(ch.lower()) - 97], maxHeight)

    return n * maxHeight


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
