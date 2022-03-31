def merging(encoding):
    dict1 = {}

    with open('1.txt', encoding=encoding) as file1:
        lines = 0
        for line in file1:
            if line != '\n':
                lines += 1

    with open('1.txt', encoding=encoding) as file1:
        data = file1.read()
        dict1['1.txt'] = [lines, data]

    with open('2.txt', encoding=encoding) as file2:
        lines = 0
        for line in file2:
            if line != '\n':
                lines += 1

    with open('2.txt', encoding=encoding) as file2:
        data = file2.read()
        dict1['2.txt'] = [lines, data]

    with open('3.txt', encoding=encoding) as file3:
        lines = 0
        for line in file3:
            if line != '\n':
                lines += 1

    with open('3.txt', encoding=encoding) as file3:
        data = file3.read()
        dict1['3.txt'] = [lines, data]

    return dict1


def sort():
    dict1 = merging('utf-8')
    sorted_tuple = sorted(dict1.items(), key=lambda x: x[1])

    return sorted_tuple


def new_file(encoding):
    data = sort()
    with open('123.txt', 'w', encoding=encoding) as doc:
        doc.write(f'{data[0][0]}\n{data[0][1][0]}\n{data[0][1][1]}\n')
        doc.write(f'{data[1][0]}\n{data[1][1][0]}\n{data[1][1][1]}\n')
        doc.write(f'{data[2][0]}\n{data[2][1][0]}\n{data[2][1][1]}\n')

new_file('utf-8')