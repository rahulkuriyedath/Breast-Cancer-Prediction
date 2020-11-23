# _Exploratory Data Analysis of the Coimbra Breast Cancer data Data Set._

## Dataset Summary.

The dataset used in this project consists of anthropometric data and parameters gathered in a standard blood analysis. This dataset was created by Miguel Patrício, José Pereira, Joana Crisóstomo, Paulo Matafome, Raquel Seiça, Francisco Caramelo, all from the Faculty of Medicine of the University of Coimbra and also Manuel Gomes from the University Hospital Centre of Coimbra (Patrício et al., 2018). The dataset was sourced from the UCI Machine Learning Repository (Dua and Graff 2017) and it can be found [here](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra), particularly [this file](https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv). Each row in this dataset represents a set of observations of individual patients and each column represents a variable. In this dataset, there are 116 observations and 9 features which are all numerical. There are zero observations with missing values for each class in the dataset. The target column is a binary dependent variable, which indicates the presence (Classification = 2) or absence (Classification = 1) of breast cancer.


### Exploratory Data Analysis checklist:

- Formulate the question
- Read in the data
- Check the packaging
- Look at the top and the bottom of your data
- Make a plot
- Follow up

### Formulate the Question: 

Given the anthropometric parameters available, does a patient have breast cancer or not?

## Load Required Packages


```python
import matplotlib.pyplot as plt
import altair as alt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
```

## Read in the data and Check the packaging


