# This is a sample Python script.
from herd import Herd
from fleet import Fleet
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fleet = Fleet()
    fleet.create_fleet()
    herd = Herd()
    herd.create_herd()

print('Game Over')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
