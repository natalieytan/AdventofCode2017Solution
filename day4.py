
    with open("day4input.txt") as open_file:
        data = open_file.read().splitlines()

    def part_1(data):
        count = 0
        for line in data:
            if len(line.split()) == len(set(line.split())):
                count +=1
        return count

    print(part_1(data))

    def part_2(data):
        count = 0
        for line in data:
            words_array = list(map(lambda x: ('').join(sorted(list(x))), line.split()))
            if len(words_array) == len(set(words_array)):
                count += 1
        return count 

    part_2(data)

    print(part_2(data))
