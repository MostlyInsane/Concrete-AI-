import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense

# PreProcess The DataSet :

Data = pd.read_excel(r'C:\Users\MONSTERRRRR PC!!!!\Desktop\My Junk\DataSets\Concrete_Data.xls')

Data = Data.rename(columns={'Cement (component 1)(kg in a m^3 mixture)'               : 'Cement',
                              'Blast Furnace Slag (component 2)(kg in a m^3 mixture)' : 'Slag',
                              'Fly Ash (component 3)(kg in a m^3 mixture)'            : 'Fly Ash',
                              'Water  (component 4)(kg in a m^3 mixture)'             : 'Water',
                              'Superplasticizer (component 5)(kg in a m^3 mixture)'   : 'Superplasticizer',
                              'Coarse Aggregate  (component 6)(kg in a m^3 mixture)'  : 'Coarse Aggregate',
                              'Fine Aggregate (component 7)(kg in a m^3 mixture)'     : 'Fine Aggregate',
                              'Age (day)'                                             : 'Age',
                              'Concrete compressive strength(MPa, megapascals)'       : 'Concrete Strength'
                            })

Train_Data = Data[0:824]                                              # Training Data
CrossValidate_Data = Data[824:926]                                    # Validation Data
Test_Data = Data[926:1030]                                            # Test Data

Train_Data = np.array(Train_Data)                                     # Convert the DataFrame into NumPy Arrays

Scaler = MinMaxScaler(feature_range=(0, 1))                           # Scaling object with specified range
Scaled_Train_Date = Scaler.fit_transform(Train_Data)                  # Scaled Train_Data with Scaling Object

# Creating The Model :

Model = Sequential([
    Dense(8, input_shape=(8,), Activation='relu'),
    Dense(8, Activation='relu'),
    Dense(1,)
])

















