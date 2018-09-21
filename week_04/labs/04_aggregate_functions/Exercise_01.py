'''
Build a simple aggregator function.

'''
def sum(nums):
    total = 0
    for each in nums:
        total += each
    return(total)

def concat(strs: list) -> str:
    out = ""
    for each in strs:
        out += each
    return(out)

print(sum([1, 2, 7, 4, 5, 6]))

print(concat(["a", "b", "q"]))
