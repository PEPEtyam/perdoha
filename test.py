
def fibonachi(num):
    x0 = 0
    x1 = 1
    for i in range(num-2):
        result = x0 + x1
        print(f"Вывожу result: {result}, в {i}-ой итерации...")
        print(f"Вывожу x0 = {x0} до изменения значений...")
        print(f"Вывожу x1 = {x1} до изменения значений...")
        x0 = x1
        print(f"Вывожу x0 = {x0} после изменения значений...")
        x1 = result
        print(f"Вывожу x1 = {x1} после изменения значений...")
        print('\n')
    
    return result
        
        
    
    
input_value = int(input('Введите член последовательности Фибоначчи, который вы хотите унать...\n'))
                        
print(f"{input_value}-ый член последовательности: ", fibonachi(input_value))
input(...)                        