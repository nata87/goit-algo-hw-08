import heapq

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

def min_cost(cables, step=1, total_cost=0):
    if not cables or len(cables) == 1:
        return total_cost

    cabl_sorted = heap_sort(cables)
    a, b = cabl_sorted[0], cabl_sorted[1]
    cost = a + b
    new_cables = cabl_sorted[2:]
    new_cables.append(cost)

    print(f" Крок {step}:")
    print(f" Поточні кабелі: {cabl_sorted}")
    print(f" З'єднуємо {a} + {b} = {cost}")
    print(f" Новий список кабелів: {new_cables}")
    print(f" Накопичена вартість: {total_cost + cost}\n")

    return min_cost(new_cables, step + 1, total_cost + cost)

if __name__ == "__main__":
    cables = [5, 6, 7, 8, 9, 10]
    print(" Початкові кабелі:", cables)
    total = min_cost(cables)
    print(f" Загальні мінімальні витрати: {total}")
