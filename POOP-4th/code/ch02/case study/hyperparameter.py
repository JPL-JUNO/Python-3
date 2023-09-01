"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 17:33:34
@Description: 
"""
from trainingdata import TrainingData
import weakref


class HyperParameter:
    def __init__(self, k: int, training: "TrainingData") -> None:
        self.k = k
        self.data: weakref.ReferenceType["TrainingData"] = weakref.ref(
            training)
        self.quality: float
