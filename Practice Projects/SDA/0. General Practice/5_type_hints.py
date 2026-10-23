def analyze_numbers(numbers: list[int]) -> dict[str, int|float]:
    nr_count = len(numbers)
    nr_sum = sum(numbers)
    nr_average =  nr_sum / nr_count

    return {
        "count": nr_count,
        "sum": nr_sum,
        "average": nr_average
    }


print(analyze_numbers([4, 8, 12, 16]))
