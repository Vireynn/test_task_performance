filepath = input(">> ")

with open(filepath, 'r') as f_obj:
    nums = [int(num.strip()) for num in f_obj.readlines()]

middle = sorted(nums)[len(nums) // 2]
print(sum(abs(num - middle) for num in nums))
