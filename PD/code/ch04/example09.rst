.. list-table:: 对象协议
    :widths: 50 70
    :header-rows: 1

    * - 方法
      - 描述
    * - ``__new__(cls, [, *args, [,**kwargs]])``
      - 用于创建实例的静态方法
    * - ``__init__(self, [, *args, [,**kwargs]])``
      - 在新实例创建后，调用该函数来初始化实例     
    * - ``__del__(self)``
      - 在实例被销毁时调用
    * - ``__repr__(self)``
      - 创建字符串表示
