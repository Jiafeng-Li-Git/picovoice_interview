
def prob_rain_more_than_n(prob_seq, n):

    if n == 0:
        result = 1
        for prob in prob_seq:
            result = result * (1-prob)
        return result

    if n == len(prob_seq):
        result = 1
        for prob in prob_seq:
            result = result * prob
        return result

    if n > len(prob_seq):
        return 0

    prob_first_day_rain = prob_seq[0]
    prob_without_first_day_seq = prob_seq[1:]
    prob_first_day_rain_least_n = prob_first_day_rain * prob_rain_more_than_n(prob_without_first_day_seq, n-1)
    prob_first_day_no_rain_least_n = (1 - prob_first_day_rain) * prob_rain_more_than_n(prob_without_first_day_seq,
                                                                                       n)

    prob_without_first_day_seq.clear()
    return prob_first_day_rain_least_n + prob_first_day_no_rain_least_n


test_list = [0] * 365
test_list[1] = 0.5
test_list[2] = 0.2
test_list[3] = 0.1
print(prob_rain_more_than_n(test_list, 3))