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