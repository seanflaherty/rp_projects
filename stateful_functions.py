# stateful function
def cumulative_average():
    data = []
    def average(value):
        data.append(value)
        return sum(data) / len(data)
    return average

stream_average = cumulative_average()

print(stream_average(12))
print(stream_average(13))
print(stream_average(14))
print(stream_average(15))