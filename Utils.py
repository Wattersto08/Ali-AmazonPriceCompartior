import pandas as pd
import numpy as np

DEBUG = True



def ALI_Convertcost(_input):
    _input = _input.replace('US $', '')
    z = _input.split(' - ')
    print(z)
    if len(z) > 1:
        return float(z[0]),float(z[1])
    else:
        try:
            return float(z[0])
        except:
            print('failed to convert')



def Output_CSV(name, price, search):

    LP = []
    HP = []
    srch = []

    
    # Convert price string to floats
    for i in price:
        print(i)
        try:
            _LP,_HP = ALI_Convertcost(i)
        except:
            LP.append(_LP)
            try:
                HP.append(_HP)
            except:
                HP.append(0)
    # create srch name list
    for i in range(len(name)):
        srch.append(search)
    
    #create a DF with appropriate colnames
    df = pd.DataFrame(list(zip(srch, name, LP,HP)), 
               columns =['Search', 'Product Name', 'Low Price', 'High Price'])

    # drop erronious rows 
    df['Name'].replace('', np.nan, inplace=True)
    df.dropna(subset=['Name'], inplace=True)

    #Export to .CSV
    df.to_csv('AliExpress_Prod_Search.csv')

    if DEBUG:
        print(df.head())
