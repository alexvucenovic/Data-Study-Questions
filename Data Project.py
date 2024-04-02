#!/usr/bin/env python
# coding: utf-8

# ## Alexandra Vucenovic, 2-13-24, Project 1

# In[31]:


import pandas as pd 


# In[32]:


import matplotlib.pyplot as plt


# In[33]:


df = pd.read_csv('Non-Majors Survey Results - Fall 2020.csv')


# ### Showing the top of the data

# In[34]:


df.head()


# ### Describing Data

# In[35]:


df.describe()


# ### Showing tail of data

# In[36]:


df.tail()


# ### Showing sample of data collected from surveys

# In[37]:


df.sample()


# ### Showing information held in dataset

# In[38]:


df.info()


# ### Removing the race/ethnicity question from dataset as redundancy 

# In[39]:


df_drop = df.drop("Race/ethnicity", axis = 1)    
print(df_drop) 


# ### Renaming 2 columns in the dataset to shorter names 

# In[40]:


df = df.rename(columns={'Which course are you currently enrolled in?': 'Currently_enrolled_in?', 'If you answered that you were interested in taking more computing classes, which ones interest you most? (check all that apply)': 'If_interested_in_computing_classes_select_all_that_apply'})


# In[41]:


df.info()


# ### Testing that the new name changes are inputted in the system^ 

# # Main Motivations Students took Computing Classes at CCM

# In[42]:



df["What motivated you to seek a computing class at CCM?"].describe()

## take from the data question and show the answer! do not need to create a whole dataset 

#df1 = df[['what were ...', 'what were ...']]
#df.value_count()
#yes's and no's


# # Show a barchart of top sources how students heard about CCM

# In[43]:


#rename all df's first and take subset


#df0 = df[["Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Open House]", "Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Instant Decision Day]", "Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [On-Campus Information Session]", "Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Virtual Information Session]", "Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Women Who Dare]", "Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Regional College Fair]" ]]
#df0.value_counts()

#df1.value_counts()
df.rename(
    columns=({'Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Open House]': 'Open House'}),
    inplace=True,
)
#df2.value_counts()
df.rename(
    columns=({'Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Instant Decision Day]': 'Instant Decision Day'}),
    inplace=True,

)
#df3.value_counts()
df.rename(
    columns=({'Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [On-Campus Information Session]': 'On-Campus Information Session'}),
    inplace=True,

)
#df4.value_counts()
df.rename(
    columns=({'Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Virtual Information Session]': 'Virtual Information Session'}),
    inplace=True,

)
#df5.value_counts()
df.rename(
    columns=({'Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Women Who Dare]': 'Women Who Dare'}),
    inplace=True,

)
#df6.value_counts()
df.rename(
    columns=({'Prior to applying to college, did you participate in any of the following events or activities at the County College of Morris and/or with the Department of Information Technologies, if at all? [Regional College Fair]': 'Regional College Fair'}),
    inplace=True,

)

#df.value_counts()



df0 = df[['Regional College Fair','Women Who Dare', 'Virtual Information Session', 'On-Campus Information Session','Instant Decision Day', 'Open House']]
df0.value_counts()

df0

yes_counts={
    'College Fair':(df0['Regional College Fair'] == 'Yes').sum(),
    'Women Who Dare':(df0['Women Who Dare']=='Yes').sum(),
    'Virtual Information Session':(df0['Virtual Information Session']=='Yes').sum(),
    'On-Campus Information Session':(df0['On-Campus Information Session']=='Yes').sum(),
    'Instant Decision Day':(df0['Instant Decision Day']=='Yes').sum(),
    'Open House':(df0['Open House']=='Yes').sum(),
}

keys = list(yes_counts.keys())
values = list(yes_counts.values())

plt.barh(keys, values)
plt.title('How Students heard about CCM')
plt.xlabel('Count of "Yes"')


#initialize df1? 
#df1
#df1.rename("What are the top sources of how students heard about CCM? Show a bar chart of this field, sort from highest to lowest.")


# # What are the top sources of students hearing about computing classes at CCM?

# In[44]:


df.rename(
    columns=({'Did you receive information about our computing course from any of the following sources? [CCM Information Technologies Website]': 'CCM Information Technologies Website'}),
    inplace=True,
)

df.rename(
    columns=({'Did you receive information about our computing course from any of the following sources? [CCM Admissions]': 'CCM Admissions'}),
    inplace=True,
)

df.rename(
    columns=({'Did you receive information about our computing course from any of the following sources? [CCM advisor/counselor]': 'CCM advisor/counselor'}),
    inplace=True,
)

df.rename(
    columns=({'Did you receive information about our computing course from any of the following sources? [Employer]': 'Employer'}),
    inplace=True,
)

df.rename(
    columns=({'Did you receive information about our computing course from any of the following sources? [Other]': 'Other'}),
    inplace=True,
)



df0 = df[['CCM Information Technologies Website', 'CCM Admissions', 'CCM advisor/counselor', 'Employer', 'Other']]

df0.value_counts()

df0

yes_counts={
    'CCM Information Technologies Website':(df0['CCM Information Technologies Website'] == 'Yes').sum(),
    'CCM Admissions':(df0['CCM Admissions'] == 'Yes').sum(),
    'CCM advisor/counselor':(df0['CCM advisor/counselor'] == 'Yes').sum(),
    'Employer':(df0['Employer'] == 'Yes').sum(),
    'Other':(df0['Other'] == 'Yes').sum(),    
}

keys = list(yes_counts.keys())
values = list(yes_counts.values())

plt.barh(keys, values)
plt.title('Top Sources for hearing about CCM CS Classes')
plt.xlabel('Count of "Yes"')


#df1= df.rename("What are the top sources of students hearing about computing classes at CCM?")

#when calling dfs from previous code it would skip over that code and go straight 


# # Create a barchart showing what age group is most likely to take CS Classes

# In[45]:


#plt.bar=(['18:24'], ['25:35'], ['36:46'], ['47:67'], ['68:88'], 'Students')


df0 = df[['Age ']]

Agedf = df0.value_counts().reset_index()

            #x              #y 

plt.bar(Agedf.iloc[:,0], Agedf.iloc[:,1])


#df0

#    'Age ':(df0['18 and younger'] == 'Yes').sum(),
    
    
#

#18 younger, 19-20, 21-24, 25-34, 35-64, 65+

#Figure out how to properly graph and depict the age ranges in correlation w survey results 

