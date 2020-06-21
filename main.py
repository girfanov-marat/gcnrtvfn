from typing import Any
import itertools
import pprint


class TooMuchParametersException(Exception):
    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


negative = {
    "атмосфера": ["кислородосодержащая", "отсутствует"],
    "размер": ["карлик", "средний", "великан"],
    "населённость": ["растения", "существа", "разумные существа", "нет"],
    "температура": ["низкая", "средняя", "выскоая"],
    "посещалась ранее": ["да", "нет"]
}

positive = {
    "атмосфера": ["кислородосодержащая", "отсутствует"],
    "размер": ["карлик", "великан"],
    "температура": ["низкая", "средняя", "выскоая"],
    "посещалась ранее": ["да", "нет"]
}


def calculate(options: dict) -> list:
    variables = list()
    final_result = list()

    # Перебираем все пары ключ значение
    for key in options:
        combination = list(itertools.product([key], options.get(key)))
        for i in range(len(combination)):
            new_key = combination[i][0]
            new_value = combination[i][1]
            variables.append({new_key: new_value})

    # записываем в переменную result все возможные комбинации длинной, равной количеству ключей
    result = list(itertools.combinations(variables, len(options.keys())))
    intermediate_result = result.copy()

    # удаляем те комбинации, в которых ключи повторяются
    for i in range(len(result)):
        all_key = list()
        for j in range(len(result[i])):
            for key in result[i][j]:
                all_key.append(key)
        for k in all_key:
            if all_key.count(k) != 1:
                intermediate_result.remove(result[i])
                break

    # создаем список из окончательных вариантов
    for i in range(len(intermediate_result)):
        final_dict = dict()
        for j in range(len(intermediate_result[i])):
            final_dict.update(intermediate_result[i][j])
        final_result.append(final_dict)

    # вызываем исключение если количество возможных вариантов больше 100
    if len(final_result) > 100:
        raise TooMuchParametersException("Слишком большое количество параметров")
    return final_result


pprint.pprint(calculate(positive))

try:
    pprint.pprint(calculate(negative))
except TooMuchParametersException:
    print('Сликшом много параметров')
