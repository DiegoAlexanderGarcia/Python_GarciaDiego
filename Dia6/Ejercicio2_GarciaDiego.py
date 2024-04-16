def two_sum(nums, target):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1

nums = list(map(int, input("Ingresa los números separados por espacios: ").split()))
target = int(input("Ingresa el objetivo: "))
print("Los índices de los dos números que suman al objetivo son:", two_sum(nums, target))