import pandas as pd
import numpy


families = ['family 1', 'family 2', 'family 3', 'family 4',
            'family 5', 'family 6', 'family 7', 'family 8',
            'family 9']
filename = 'insertfilenamehere.csv'
chapel = 'StakeCenter'
print(len(families))

def main():
    master_trek_df = import_csv()
    prepped_df = prep_df(master_trek_df)
    final_list = assign_families(prepped_df)
    create_csv(final_list)


def create_csv(final_list):
    df = pd.DataFrame(final_list, columns=['Gender', 'Name', 'Age', 'Ward', 'Family'])
    df = df.sort_values(by=['Family', 'Gender', 'Age', 'Ward'])
    df.to_csv(f'/Users/masonlancaster/Desktop/sortedfamilies_{chapel}.csv', index=False)
    print('nothing')


def assign_families(df):
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
    df = df[df.Age != 'Adult']
    df = df[df.Age != 'Bishop']
    df = df.sort_values(by=['Gender', 'Age', 'Ward'])
    return df


def import_csv():
    master_trek_df = pd.read_csv(f'/Users/masonlancaster/Desktop/{filename}')
    return master_trek_df


if __name__ == "__main__":
    main()
