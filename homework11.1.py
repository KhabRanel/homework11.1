from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start1 = time.time()
# for file in filenames:
#     read_info(file)
# finish1 = time.time()
# print(finish1 - start1)

start2 = time.time()
if __name__ == "__main__":
    with Pool(4) as p:
        p.map(read_info, filenames)
    finish2 = time.time()
    print(finish2 - start2)
