import numpy as np

def num_rand_game(low = 1, high = 101) -> int:
    """Сначала устанавливаем границы рандом числа (по дефолту от 1 до 100 включительно), а потом уменьшаем
    границы диапозона поиска в зависимости от того, больше наше число или меньше нужного.
       Функция принимает диапозон рандомного числа и возвращает число попыток
       
    Args:
        low (int, optional): Нижний порог рандомного числа. Defaults to 1.
        high (int, optional): Верхний порог рандомного числа. Defaults to 101.

    Returns:
        int: Число попыток
    """
    
    number = np.random.randint(low, high)
    count = 0

    while True:
        predict = (low + high) // 2 # Делим диапозон числа пополам и делаем вывод: больше или меньше искомого
        count += 1
        if count > 50: break # Добавим запасной выход из цикла в случае зацикливания

        if predict == number:
            break
        elif predict < number:
            # Если наше число меньше искомого, меняем  нижний диапозон на наше число +1
            low = predict + 1
        else:
            # Если наше число больше искомого, меняем  верхний диапозон на наше число -1
            high = predict - 1
    return count
            

# print(num_rand_game())


def score_game(num_rand_game) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        num_rand_game ([type]): функция угадывания рандомного числа

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(num_rand_game(number))

    score = int(np.mean(count_ls))
    return score

print(f"Ваш алгоритм угадывает число в среднем за: {score_game(num_rand_game)} попыток")