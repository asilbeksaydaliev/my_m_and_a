import pandas as pd
import my_ds_babel

def my_m_and_a(content_database_1, content_database_2, content_database_3):

  df_1 = pd.read_csv(content_database_1)
  df_2 = pd.read_csv(content_database_2,sep=';',header = None, names=['Age','City','Gender','Name','Email'])
  df_3 = pd.read_csv(content_database_3,sep='\t', names = ['Gender','Name','Email','Age','City','Country'],skiprows=1)

  new_name_2,new_name_3 = df_2.Name.str.split(expand=True),df_3.Name.str.split(expand=True)
  new_name_3[0] = new_name_3[0].str.replace('string_','')
  df_2['FirstName'],df_2['LastName'],df_2['UserName'] = new_name_2[0].str.extract(r'([a-zA-Z]+)'),new_name_2[1].str.extract(r'([a-zA-Z]+)'),new_name_2[0].str.extract(r'([a-zA-Z]+)')
  df_3['FirstName'],df_3['LastName'],df_3['UserName'] = new_name_3[0].str.extract(r'([a-zA-Z]+)'),new_name_3[1].str.extract(r'([a-zA-Z]+)'),new_name_3[0].str.extract(r'([a-zA-Z]+)')
  df_2['Age'] = df_2['Age'].str.extract('(\d+)')
  df_3['Age'] = df_3['Age'].str.extract('(\d+)')

  df = pd.concat([df_1,df_2,df_3])
  df.Gender = df.Gender.str.replace('string_', '').str.replace('boolean_', '').str.replace('character_', '')
  df.Gender = df.Gender.replace({'1':'Male','0':'Female','M':'Male','F':'Female'})
  df.FirstName,df.LastName,df.UserName = df.FirstName.str.title(),df.LastName.str.title(),df.UserName.str.lower()
  df.Email = df.Email.str.replace('string_', '').str.lower()
  df.City = df.City.str.replace('-', ' ').str.replace('_', ' ').str.title()
  df.Country = 'USA'
  df.drop('Name', inplace=True, axis=1)
  df.Age = df.Age.astype('str')
  df.FirstName,df.LastName = df.FirstName.astype('str'),df.LastName.astype('str')

  return df



# import pandas as pd
# import my_ds_babel
# import warnings
# warnings.filterwarnings('ignore')

# def my_m_and_a(data1, data2, data3):
    
#     all_data1 = pd.read_csv(data1)
#     all_data2 = pd.read_csv(data2, sep=';', header=None, names=['age', 'city', 'gender', 'name', 'email'])
#     all_data3 = pd.read_csv(data3, sep='\t', skiprows=1, names=['gender', 'name', 'email', 'age', 'city', 'country'])


#     genders = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
#     all_data1['Gender'] = all_data1['Gender'].replace(genders)
#     all_data1['FirstName'] = all_data1['FirstName'].replace(r'\W', '', regex=True)
#     all_data1['FirstName'] = all_data1['FirstName'].str.title()
#     all_data1['LastName'] = all_data1['LastName'].replace(r'\W', '', regex=True)
#     all_data1['LastName'] = all_data1['LastName'].str.title()
#     all_data1['Email'] = all_data1['Email'].str.lower()
#     all_data1['City'] = all_data1['City'].str.replace('_', '-')
#     all_data1['City'] = all_data1['City'].str.title()
#     all_data1['Country'] = 'USA'
#     all_data1.drop('UserName', axis=1, inplace=True)


#     all_data2.age = all_data2.age.str.replace(r'\D', '',  regex=True)
#     all_data2.city = all_data2.city.str.replace("_", '-').str.title()
#     genders = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
#     all_data2['gender'] = all_data2['gender'].replace(genders)
#     all_data2.name = all_data2.name.str.title()
#     name_df = all_data2.name.str.split(expand=True)
#     all_data2['first_name'], all_data2['last_name'] = name_df[0], name_df[1]
#     all_data2.first_name = all_data2.first_name.str.replace('\W', '').str.title()
#     all_data2.last_name = all_data2.last_name.str.replace("\W", "").str.title()
#     all_data2.drop('name', axis=1, inplace=True)
#     all_data2['Country'] = 'USA'
#     all_data2['email'] = all_data2['email'].str.lower()
#     all_data2 = all_data2[['gender', 'first_name', 'last_name', 'email', 'age', 'city',  'Country']]
#     all_data2.rename(columns={'gender': 'Gender', 'first_name':'FirstName', 'last_name':'LastName', 'email':'Email', 'age':'Age', 'city':'City', 'Country':'Country',},inplace=True )


#     all_data3.replace(r'string_', '', regex=True, inplace=True)
#     all_data3.replace(r'boolean_', '',regex=True, inplace=True)
#     all_data3.replace(r'character_', '', regex=True, inplace=True)
#     all_data3['gender'] = all_data3['gender'].replace(genders)
#     all_data3.replace(r'integer_', '', regex=True, inplace=True)
#     all_data3['email'] = all_data3['email'].str.lower()
#     all_data3.age = all_data3.age.str.replace("\D", "", regex=True)
#     all_data3.city = all_data3.city.str.replace("string_", "").str.replace("_", "-").str.title()
#     nw = all_data3['name'].str.split(expand=True)
#     all_data3['first_name'] = nw[0]
#     all_data3['last_name'] = nw[1]
#     all_data3.first_name = all_data3.first_name.str.replace('\W', '' )
#     all_data3.last_name = all_data3.last_name.str.replace("\W","" ).str.title()
#     all_data3.first_name = all_data3.first_name.str.replace('string_', '' ).str.title()
#     all_data3['country'] = 'USA'
#     all_data3.drop('name', axis=1, inplace=True)
#     all_data3 = all_data3[['gender', 'first_name', 'last_name', 'email', 'age', 'city', 'country']]
#     all_data3.rename(columns={'gender': 'Gender', 'first_name':'FirstName', 'last_name':'LastName', 'email':'Email', 'age':'Age', 'city':'City', 'country':'Country',},inplace=True )
    
    
#     data1 = pd.concat([all_data1, all_data1, all_data1], ignore_index=True)
#     data1 = data1.astype('string')


#     data1.LastName = data1.LastName.astype("str")
#     data1.FirstName = data1.FirstName.astype("str")
#     data1.Gender = data1.Gender.astype("str")

#     return data1

