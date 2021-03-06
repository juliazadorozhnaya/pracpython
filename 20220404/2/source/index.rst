.. MUD documentation master file, created by
   sphinx-quickstart on Sun Apr 10 21:10:51 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MUD's documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   MUDdoc.rst

The task:
---------

* Имеется поле 10х10 клеток (по каждой оси нумерация с 0 по 9)
* В каждой клетке может находиться 0 или более монстров, у каждого монстра есть имя и число очков здоровья (hp - hit points)
* По полю ходит игрок; попав на клетку с монстром, он может его атаковать, нанося урон (списывая очки здоровья)
* В начале игры игрок появляется в случайной клетке (0, 0)
* Клетка с координатами (0, 0) находится в левом верхнем углу поля
* Настройка поля и игровой процесс организованы при помощи командной строки (readline/shlex/cmd):

* add monster name <имя монстра> hp <число очков здоровья> coords <X> <Y>
   * Добавить в клетку с заданными координатами монстра с заданным именем и числом очков здоровья
   * Если в этой клетке уже есть монстр с таким именем, его число очков здоровья меняется на новое
   * Пример: add monster name Gnoll hp 23 coords 5 7

* show monsters
   * Вывести про каждого монстра на отдельной строке информацию: его имя, координаты, число очков здоровья
   * Пример: War Troll at (4 2) hp 100

* move <направление>

   * Подвинуть игрока на одну клетку в заданном направлении (варианты: up, down, left, right), если это возможно с учетом границ поля; up, down - смещение по оси Y; left, right - по оси X
   * Пример: move up
   * После подвижки (т.е. успешного изменения позиции) вывести информацию о новой позиции, например\: player at 6 9; если подвижка невозможна, вывести\: cannot move
   * Если после подвижки игрок попал на клетку с монстром, вывести информацию о монстре (монстрах) в этой клетке, например\: encountered\: War Troll 57 hp, Lizardman 13 hp

* attack <имя монстра>
   * Атаковать монстра с заданным именем, находящегося в той же клетке, где игрок.
   * Атака списывает у монстра 10 очков здоровья; по результатам выводится сообщение.
   * Монстр, у которого в результате атаки осталось 0 или менее очков здоровья, исчезает.
   * Если монстра с заданными именем нет в клетке с игроком, выводится сообщение: no <имя монстра> here


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
