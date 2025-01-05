"""Модуль для работы с повареной книгой"""

from pprint import pprint

def read_cookbook(file_directory: str) -> dict:
    """
    Функция, которая на основе файла с относительным путем file_directory
    собирает словарь из блюд, ключи которого - это имена блюд, а значения - 
    это список словарей ингредиентов. Каждый словарь ингредиентов отображает 
    нужное количество этого ингредиента для блюда, его название и единицу 
    измерения.
    :param file_directory: [str] - путь к файлу с повареной книгой
    :result: [dict] - словарь, повареная книга
    """
    try:
        recipes = {}
        with open(file_directory, encoding='utf-8') as file:
            while True:
                curr_name = file.readline().strip()
                if not curr_name:
                    break
                curr_ingredients_count = int(file.readline().strip())
                curr_ingredients_list = []
                for _ in range(curr_ingredients_count):
                    item, quantity, measure = file.readline().\
                        strip().split(" | ")
                    curr_ingredients_list.append({
                        "ingredient_name": item,
                        "measure": measure, 
                        "quantity": int(quantity),
                    })
                recipes[curr_name] = curr_ingredients_list
                file.readline()
        return recipes
    except FileNotFoundError as exp:
        raise FileNotFoundError("Неправильный путь к файлу") from exp

def get_shop_list_by_dishes(dishes: list[str], person_count: int, book: dict) -> dict:
    """
    Функция, которая считает нужное количество ингредиентов, для того, чтобы
    приготовить все блюда из списка dishes с ингредиентами, известными в
    кулинарной книге book для количества гостей: person_count.
    :param dishes: [list] - список названий блюд
    :param person_count: [int] - число порций
    :param book: - [dict] кулинарная книга
    :result: [dict] - словарь, состоящий из ингредиентов в нужном количестве
    """
    ingredient_dict = {}
    for dish in dishes:  # перебираем блюда
        if dish not in book:  # проверяем наличие блюда в книге
            raise ValueError(f"Блюда {dish} нет в кулинарной книге")

        for item in book[dish]:  # перебираем ингредиенты этого блюда
            if item['ingredient_name'] not in ingredient_dict:
                ingredient_dict[item['ingredient_name']] = {  # устанавливаем
                    'measure': item['measure'],  # значение словаря по умолч.
                    'quantity': 0,
                    }
            ingredient_dict[item['ingredient_name']]['quantity'] += (
                                            item['quantity'] * person_count)
    return ingredient_dict

def main():
    """Функция для тестирования работы с кулинарной книгой"""
    file_path = "recipes.txt"  # можно изменить
    cookbook = read_cookbook(file_path)
    pprint(cookbook)  # задание №1
    print()
    final_ingredients = get_shop_list_by_dishes(
        ['Запеченный картофель', 'Омлет'],
        2,
        cookbook)
    pprint(final_ingredients)  # задание №2

if __name__ == "__main__":
    main()
