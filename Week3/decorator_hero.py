from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        super().__init__()
        self.base = base

    @abstractmethod
    def get_stats(self):
        pass

    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        res_pos = self.base.get_positive_effects()
        res_pos.append(self.__class__.__name__)
        return res_pos

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        res_stats = self.base.get_stats()
        res_stats["Strength"] +=7
        res_stats["Endurance"] += 7
        res_stats["Agility"] += 7
        res_stats["Luck"] += 7
        res_stats["Perception"] -=3
        res_stats["Charisma"] -= 3
        res_stats["Intelligence"] -= 3
        res_stats["HP"] +=50
        return res_stats


class Blessing(AbstractPositive):
    def get_stats(self):
        res_stats = self.base.get_stats()
        res_stats["Strength"] += 2
        res_stats["Perception"] += 2
        res_stats["Endurance"] += 2
        res_stats["Charisma"] += 2
        res_stats["Intelligence"] += 2
        res_stats["Agility"] += 2
        res_stats["Luck"] += 2
        return res_stats


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        res_neg = self.base.get_negative_effects()
        res_neg.append(self.__class__.__name__)
        return res_neg


class Weakness(AbstractNegative):
    def get_stats(self):
        res_stats = self.base.get_stats()
        res_stats["Strength"] -= 4
        res_stats["Endurance"] -= 4
        res_stats["Agility"] -= 4
        return res_stats


class Curse(AbstractNegative):
    def get_stats(self):
        res_stats = self.base.get_stats()
        res_stats["Strength"] -= 2
        res_stats["Perception"] -= 2
        res_stats["Endurance"] -= 2
        res_stats["Charisma"] -= 2
        res_stats["Intelligence"] -= 2
        res_stats["Agility"] -= 2
        res_stats["Luck"] -= 2
        return res_stats


class EvilEye(AbstractNegative):
    def get_stats(self):
        res_stats = self.base.get_stats()
        res_stats["Luck"] -=10
        return res_stats


if __name__ == "__main__":
    hero = Hero()
    hero = Berserk(hero)
    print(hero.get_positive_effects())
    hero = Curse(hero)
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())
    hero = Berserk(hero)
    print(hero.get_positive_effects())
    hero.base = Hero()
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())