from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    SAVE_OTHERS = 5
    SAVE_SOMEONE = 6
    HELP_HEROES = 7
    HACK_BOSS = 8
    VIRUS_OR_HEAL = 9
    YES_OR_NO = 10

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        if hero.health <= 0:
            self.choose_defence(heroes)
        else:
            self.__defence = hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            raise ValueError("Ability must be of type SuperAbility")
        else:
            self.__super_ability = super_ability

    def hit(self, boss):
        boss.health = boss.health - self.damage

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeffient = randint(2, 5)
        boss.health = boss.health - self.damage * coeffient
        print(f'Warrior hits critically: {self.damage * coeffient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        cef = randint(1,15)
        for hero in heroes:
            hero.damage = hero.damage + cef


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health = hero.health + self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damaged = 0

    def apply_super_power(self, boss, heroes):
        pass


class Witcher(Hero):
    def __init__(self, name, health, damage = 0):
        super().__init__(name, health, damage, SuperAbility.SAVE_SOMEONE)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0:
                hero.health = hero.health + self.health
                self.health = 0
                break


class AntMan(Hero):
    a = 1
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.HELP_HEROES)
    def apply_super_power(self, boss, heroes):
        self.health = round(self.health / self.a)
        self.damage = round(self.damage / self.a)
        coeffient = randint(1, 4)
        self.health = self.health * coeffient
        self.damage = self.damage * coeffient
        self.a = coeffient


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.HACK_BOSS)
    def apply_super_power(self, boss, heroes):
        a = self.damage
        self.health += a
        b = 0
        cef = randint(0, 300)
        boss.health = boss.health - cef
        for hero in heroes:
            hero.health += cef
            break


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.VIRUS_OR_HEAL)

    def apply_super_power(self, boss, heroes):
        suriken = randint(3, 4)
        if suriken % 3 == 0:
            boss.health += self.damage
            boss.health += 100




round_counter = 0


def print_statistics(boss, heroes):
    print('ROUND ' + str(round_counter) + ' -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0 and boss.health > 0:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Rashan', 1000, 50)
    warrior = Warrior('Konor', 280, 10)
    doc = Medic('Hous', 250, 5, 15)
    berserk = Berserk('Hiccup', 200, 15)
    magic = Magic('Invoker', 270, 20)
    assistant = Medic('Morty', 290, 5, 5)
    witcher = Witcher('Best', 300)
    ant_man = AntMan('strong', 250, 10)
    hacker = Hacker('Lux', 250, 15)
    samurai = Samurai('Oda Nobunaga', 260, 15)

    heroes = [warrior, doc, berserk, magic, assistant, witcher, ant_man, hacker, samurai]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()