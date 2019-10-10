#!/usr/bin/env python3
import matplotlib.pyplot as plt


def vector_mean(v: list or tuple) -> float:
    return sum(v)/len(v)


def x_term(x: list or tuple, y: list or tuple) -> float:
    mx = vector_mean(x)
    my = vector_mean(y)
    numerator = denominator = 0.
    for xi, yi in zip(x, y):
        numerator += (xi - mx) * (yi - my)
        denominator += (xi - mx) ** 2
    return numerator / denominator


def b_term(x: list or tuple, y: list or tuple, b: float) -> float:
    return (sum(y) - (b * sum(x))) / len(x)


def least_squares_fit(x: list or tuple, y: list or tuple) -> (float, float):
    var_x = x_term(x, y)
    b = b_term(x, y, var_x)
    sign = '+'
    if b < 0:
        sign = ''
    print(f'Least Squares Eq.: y = {var_x}x {sign}{b}')
    return var_x, b


def main():

    x = [12, 30, 15, 24, 14, 18, 28, 26, 19, 27]
    y = [20, 60, 27, 50, 21, 30, 61, 54, 32, 57]

    var_x, b = least_squares_fit(x, y)

    y_samples, x_samples = [], []
    max_sample = int(max(x+y)) + 2
    min_sample = int(min(x+y)) - 2
    num_samples = range(min_sample, max_sample)
    for sample in num_samples:
        eq_result = var_x * sample + b
        if eq_result > max_sample:
            break
        y_samples.append(eq_result)
        x_samples.append(sample)

    plt.scatter(x, y)

    plt.plot(x_samples, y_samples, color='red', label='Linear Fit')
    plt.show()


if __name__ == '__main__':
    main()
