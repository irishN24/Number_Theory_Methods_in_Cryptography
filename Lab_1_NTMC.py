def fast_square(x, b=10):
    """
    Быстрое возведение числа в квадрат по алгоритму из текста.
    
    Параметры:
    x: число в виде списка цифр в системе счисления с основанием b.
       Например, x = [x_{n-1}, ..., x_0] (старший разряд слева).
    b: основание системы счисления (по умолчанию 10).
    
    Возвращает:
    Список цифр результата y = x^2 в той же системе счисления.
    """
    n = len(x)
    # Длина результата может быть до 2n
    y = [0] * (2 * n)  # шаг 1: инициализация
    
    for i in range(n):
        # шаг 2.1: квадрат xi
        val = y[2 * i] + x[i] * x[i]
        y[2 * i] = val % b
        carry = val // b  # перенос (c в алгоритме)
        
        for j in range(i + 1, n):
            # шаг 2.2: перекрёстные члены 2 * xi * xj
            # добавляем к y[i+j] текущий перенос и 2*xi*xj
            val = y[i + j] + 2 * x[i] * x[j] + carry
            y[i + j] = val % b
            carry = val // b
        
        # шаг 2.3: сохраняем оставшийся перенос в следующий разряд
        # на последней итерации i = n-1 это даст y[2n-1] и, возможно, y[2n]
        if carry > 0:
            # нужно расширить результат
            if i + n < len(y):
                y[i + n] += carry
            else:
                y.append(carry)
    
    # Убираем ведущие нули для красоты
    while len(y) > 1 and y[-1] == 0:
        y.pop()
    
    return y[::-1]  # возвращаем в порядке старший разряд слева

def number_to_digits(num, base=10):
    """Преобразует целое число в список цифр в заданной системе счисления."""
    if num == 0:
        return [0]
    digits = []
    while num > 0:
        digits.append(num % base)
        num //= base
    return digits[::-1]

def digits_to_number(digits, base=10):
    """Преобразует список цифр в целое число."""
    num = 0
    for d in digits:
        num = num * base + d
    return num

# Пример использования
if __name__ == "__main__":
    # Тестовое число в десятичной системе
    original = 1234
    b = 10
    
    # Представляем число в виде цифр в системе счисления b
    x_digits = number_to_digits(original, b)
    print(f"Исходное число: {original}")
    print(f"Цифры числа (по основанию {b}): {x_digits}")
    
    # Вычисляем квадрат по алгоритму
    result_digits = fast_square(x_digits, b)
    result_num = digits_to_number(result_digits, b)
    
    print(f"Квадрат по алгоритму: {result_num}")
    print(f"Проверка: {original}^2 = {original**2}")
    
    # Тест с двоичной системой
    print("\n" + "="*40)
    b2 = 2
    x_bin = [1, 1, 0, 1]  # число 13 в двоичной (1101)
    original_bin = digits_to_number(x_bin, b2)
    result_bin_digits = fast_square(x_bin, b2)
    result_bin = digits_to_number(result_bin_digits, b2)
    
    print(f"Двоичное число: {x_bin} = {original_bin}")
    print(f"Квадрат в двоичной: {result_bin_digits} = {result_bin}")
    print(f"Проверка: {original_bin}^2 = {original_bin**2}")