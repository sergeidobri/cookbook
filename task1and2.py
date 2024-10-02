def read_cookbook(file_directory: str) -> dict:
    """
    Функция, которая на основе файла с относительным путем file_directory
    собирает словарь из блюд, ключи которого - это имена блюд, а значения - 
    это список словарей ингредиентов. Каждый словарь ингредиентов отображает 
    нужное количество этого ингредиента для блюда, его название и единицу 
    измерения.
    """
    try:
        with open(file_directory) as file:
            index = 0
            lines = file.readlines()
            recepies = {}

            while index < len(lines):
                curr_name = lines[index].strip()
                curr_ingredients_count = int(lines[index+1].strip())
                curr_ingredients_list = []
                for i in range(curr_ingredients_count):
                    item, quantity, measure = lines[index+2+i].strip().split(" | ")
                    curr_ingredients_list.append({
                        "ingredient_name": item,
                        "measure": measure, 
                        "quantity": int(quantity),
                        })
                
                recepies[curr_name] = curr_ingredients_list
                index += curr_ingredients_count + 3
            return recepies
    except FileNotFoundError:
        print('Ваш файл не был найден. Измените значение file_path в main()')
        return -1

def get_shop_list_by_dishes(dishes: list[str], person_count: int, book: dict) -> dict:
    """
    Функция, которая считает нужное количество ингредиентов, для того, чтобы
    приготовить все блюда из списка dishes с ингредиентами, известными в
    кулинарной книге book для количества гостей: person_count.
    """
    ingredient_dict = {}
    for dish in dishes:  # перебираем блюда
        if dish not in book:  # проверяем наличие блюда в книге
            return "Возникла ошибка"
        
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
    file_path = "C:\\Users\\newak\\OneDrive\\Desktop\\e-books\\\
it-science\\netology\\OOP\\recepies.txt"  # можно изменить
    cookbook = read_cookbook(file_path)
    if cookbook == -1:
        return 0
    print(cookbook)  # задание №1
    final_ingredients = get_shop_list_by_dishes(
        ['Запеченный картофель', 'Омлет'], 
        2, 
        cookbook,
        )
    print(final_ingredients)  # задание №2

if __name__ == "__main__":
    main()
    