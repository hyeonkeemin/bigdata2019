import random
import pandas as pd

def type_create(height, weight):
    bmi = weight / (height/100) ** 2
    if bmi < 18.5: return 'thin'
    if bmi < 25: return 'normal'
    return 'fat'

bmi_data = pd.DataFrame(columns=('height','weight','type'))

for i in range(30000):
    height = random.randint(120,200)
    weight = random.randint(35,80)
    bmi_data.loc[i] = [height, weight, type_create(height, weight)]

bmi_data.to_csv('bmi_test.csv', index=False)
