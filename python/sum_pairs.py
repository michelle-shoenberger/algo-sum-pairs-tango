def sum_pairs(numbers, total):
    result = []
    # Check for wrong input type
    if not isinstance(numbers, list):
        return "Not a list"
    elif not (isinstance(total, int) or isinstance(total, float)):
        return "Not a number"
    numsdict = {}
    for num in numbers:
        if (total - num) in numsdict:
          result.append([total - num, num])
        numsdict[num] = numsdict[num] + 1 if num in numsdict else 1
    if result == []:
        return "Unable to find pairs"
    return result