# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: observer
# Author: xiaxu
# DATA: 2023/10/8
# Description:
# ---------------------------------------------------
"""
http://code.activestate.com/recipes/131499-observer-pattern/

*TL;DR
Maintains a list of dependents and notifies them of any state changes.

*Examples in Python ecosystem:
Django Signals: https://docs.djangoproject.com/en/3.1/topics/signals/
Flask Signals: https://flask.palletsprojects.com/en/1.1.x/signals/
"""

from __future__ import annotations

from contextlib import suppress
from typing import Protocol


# 定义观察者基类
class Observer(Protocol):
    def update(self, subject: Subject) -> None:
        pass


# 观察目标的基类
class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    #添加观察者
    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    # 删除观察者
    def detach(self, observer: Observer) -> None:
        with suppress(ValueError):
            self._observers.remove(observer)

    # 通知观察者更新
    def notify(self, modifier: Observer | None = None) -> None:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# 具体观察目标
class Data(Subject):
    def __init__(self, name: str = "") -> None:
        super().__init__()
        self.name = name
        self._data = 0

    # 属性装饰器，装饰后可以通过0bj.data获取
    @property
    def data(self) -> int:
        return self._data

    #方法设置
    @data.setter
    def data(self, value: int) -> None:
        self._data = value
        self.notify()


# 具体观察者（泛化关系）
class HexViewer(Observer):
    def update(self, subject: Data) -> None:
        print(f"HexViewer: Subject {subject.name} has data 0x{subject.data:x}") # :x表示为16进制表示


class DecimalViewer(Observer):
    def update(self, subject: Data) -> None:
        print(f"DecimalViewer: Subject {subject.name} has data {subject.data}")

if __name__ == '__main__':

    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)
    data1.data = 10
    data2.data = 15
    data1.data = 3
    data2.data = 5
    data1.detach(view2)
    data2.detach(view2)
    data1.data = 10
    data2.data = 15
