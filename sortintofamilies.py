import pandas as pd
import numpy


families = ['family 1', 'family 2', 'family 3', 'family 4',
            'family 5', 'family 6', 'family 7', 'family 8',
            'family 9']

filename = 'insertfilenamehere.csv'  # Name of the csv file that contains all of the youth
chapel = 'StakeCenter'  # Will be appended to the final file name

def main():
    master_trek_df = import_csv()
    prepped_df = prep_df(master_trek_df)
    final_list = assign_families(prepped_df)
    create_csv(final_list)


def create_csv(final_list):
    """Creates final csv and saves it to a location on the computer"""
    df = pd.DataFrame(final_list, columns=['Gender', 'Name', 'Age', 'Ward', 'Family'])
    df = df.sort_values(by=['Family', 'Gender', 'Age', 'Ward'])
    df.to_csv(f'/filelocationhere/sortedfamilies_{chapel}.csv', index=False)
    print('nothing')


def assign_families(df):
    """Assigns students to families"""
    df_list = df.values.tolist()
    family_index = 0
    for record in df_list:
        family = families[family_index]
        record.append(family)
        family_index += 1
        if family_index == len(families):
            family_index = 0
    return df_list

def prep_df(df):
    """Sorts the data frame based on values that are set"""
    df = df[df.Age != 'Adult']
    df = df[df.Age != 'Bishop']
    df = df.sort_values(by=['Gender', 'Age', 'Ward'])
    return df


def import_csv():
    """Imports the csv and converts to data frame"""
    master_trek_df = pd.read_csv(f'/Users/masonlancaster/Desktop/{filename}')
    return master_trek_df


if __name__ == "__main__":
    main()
