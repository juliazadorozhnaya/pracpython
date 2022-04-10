.. InGame documentation master file, created by
   sphinx-quickstart on Sun Apr 10 18:48:30 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to InGame's documentation!
==================================

.. toctree::
   :maxdepth: 4
   :caption: Main:


.. image:: _static/squid_game_logo.jpg

Game menu:
-------------

.. code-block:: python

   import pygame

   from ingame import InGame

   g = InGame()
   g.curr_menu.display_menu()
   pygame.quit()

Problem statement
-----------------

   * **InGame** game based on the series Squid Game.
   * To work with computer vision algorithms, you can use the package OpenCV_.
   * As a framework, it is planned to use PyGame_.


.. _OpenCV: https://pypi.org/project/opencv-python
.. _PyGame: https://pypi.org/project/pygame/



Project participants:
---------------------

    #. Задорожная Юлия Андреевна, группа 321, nick: Julia
    #. Чистякова Анна Сергеевна, группа 328, nick: wianluna

Link to repository:
-------------------

https://github.com/juliazadorozhnaya/InGame


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
