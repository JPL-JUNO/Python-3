"""
@Description: Working with NumPy Arrays: Slicing, Broadcasting, and Array Types
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-06 14:48:50
"""
import numpy as np
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer = [118, 118, 127]
softwareEngineer = [129, 131, 137]
employees = np.array([dataScientist, productManager,
                      designer, softwareEngineer])
employees[0, ::2] = employees[0, ::2]*1.1
print(employees)
