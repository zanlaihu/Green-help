#  Created by Zanlai Hu on 2018/3/10.
#  Copyright © 2018 zanlaihu. All rights reserved.

# This is the file to rank stars for every products, so that we can find the most healthy food.
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def write_in_csv(dataframe, file):
    dataframe.to_csv(file, sep=',', encoding='utf-8')

if __name__ == '__main__':
    csv_file = 'ausnut1.csv'  # path to the downloaded csv file
    dataframe = pd.read_csv(csv_file)

    columns_to_keep = ['Food ID','Food Name','Energy, with dietary fibre (kJ)', 'Protein (g)', 'Added sugars (g)']
    newdf = dataframe[columns_to_keep]
    newdf = newdf.assign(protein_ratio=newdf['Protein (g)'] / newdf['Energy, with dietary fibre (kJ)'])
    newdf = newdf.assign(addedsugar_ratio=newdf['Added sugars (g)'] / newdf['Energy, with dietary fibre (kJ)'])

    by_protein = newdf.sort_values(by=["protein_ratio"], ascending=False)
    by_addsugar = newdf.sort_values(by=["addedsugar_ratio"], ascending=False)

    def function1(a):
        if a < 0.006:
            return 1
        elif a < 0.012:
            return 2
        elif a < 0.018:
            return 3
        elif a < 0.024:
            return 4
        elif a < 0.03:
            return 5
        elif a < 0.036:
            return 6
        elif a < 0.042:
            return 7
        elif a < 0.048:
            return 8
        elif a < 0.054:
            return 9
        else:
            return 10


    def function2(a):
        if a < 0.006:
            return 10
        elif a < 0.012:
            return 9
        elif a < 0.018:
            return 8
        elif a < 0.024:
            return 7
        elif a < 0.03:
            return 6
        elif a < 0.036:
            return 5
        elif a < 0.042:
            return 4
        elif a < 0.048:
            return 3
        elif a < 0.054:
            return 2
        else:
            return 1


    newdf['protein_star'] = newdf.apply(lambda x: function1(x.protein_ratio), axis=1)
    newdf['addedsugar_star'] = newdf.apply(lambda x: function2(x.addedsugar_ratio), axis=1)

    print(newdf)

    def function3(a, b):
        c = (a + b)/2
        return c

    newdf['aver_star'] = newdf.apply(lambda x: function3(x.protein_star, x.addedsugar_star), axis=1)
    write_in_csv(newdf, "stars_products10.csv")  # path where the new csv file is stored



