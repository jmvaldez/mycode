#!/usr/bin/env python3

import pandas as pd
import os

def main():
    user_file = input("Please enter the path of your file: Must be .txt ")
    if user_file.endswith(".txt"):
        df = pd.read_csv(user_file)
        new_csv = os.path.basename(user_file).replace(".txt", ".csv")
        print(new_csv)
        df.to_csv(new_csv, index = None)
        read_new_csv = pd.read_csv(new_csv)
        csv_headers = pd.read_csv(new_csv, index_col = 0, nrows = 0).columns.tolist()
        sort_by = input(f'What do you want to sort by? {csv_headers}')
        read_new_csv.sort_values( [sort_by], axis=0, ascending=[False], inplace=True  )
        
        preview_request = input("Do you want to preview your sorted csv?Yes or No? ")
        if preview_request == "Yes":
            print("\nYour sorted csv: ")
            print(read_new_csv)
            save_request = input("Would you like to save your file? Yes or No?")
        else:
            save_request = input("Would you like to save your file? Yes or No?")

            
        if save_request == "Yes":
            print(f'sorted_by_{sort_by}.csv')
            sorted_csv_file_name = f'sorted_by_{sort_by}.csv'
            print(sorted_csv_file_name)
            read_new_csv.to_csv(r'/home/student/static/' + sorted_csv_file_name , index=False)
        else:
            print("Your file will not be saved")

    else:
        print("Invalid file type. Must be a .txt file")
        user_file = input("Please enter the path of your file: ")


if __name__ == "__main__":
    main()
