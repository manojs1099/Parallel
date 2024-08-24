import multiprocessing

def calculate_partial_sum(arr_slice):
    return sum(arr_slice)

if __name__ == "__main__":
    N = int(input("Enter the size of the array: "))
    num_processes = multiprocessing.cpu_count()
    array = [i + 1 for i in range(N)]
    chunk_size = N // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        partial_sums = pool.map(calculate_partial_sum, [array[i:i + chunk_size] for i in range(0, N, chunk_size)])

    total_sum = sum(partial_sums)
    print(f"Sum of array: {total_sum}")