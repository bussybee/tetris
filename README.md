Задача 5. Логические игры

В задаче обязательно реализовать логику игры в виде отдельного класса Game.

Оформление игры может быть максимально простым (допустим, не надо плавных перемещений шариков с клетки на клетку, каких-либо визуальных эффектов, звукового сопровождения и т.п.). Элементы – просто цветные кружки / кубики / обычные цифры и т.д. в зависимости от варианта. Выделение элемента (если нужно) – изменение цвета фона ячеек игрового поля. (В любом случае все это не относится к логике игры.)

Для большинства игр никаких уровней (для некоторых игр можно сделать 1-2 уровня, которые описываются в отдельных файлах) и т.д.

Оконный интерфейс должен быть реализован c помощью библиотеки PyQt5. Кроме главной формы необходимо предусмотреть, как минимум, еще две формы: 1) форму с возможностью задания настроек игры (например, размеры игрового поля, используемые цвета и т.п.), 2) форму с описанием правил игры (описание может быть в виде html).

Во многих играх, приведенных в вариантах задач в виде примера, кроме центральной идеи, есть различные, так скажем, расширения-исключения. Вот этого всего реализовывать также не надо.

Обязательным является использование @property, @staticmethod/@classmethod (в данной задаче, вероятно, все же @staticmethod).

Для просмотра FLASH-игр (задачи с 6 по 25) необходимо FLASH-плеер (ссылка ↓ниже↓ для Windows, Macintosh или Linux).
С помощью данного Flash-плеера можно открыть нужный SWF-файл из каталога.

Вариант 2: Классический тетрис. 