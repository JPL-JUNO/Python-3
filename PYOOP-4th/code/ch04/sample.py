"""
@Title: 实现样本数据类
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-30 15:12:50
@Description: 
"""


class Sample:
    """样本类，基本特征是四个维度的度量值，即花萼长度、花萼宽度、花瓣长度与花瓣宽度"""

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"花萼长度: {self.sepal_length}, "
                f"花萼宽度: {self.sepal_width}, "
                f"花瓣长度: {self.petal_length}, "
                f"花瓣宽度: {self.petal_width}"
                f")"
                )


class LabeledSample(Sample):
    """带标签的样本，即用于监督学习的样本"""

    def __init__(self,
                 label: str,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        super().__init__(sepal_length, sepal_width, petal_length, petal_width)
        self.label = label

    @classmethod
    def from_dict(cls, data: dict[str:float]) -> None:
        if data["label"] not in ("Iris-setosa", "Iris-versicolor", "Iris-virginica"):
            raise ValueError(f"样本的标签错误")
        try:
            return cls(label=data["label"],
                       sepal_length=data["sepal_length"],
                       sepal_width=data["sepal_width"],
                       petal_length=data["petal_length"],
                       petal_width=data["petal_width"],)
        except:
            raise KeyError(f"样本提供的特征不正确")

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"花萼长度: {self.sepal_length}, "
                f"花萼宽度: {self.sepal_width}, "
                f"花瓣长度: {self.petal_length}, "
                f"花瓣宽度: {self.petal_width}, "
                f"标签: {self.label!r}"
                f")"
                )


class PredictSample(Sample):
    """需要进行预测的样本（没有标签，标签需要预测）"""

    def __init__(self, data: dict[str, float]) -> None:
        if set(data.keys()) != {
            "sepal_length", "sepal_width", "petal_length", "petal_width",
        }:
            raise ValueError(f"预测样本提供的特征数据不符合要求")
        try:
            self.sepal_length = data["sepal_length"]
            self.sepal_width = data["sepal_width"]
            self.petal_length = data["petal_length"]
            self.petal_width = data["petal_width"]
        except KeyError:
            raise KeyError(f"预测样本中找不到必须的特征（键）")
