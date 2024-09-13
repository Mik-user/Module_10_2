
from threading import Thread
import time



class Knight(Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        battle_time = 0
        while enemy > 0:
            time.sleep(1)
            battle_time += 1
            enemy -=self.power
            if enemy < 0:
                enemy = 0
            print(f'{self.name} сражается {battle_time} день(дня). Осталось еще {enemy} врагов!')
        print(f'{self.name} одержал победу за {battle_time} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились')