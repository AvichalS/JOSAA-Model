# -*- coding: utf-8 -*-
"""JOSAA Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y1Mz5bOvQ0cM26pxK0EeWrS_EguGpk9G

Loading file
"""

import pandas as pd
df=pd.read_csv('/content/round1_josaa_22.csv')
df.dropna() #removing rows with null values

"""Preparing rank range"""

df['Opening Rank'] = pd.to_numeric(df['Opening Rank'], errors='coerce')
df['Closing Rank'] = pd.to_numeric(df['Closing Rank'], errors='coerce')
max_rank=int(df[['Closing Rank']].max())
min_rank=int(df[['Opening Rank']].min())

"""Preparing Seat types"""

seattypes=df['Seat Type'].unique()

"""Preparing gender options"""

genders=df['Gender'].unique()

"""Function to get student data"""

def get_data():
  while True:
    rank=int(input(f"Rank between: {min_rank} and {max_rank}\nEnter rank: "))
    if (rank>=min_rank) and (rank<=max_rank):
      while True:
        seat_type=input(f"\nSeat types avaliable: {seattypes}\nEnter seat type: ")
        if seat_type in seattypes:
          while True:
            gender=int(input(f"\nGender options\nPress 1 for: {genders[0]}\nPress 2 for: {genders[1]}\nEnter gender option number: "))
            if (gender==1) or (gender==2):
              print("\n\nDisplaying results...\n")
              if gender==1:
                gender=genders[0]
              else:
                gender=genders[1]
              break
            else:
              print("\nInvalid gender option. Please try again.\n")
          break
        else:
          print("\nInvalid seat type. Please try again.\n")
      break
    else:
      print("\nInvalid rank entered. Please try again.\n")    
  return rank, seat_type, gender

"""Function to find result list of college branches"""

def find_results(rank, seat_type, gender):
  res=[]
  for i in range(len(df)):
    if (rank>=df.loc[i][5]) and (rank<=df.loc[i][6]) and (gender==df.loc[i][4]) and (seat_type==df.loc[i][3]):
      res.append(df.loc[i][0:2])
  res_df = pd.DataFrame(res, columns=['Institute', 'Academic Program Name'])
  return res_df

"""Driver code"""

rank, seat_type, gender=get_data()
res_df=find_results(rank, seat_type, gender)
res_df