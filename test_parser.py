import pytest
from parser import table_data_list

popularity_thresholds = [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9]

# Функция для форматирования числа с разделением разрядов пробелами
def format_number(number):
    return f"{number:,}".replace(",", " ")

@pytest.mark.parametrize("popularity_threshold", popularity_thresholds)
def test_popularity_threshold(popularity_threshold):
    errors = []
    for data in table_data_list:
        popularity_str = data.popularity
        # Извлекаем числа из строки, учитывая всякие дополнительные символы, кроме цифр
        popularity_str = ''.join(filter(str.isdigit, popularity_str))
        popularity = int(popularity_str) if popularity_str else 0

        if popularity < popularity_threshold:
            formatted_popularity = format_number(popularity)
            formatted_threshold = format_number(popularity_threshold)
            error_message = (
                f"{data.website} (Frontend:{data.frontend}|Backend:{data.backend}) "
                f"has {formatted_popularity} unique visitors per month. "
                f"(Expected more than {formatted_threshold})"
            )
            errors.append(error_message)

    assert not errors, "Errors found in the table.\n" + "\n".join(errors)