import math
import random
import pygame


class Vec2d:
    """ Класс вектора """
    def __init__(self, x, y):
        self._vector = (x, y)

    def __get__(self, instance, owner):  # получение значения вектора
        return self._vector

    def __getitem__(self, index):  # получение координаты вектора по индексу
        return self._vector[index]

    def __str__(self):  # переопеределение печати экземпляра класса
        return str(self._vector)

    def __add__(self, other):  # сумма двух векторов
        return Vec2d(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):  # разность двух векторов
        return Vec2d(self[0] - other[0], self[1] - other[1])

    def __mul__(self, other):  # умножение вектора на число и скалярное умножение векторов
        if isinstance(other, Vec2d):
            return Vec2d(self[0] * other[0], self[1] * other[1])
        else:
            return Vec2d(self[0] * other, self[1] * other)

    def __len__(self):  # длина вектора
        return int(math.sqrt(self[0]**2 + self[1]**2))

    def int_pair(self):  # получение пары (x, y)
        return self._vector


class Polyline:
    """ Класс замкнутых линий """
    def __init__(self):
        self._points = []
        self._speeds = []
        self._screen = (800, 600)

    def __len__(self):
        return len(self._points)

    def __get__(self, instance, owner):
        return self._points

    def __getitem__(self, index):
        return self._points[index]

    def add_point(self, point, speed):  # добавление в ломаную точки и ее скорости
        self._points.append(point)
        self._speeds.append(speed)

    def set_points(self):  # пересчет координат точек на скорость
        for i in range(len(self._points)):
            self._points[i] = self._points[i] + self._speeds[i]
            if self._points[i][0] > self._screen[0] or self._points[i][0] < 0:
                self._speeds[i] = Vec2d(- self._speeds[i][0], self._speeds[i][1])
            if self._points[i][1] > self._screen[1] or self._points[i][1] < 0:
                self._speeds[i] = Vec2d(self._speeds[i][0], - self._speeds[i][1])

    def draw_points(self, display, style="points", width=3, color=(255, 255, 255)):  # рисование точек и линий
        if style == "line":
            for i in range(-1, len(self._points) - 1):
                pygame.draw.line(display, color, (int(self._points[i][0]), int(self._points[i][1])),
                                 (int(self._points[i + 1][0]), int(self._points[i + 1][1])), width)
        elif style == "points":
            for i in self._points:
                pygame.draw.circle(display, color, (int(i[0]), int(i[1])), width)


class Knot(Polyline):
    """ Класс кривой """
    def __init__(self, count):
        super().__init__()
        self._count = count
        self._points_knot = []

    count = property()  # свойство количество точек сглаживания

    @count.setter
    def count(self, value):
        self._count -= value if self._count > 1 else 0

    @count.getter
    def count(self):
        return self._count

    def get_point(points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return add(mul(points[deg], alpha), mul(get_point(points, alpha, deg - 1), 1 - alpha))

    def get_points(base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(get_point(base_points, i * alpha))
        return res

    def get_knot(points, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append(mul(add(points[i], points[i + 1]), 0.5))
            ptn.append(points[i + 1])
            ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))

            res.extend(get_points(ptn, count))
        return res

    def draw_points(self, display, style="points", width=3, color=(255, 255, 255)):  # рисование точек и линий
        self._points_knot = self
        if style == "line":
            for i in range(-1, len(self._points_knot) - 1):
                pygame.draw.line(display, color, (int(self._points_knot[i][0]), int(self._points_knot[i][1])),
                                 (int(self._points_knot[i + 1][0]), int(self._points_knot[i + 1][1])), width)
        elif style == "points":
            for i in self:
                pygame.draw.circle(display, color, (int(i[0]), int(i[1])), width)



# Основная программа
if __name__ == "__main__":
    # инициализация окна
    pygame.init()
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("MyScreenSaver")

    # steps = 35  # количество точек сглаживания
    working = True  # маркер работы
    poly = Knot(35)
    # poly = Polyline()

    # show_help = False  # маркер отображения помощи
    pause = True  # маркер паузы

    hue = 0  # оттенок
    color_line = pygame.Color(0)  # цвет

    # цикл работы программы
    while working:
        # отлавливаем событие с клавиатуры и мышки
        for event in pygame.event.get():
            # если нажат крестик закрытия окна, меняем маркер работы программы
            if event.type == pygame.QUIT:
                working = False
            # отлавливаем событие с клавиатуры
            if event.type == pygame.KEYDOWN:
                # Esc - меняем маркер работы программы
                if event.key == pygame.K_ESCAPE:
                    working = False
                # R - обнуляем данные
                if event.key == pygame.K_r:
                    poly = Polyline()
                # P - меняем маркер движения
                if event.key == pygame.K_p:
                    pause = not pause
                # Num+ - увеличиваем количество точек сглаживания
                if event.key == pygame.K_KP_PLUS:
                    poly.count += 1
                    # steps += 1
                # F1 - открытие/закрытие окна помощи
                # if event.key == pygame.K_F1:
                    # show_help = not show_help
                # Num- - уменьшаем количество точек сглаживания
                if event.key == pygame.K_KP_MINUS:
                    poly.count -= 1
                    # steps -= 1 if steps > 1 else 0
            # отлавливаем событие с мыши - клик любой кнопкой - добавляем точку в
            # полилайн и генерируем скорость для этой точки
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_event = Vec2d(event.pos[0], event.pos[1])
                speed_event = Vec2d(random.random() * 2, random.random() * 2)
                poly.add_point(point_event, speed_event)

        # отрисовка окна
        gameDisplay.fill((0, 0, 0))  # заполняем окно черным цветом
        hue = (hue + 1) % 360  # меняем оттенок линии
        color_line.hsla = (hue, 100, 50, 100)  # формируем новый цвет с учетом нового оттенка
        poly.draw_points(gameDisplay)  # рисуем точки
        poly.draw_points(gameDisplay, "line", 3, color_line)  # рисуем линию
        # draw_points(get_knot(points, steps), "line", 3, color)
        # если стоит маркер движения - сдвигаем точки на скорость
        if not pause:
            poly.set_points()
        # если стоит маркер окна помощи - показываем окно помощи
        # if show_help:
        #    draw_help()

        pygame.display.flip()  # перерисовка окна

    # выход из программы
    pygame.display.quit()
    pygame.quit()
    exit(0)
