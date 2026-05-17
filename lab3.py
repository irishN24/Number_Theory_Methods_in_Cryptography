#Алгоритм Баретта
import time

def barret_algorithm(x: int, m: int, z: int, b: int, k: int) -> int:
    if b <= 3 or m <= 0 or len(str(x)) > 2 * k:
        print("Ошибка")
        return -1  

    b_1 = b ** (k + 1) # b ^ k+1
    #приближенное частное
    approximate_q = ((x // b ** (k - 1)) * z) // b_1

    #остаток
    r_sub = (x - (approximate_q * m)) % b_1

    # Корректируем r_sub, если он больше diviser
    while r_sub >= m:
        r_sub -= m

    return r_sub

def get_positive_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Пожалуйста, введите положительное число.")
            else:
                return value
        except ValueError:
            print("Пожалуйста, введите целое число.")

def main():
    x = get_positive_integer_input("Введите число: ")
    m = 0
    while m == 0:
        m = get_positive_integer_input("Введите делитель: ")

    k = len(str(m))
    b = 10
    z = pow(b, 2 * k) // m

    # Измерение времени для встроенной операции %
    time_builtin_start = time.time()
    builtin_mod_result = x % m
    time_builtin_finish = time.time()
    time_builtin_result = time_builtin_finish - time_builtin_start

    # Измерение времени для алгоритма Баррета
    time_barret_start = time.time()
    barret_algorithm_mod_result = barret_algorithm(x, m, z, b, m)
    if barret_algorithm_mod_result == -1:
        return 0
    time_barret_finish = time.time()
    time_barret_result = time_barret_finish - time_barret_start

    print(f"\nРезультаты вычислений:")
    print(f"{x} mod {m} = {builtin_mod_result} (Встроенная функция '%'). Время: {time_builtin_result:.6f} секунд")
    print(f"{x} mod {m} = {barret_algorithm_mod_result} (Алгоритм Баррета). Время: {time_barret_result:.6f} секунд")

if __name__ == "__main__":
    main()
