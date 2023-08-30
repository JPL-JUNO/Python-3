"""
@Title: 超参数调整，可以衡量不同参数下模型的性能
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-30 17:31:22
@Description: 
"""

from distance import Distance
from knn import KNNClassifier
from itertools import product


class HyperParameter:
    """超参数的调整，没能实现"""

    def __init__(self, model: KNNClassifier, parameters: dict[str:list]) -> None:
        self.model = model
        self.parameters = parameters

    def fit(self):
        params: list[str] = []
        for param in self.parameters.keys():
            if param in self.model.get_params():
                params.append(param)
            else:
                raise ValueError(f"模型不存在参数 {param}")

        for param_pair in product(*list(self.parameters.values())):
            params_dict = dict(zip(self.parameters.keys(), param_pair))
            print(params_dict)
            self.model.set_params(params_dict)


if __name__ == '__main__':
    knn = KNNClassifier()
    hp = HyperParameter(knn, {'k': [3, 5, 7], 'p': [1, 2]})
    hp.fit()
    print(knn.k)
