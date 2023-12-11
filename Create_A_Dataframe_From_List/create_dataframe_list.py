import pandas as pd
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    # Extract student IDs and ages from the 2D list
    student_ids = [row[0] for row in student_data]
    ages = [row[1] for row in student_data]

    # Create a dictionary with student IDs and ages
    data = {"student_id": student_ids, "age": ages}

    # Create a pandas DataFrame from the dictionary
    dataframe = pd.DataFrame(data)

    return dataframe
