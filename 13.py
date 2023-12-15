import functools

f = open("input.txt", "r")
input = [group for group in f.read().split('\n\n')]

def fix_smudge(a, b):
    if a is None or b is None:
        return None
    count = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return a


def transpose(matrix):
    result = []
    for x in range(0, len(matrix[0])):
        line = ''
        for y in range(len(matrix) - 1, -1, -1):
            line += matrix[y][x]
        result.append(line)
    return result


def test_for_symmetry(matrix, index):
    for i in range(0, index + 1):
        if (index - i) >= 0 and (index + i + 1) < len(matrix):
            if matrix[index - i] != matrix[index + i + 1]:
                return False
    return True


def fix_smudge_in_matrix(matrix, index):
    test_matrix = matrix[:]
    for i in range(0, index + 1):
        if (index - i) >= 0 and (index + i + 1) < len(matrix):
            a = fix_smudge(matrix[index - i], matrix[index + i + 1])
            if a is not None:
                test_matrix[index - i] = a
                test_matrix[index + i + 1] = a
                if test_for_symmetry(test_matrix, index):
                    return test_matrix
    return None


split_input = [x for x in input]
total = 0


def fix_smudge_and_test_smart(matrix, h_factor):
    score = 0
    for index in range(0, len(matrix) - 1):
        if matrix[index] == matrix[index + 1]:
            fix = fix_smudge_in_matrix(matrix, index)
            if fix is not None:
                matrix = fix
                if test_for_symmetry(matrix, index):
                    score = (index + 1) * h_factor
                    break
    return score

def fix_smudge_and_test_brute(matrix, h_factor):
    score = 0
    for index in range(0, len(matrix) - 1):
        fix = fix_smudge_in_matrix(matrix, index)
        if fix is not None:
            matrix = fix
            if test_for_symmetry(matrix, index):
                score = (index + 1) * h_factor
                break
    return score


for input in split_input:
    m = input.splitlines()
    transposed_matrix = transpose(m)
    answer = fix_smudge_and_test_smart(m, 100)
    if answer == 0:
        answer = fix_smudge_and_test_smart(transposed_matrix, 1)
    if answer == 0:
        answer = fix_smudge_and_test_brute(transposed_matrix, 1)
    if answer == 0:
        answer = fix_smudge_and_test_brute(m, 100)
    total += answer
print(total)
