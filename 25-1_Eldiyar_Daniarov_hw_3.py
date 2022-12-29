class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, value):
        self.__cpu = value

    def get_memory(self):
        return self.__memory

    def set_memory(self, value):
        self.__memory = value

    def make_computetions(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f'CPU : {self.__cpu}, memory: {self.__memory}'


    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            return f'Идет звонок на номер {call_to_number} c сим-карты - {sim_card_number} - ' \
                   f'{self.__sim_cards_list[sim_card_number - 1]}'
        else:
            return 'Сим-карты под таким номером нету!'

    def __str__(self):
        return f'Симкарты: {self.__sim_cards_list}'


class SmartPnone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)


    def use_qps(self, location):
        return f'Путь от вашего местоположения до {location} проложен!'

    def __str__(self):
        return f'CPU: {self.get_cpu()}, memory: {self.get_memory()}, sim cards: {self.get_sim_cards_list()}'



some_comp = [Computer(16, 512), Phone(['O!', 'Beeline', 'Megacome']),
             SmartPnone(6, 128, ['O!', 'Beeline', 'Megacome']), SmartPnone(8, 256, ['O!', 'Beeline', 'Megacome'])]
for i in some_comp:
    print(i)

comp = Computer(16, 256)
some_phone = Phone( ['O!', 'Beeline', 'Megacome'])
some_smart = SmartPnone(8, 256,  ['O!', 'Beeline', 'Megacome'])
print(some_smart > comp)
print(some_smart < comp)
print(some_smart >= comp)
print(some_smart <= comp)
print(some_smart == comp)
print(some_smart != comp)
print(comp.get_cpu())
print(comp.set_cpu(8))
print(comp.make_computetions())
print(comp.set_memory(256))
print(comp.get_cpu())
print(some_phone.call(2, +996508808980))
print(some_phone.get_sim_cards_list())
print(some_phone.set_sim_cards_list(['mts']))
print(some_smart.use_qps('GeekTech'))



