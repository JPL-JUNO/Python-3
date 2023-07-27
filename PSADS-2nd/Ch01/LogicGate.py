"""
@Description: 继承：逻辑门与电路
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-27 20:40:02
"""


class LogicGate:
    def __init__(self, n) -> None:
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        # 前还不用实现 performGateLogic 函数。
        # 原因在于，我们不知道每一种逻辑门将如何进行自己的逻辑运算。这些细节会交由继承层次结构中的每一个逻辑门来实现。
        # 这是一种在面向对象编程中非常强大的思想——我们创建了一个方法，而其代码还不存在。
        # 参数 self 是指向实际调用方法的逻辑门对象的引用。
        # 任何添加到继承层次结构中的新逻辑门都仅需要实现之后会被调用的 performGateLogic 函数。
        # 一旦实现完成，逻辑门就可以提供运算结果。
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    # 新添的行为就是获取两个输入值
    def get_pinA(self):
        if self.pinA is None:
            return int(input('Enter Pin A input for gate' + self.get_label() + ' --> '))
        else:
            return self.pinA.get_from().get_output()

    def get_pinB(self):
        return int(input('Enter Pin B input for gate' + self.get_label() + ' --> '))

    def setNextPin(self, source):
        if self.pinA is None:
            print(source)
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError('Error: No Empty Pins')


class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input('Enter Pin input for gate' + self.get_label() + ' --> '))
        else:
            return self.pin.get_from().get_output()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print('Cannot Connect: No Empty pins on this gate')


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a != 0 and b != 0:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin()
        if a != 0:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, f_gate, t_gate):
        self.from_gate = f_gate
        self.to_gate = t_gate
        t_gate.setNextPin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


if __name__ == "__main__":
    g1 = AndGate('G1')
    g2 = AndGate('G2')
    g3 = OrGate('G3')
    g4 = NotGate('G4')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
