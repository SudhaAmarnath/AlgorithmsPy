https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

'''
For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.
'''
def almostIncreasingSequence(sequence):
    i = 0
    while i < len(sequence) - 1:
        if not sequence[i] < sequence[i + 1]:
            if increasingSequence(sequence[:i] + sequence[i+1:]) or increasingSequence(sequence[:i+1] + sequence[i+2:]):
                return True
            else:
                return False
        i += 1
    return True


def increasingSequence(sequence):
    for i in range(len(sequence) - 1):
        if not sequence[i] < sequence[i + 1]:
            return False
    return True