```python
bc_df = pd.read_csv("../data/raw/dataR2.csv")

bc_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>BMI</th>
      <th>Glucose</th>
      <th>Insulin</th>
      <th>HOMA</th>
      <th>Leptin</th>
      <th>Adiponectin</th>
      <th>Resistin</th>
      <th>MCP.1</th>
      <th>Classification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>48</td>
      <td>23.500000</td>
      <td>70</td>
      <td>2.707</td>
      <td>0.467409</td>
      <td>8.8071</td>
      <td>9.702400</td>
      <td>7.99585</td>
      <td>417.114</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>83</td>
      <td>20.690495</td>
      <td>92</td>
      <td>3.115</td>
      <td>0.706897</td>
      <td>8.8438</td>
      <td>5.429285</td>
      <td>4.06405</td>
      <td>468.786</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>82</td>
      <td>23.124670</td>
      <td>91</td>
      <td>4.498</td>
      <td>1.009651</td>
      <td>17.9393</td>
      <td>22.432040</td>
      <td>9.27715</td>
      <td>554.697</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>68</td>
      <td>21.367521</td>
      <td>77</td>
      <td>3.226</td>
      <td>0.612725</td>
      <td>9.8827</td>
      <td>7.169560</td>
      <td>12.76600</td>
      <td>928.220</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>86</td>
      <td>21.111111</td>
      <td>92</td>
      <td>3.549</td>
      <td>0.805386</td>
      <td>6.6994</td>
      <td>4.819240</td>
      <td>10.57635</td>
      <td>773.920</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>111</th>
      <td>45</td>
      <td>26.850000</td>
      <td>92</td>
      <td>3.330</td>
      <td>0.755688</td>
      <td>54.6800</td>
      <td>12.100000</td>
      <td>10.96000</td>
      <td>268.230</td>
      <td>2</td>
    </tr>
    <tr>
      <th>112</th>
      <td>62</td>
      <td>26.840000</td>
      <td>100</td>
      <td>4.530</td>
      <td>1.117400</td>
      <td>12.4500</td>
      <td>21.420000</td>
      <td>7.32000</td>
      <td>330.160</td>
      <td>2</td>
    </tr>
    <tr>
      <th>113</th>
      <td>65</td>
      <td>32.050000</td>
      <td>97</td>
      <td>5.730</td>
      <td>1.370998</td>
      <td>61.4800</td>
      <td>22.540000</td>
      <td>10.33000</td>
      <td>314.050</td>
      <td>2</td>
    </tr>
    <tr>
      <th>114</th>
      <td>72</td>
      <td>25.590000</td>
      <td>82</td>
      <td>2.820</td>
      <td>0.570392</td>
      <td>24.9600</td>
      <td>33.750000</td>
      <td>3.27000</td>
      <td>392.460</td>
      <td>2</td>
    </tr>
    <tr>
      <th>115</th>
      <td>86</td>
      <td>27.180000</td>
      <td>138</td>
      <td>19.910</td>
      <td>6.777364</td>
      <td>90.2800</td>
      <td>14.110000</td>
      <td>4.35000</td>
      <td>90.090</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>116 rows × 10 columns</p>
</div>



### The Workflow to which we should adhere.

To avoid breaking the golden rule and hence optaining an optimistic estimate of our model's performance when computing scores (which is bad), we have decided to split our dataset before performing an exploratory data analysis.


```python
train_df, test_df = train_test_split(bc_df, test_size = 0.3, random_state = 111)
```


```python
train_df["Classification"].value_counts(normalize=True)
```




    2    0.567901
    1    0.432099
    Name: Classification, dtype: float64



The class distribution is fairly balanced, therefore we do not need to worry about a class imbalance. 


```python
train_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 81 entries, 94 to 84
    Data columns (total 10 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   Age             81 non-null     int64  
     1   BMI             81 non-null     float64
     2   Glucose         81 non-null     int64  
     3   Insulin         81 non-null     float64
     4   HOMA            81 non-null     float64
     5   Leptin          81 non-null     float64
     6   Adiponectin     81 non-null     float64
     7   Resistin        81 non-null     float64
     8   MCP.1           81 non-null     float64
     9   Classification  81 non-null     int64  
    dtypes: float64(7), int64(3)
    memory usage: 7.0 KB



```python
train_df.describe(include = "all")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>BMI</th>
      <th>Glucose</th>
      <th>Insulin</th>
      <th>HOMA</th>
      <th>Leptin</th>
      <th>Adiponectin</th>
      <th>Resistin</th>
      <th>MCP.1</th>
      <th>Classification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
      <td>81.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>56.716049</td>
      <td>27.484590</td>
      <td>100.888889</td>
      <td>11.592642</td>
      <td>3.228910</td>
      <td>27.571460</td>
      <td>9.699994</td>
      <td>14.767862</td>
      <td>528.879457</td>
      <td>1.567901</td>
    </tr>
    <tr>
      <th>std</th>
      <td>16.612672</td>
      <td>5.020722</td>
      <td>24.901807</td>
      <td>11.358037</td>
      <td>4.192692</td>
      <td>20.296397</td>
      <td>6.168656</td>
      <td>13.242587</td>
      <td>346.611009</td>
      <td>0.498454</td>
    </tr>
    <tr>
      <th>min</th>
      <td>24.000000</td>
      <td>18.370000</td>
      <td>74.000000</td>
      <td>2.432000</td>
      <td>0.563880</td>
      <td>4.311000</td>
      <td>2.194280</td>
      <td>3.210000</td>
      <td>45.843000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>45.000000</td>
      <td>23.000000</td>
      <td>87.000000</td>
      <td>4.690000</td>
      <td>1.013839</td>
      <td>12.261700</td>
      <td>5.429285</td>
      <td>6.850000</td>
      <td>280.694000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>54.000000</td>
      <td>27.300000</td>
      <td>93.000000</td>
      <td>6.760000</td>
      <td>1.658774</td>
      <td>20.092000</td>
      <td>8.010000</td>
      <td>10.576350</td>
      <td>448.799000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>69.000000</td>
      <td>31.250000</td>
      <td>103.000000</td>
      <td>12.548000</td>
      <td>3.262364</td>
      <td>37.843000</td>
      <td>11.787960</td>
      <td>16.485080</td>
      <td>667.928000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>89.000000</td>
      <td>37.035608</td>
      <td>201.000000</td>
      <td>58.460000</td>
      <td>25.050342</td>
      <td>90.280000</td>
      <td>36.060000</td>
      <td>82.100000</td>
      <td>1698.440000</td>
      <td>2.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Make Plots:


```python
features = train_df.drop(columns = ["Classification"]).select_dtypes(include = np.number)

for feat in features:
    ax = train_df.groupby("Classification")[feat].plot.hist(bins = 20, alpha = 0.4, legend = True)
    plt.xlabel(feat)
    plt.title("Histogram of " + feat)
    plt.show()
```


    
![png](output_16_0.png)
    



    
![png](output_16_1.png)
    



    
![png](output_16_2.png)
    



    
![png](output_16_3.png)
    



    
![png](output_16_4.png)
    



    
![png](output_16_5.png)
    



    
![png](output_16_6.png)
    



    
![png](output_16_7.png)
    



    
![png](output_16_8.png)
    


## Follow up:

Looking at the graphs developed above, there seems to be some interesting features which we can use to predict the presence or absence of breast cancer. Therefore, we plan on exploring classification evaluation metrics, developing a baseline model, exploring more complicated models, choosing a model based on our evaluation metrics, and performing hyperparameter optimization of the model.  

# _References_

Patrício, M., Pereira, J., Crisóstomo, J., Matafome, P., Gomes, M., Seiça, R. and Caramelo, F., 2018. Using Resistin, glucose, age and BMI to predict the presence of breast cancer. BMC Cancer, 18(1). https://doi.org/10.1186/s12885-017-3877-1

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences. http://archive.ics.uci.edu/ml.
