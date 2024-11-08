## Project_pi
Этот проект реализует вычисления n-го знака после запятой числа Пи

## Использование
1. Откройте любой среду разработки к примеру PyCharm
2. Установите библиотеку mpmath командой pip install mpmath
3. Скопируйте и вставьте следующий код в main.py:
```python
from mpmath import mp

def calculate_pi_mpmath(n):
    mp.dps = n + 2
    return str(mp.pi)
while True:
    try:
        n = int(input("Введите количество знаков после запятой для числа π: "))
        break
    except ValueError:
        pass
pi_value = calculate_pi_mpmath(n)
print(f"Число π до {n}-го знака после запятой: {pi_value}")
```
4. Запустите код
5. Введите количество знаков после запятой для числа π
6. После вычисления будет выведен результат
7. Ограничения В мощности железа число пи до 1 трлн знаков после запятой будет проблематично рассчитать Чем больше знаков после запятой, тем дольше будет вывод