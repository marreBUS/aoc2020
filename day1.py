my_file = open('input-day1.txt', 'r')
content = my_file.read().split('\n')
content = list(filter(None, content))
input_list = [ int(x) for x in content]

def solution1(target):
    small_list = []
    large_list = []
    half_list = []
    final_x = 0
    final_y = 0
    final_sum = 0

    for x in input_list:
        if x > target/2:
            large_list.append(x)
        if x < target/2:
            small_list.append(x)
        if x == target/2:
            half_list.append(x)

        for x in small_list:
            for y in large_list:
                if x+y == target:
                    final_x = x
                    final_y = y
                    final_sum = final_x + final_y
    print("X: ", final_x, " Y: ", final_y, " Sum: ", final_sum, " Product: ", final_x * final_y)

def solution2(target):
    first_filter = []
    second_filter = []
    for x in input_list:
        base = target - x
        if base < target and base > 0:
            first_filter = list(filter(lambda y: y < base, input_list ))
        for z in first_filter:
            base2 = base - (x + z)
            if base2 <= base and base2 > 0:
                second_filter = list(filter(lambda a: a < base2, first_filter))
            for b in second_filter:
                if(b + x + z) == target:
                    print("x: ", x, "z: ", z, "b: ", b, "sum: ", x+z+b, " Product: ", b * x * z)

solution1(2020)
solution2(2020)