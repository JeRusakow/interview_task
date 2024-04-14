"""
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Оценивается:
- Полнота и качество реализации
- Оформление кода
- Наличие сравнения и пояснения по быстродействию
"""
from collections import deque
from typing import Any


class CyclicBuffer1:

    def __init__(self, buf_size: int):
        if buf_size < 1:
            raise ValueError("Buffer size cannot be less than 1!")

        self._data = [None for _ in range(0, buf_size)]
        self.size = buf_size
        self._head_ptr = 0
        self._tail_ptr = 0
        self._obj_count = 0

    def push(self, obj: Any):
        if self.is_full():
            raise ValueError("Buffer is full!")

        self._data[self._head_ptr] = obj
        self._obj_count += 1
        self._head_ptr += 1
        if self._head_ptr == self.size:
            self._head_ptr = 0

    def pop(self) -> Any:
        if self.is_empty():
            return None

        obj = self._data[self._tail_ptr]
        self._obj_count -= 1
        self._tail_ptr += 1
        if self._tail_ptr == self.size:
            self._tail_ptr = 0
        return obj

    def is_full(self) -> bool:
        return self._obj_count == self.size

    def is_empty(self) -> bool:
        return self._obj_count == 0


class CyclicBuffer2:

    def __init__(self, buf_size: int):
        if buf_size < 1:
            raise ValueError("Buffer size cannot be less than 1!")

        self._data = {i: None for i in range(0, buf_size)}
        self.size = buf_size
        self._head_ptr = 0
        self._tail_ptr = 0
        self._obj_count = 0

    def push(self, obj: Any):
        if self.is_full():
            raise ValueError("Buffer is full!")

        self._data[self._head_ptr] = obj
        self._obj_count += 1
        self._head_ptr += 1
        if self._head_ptr == self.size:
            self._head_ptr = 0

    def pop(self) -> Any:
        if self.is_empty():
            return None

        obj = self._data[self._tail_ptr]
        self._obj_count -= 1
        self._tail_ptr += 1
        if self._tail_ptr == self.size:
            self._tail_ptr = 0
        return obj

    def is_full(self) -> bool:
        return self._obj_count == self.size

    def is_empty(self) -> bool:
        return self._obj_count == 0


class CyclicBuffer3:
    def __init__(self, buf_size: int):
        self._data = deque(maxlen=buf_size)
        self.size = buf_size

    def push(self, obj: Any):
        if self.is_full():
            raise ValueError("Buffer size cannot be less than 1!")
        self._data.append(obj)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.popleft()

    def is_full(self):
        return len(self._data) == self.size

    def is_empty(self):
        return len(self._data) == 0


"""
Представляю две реализации циклического FIFO-буфера. 
Первая - простая, straightforward реализация. В качестве хранилища данных используется простой список с двумя индексами 
головы, куда идёт запись, и хвоста, откуда идёт чтение.
Реализация поддерживает, помимо добавление и удаления объектов, проверка пустоты и заполненности буфера.

Отличие второй от первой - использование в качестве хранилища данных словарь, вместо списка. Согласно документации 
получение элемента из словаря может быть дольше, чем из списка (O(n) VS O(1)).

Третья реализация предлагает использование как хранилища двунапревленного списка с фиксированной длиной. Она проще для 
реализации и использует меньше явных переменных. Что касается алгоритмической сложности, получение элементов из дэка и 
сохранение их в него имеют сложность O(1).  Поэтому она мне нравится больше двух прочих. 
"""
