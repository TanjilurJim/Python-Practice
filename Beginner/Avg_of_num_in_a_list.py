def av_of_numbers(li):
    summation = 0
    for i in li:
        summation +=i

    avg = summation / len(li)
    return avg

list = [10,20,30,40,50]
result = av_of_numbers(list)

print(result)
