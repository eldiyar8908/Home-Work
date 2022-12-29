amount_regions = 7
talas = float(input('Укажите темпиратуру в Таласе : ')) #переменное
isyk_kul = float(input('Укажите темпиратуру в Иссык-Куле : ')) #переменное
naryn = float(input('Укажите темпиратуру в Нарыне : ')) #переменное
osh = float(input('Укажите темпиратуру в Оше : ')) #переменное
jalal_abad = float(input('Укажите темпиратуру в Джалал-Абаде : ')) #переменное
batken = float(input('Укажите темпиратуру в Баткене: ')) #переменное
chuy = float(input('Укажите темпиратуру в Чуе : ')) #переменное
sum_of_area_temperatures = (talas + isyk_kul + naryn + osh + jalal_abad + batken + chuy)
ans = round(sum_of_area_temperatures/amount_regions, 1)
print('Средний показатель температуры воздуха по КР на сегодня', ans,'°C' )