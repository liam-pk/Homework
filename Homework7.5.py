def sumexclude(data):
    "Sum all the elements in a list up to but not including the first even number."
    count = 0
    for i in data:
        if i % 2 == 0:
            break
        count += i
    return count