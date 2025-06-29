import numpy as np
from typing import List, Dict, Union


def calculate_quartiles(data: List[Union[int, float]]) -> Dict[str, float]:
    """
    Вычисляет квартили для заданного набора данных.

    Аргументы:
        data (list): Список чисел (int или float) для анализа.
                     Не требуется предварительной сортировки.

    Возвращает:
        dict: Словарь с ключами 'Q1', 'Q2', 'Q3', содержащий значения:
              - Q1 (первый квартиль, 25-й перцентиль)
              - Q2 (медиана, 50-й перцентиль)
              - Q3 (третий квартиль, 75-й перцентиль)

    Исключения:
        ValueError: Если входной список пустой.

    Пример:
        >>> calculate_quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9])
        {'Q1': 3.0, 'Q2': 5.0, 'Q3': 7.0}
    """
    if not data:
        raise ValueError("Входной список данных пуст")

    # Преобразуем в numpy массив для удобных вычислений
    data_array = np.array(data)
    
    # Используем numpy.percentile для точного расчета квартилей
    q1 = float(np.percentile(data_array, 25))
    q2 = float(np.percentile(data_array, 50))  # Медиана
    q3 = float(np.percentile(data_array, 75))
    
    return {'Q1': q1, 'Q2': q2, 'Q3': q3}
