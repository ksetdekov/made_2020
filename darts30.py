# hate it, hate it, hate it! fucking python and stupid exams that dont provide data to experiment with
# sample input
# 1
# 8 2
# 2 3 4 5 -30 6 -1 2
def input_filtered_nums(min_count=1, filters=[]):
    ''' Запрашивает у пользователя значения, разделенные пробелами,
        пока не накопит нужное количество отфильтрованных целых чисел'''

    nums = []
    while len(nums) < min_count:
        tmp = [int(s) for s in input().split(" ") if len(s.strip()) > 0]
        for _filter in filters:
            tmp = list(filter(_filter, tmp))
            if not tmp:
                break
        nums.extend(tmp)
    return (nums)

    n_targets = input_filtered_nums()
    targets = list()
    for i in range(n_targets[0]):
        target = dict()  # dict.fromkeys(['n_sect','black','points'])
        target['n_sect'], target['black'] = input_filtered_nums(2)
        target['points'] = input_filtered_nums(target['n_sect'])
        targets.append(target)

while True:
    print(input_filtered_nums())
    # data = input('input')
    #result = []
    # count = int(data[0])
    # for i in range(0, count):
    #     # print(i)
    #     result.append(12)
    # print(*result, sep='\n')





