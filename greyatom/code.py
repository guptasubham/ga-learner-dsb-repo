# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
#data_file='file.csv' # path for the file
data=np.genfromtxt(path, delimiter=",", skip_header=1)

#print("\nData: \n\n", data)

#print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((data,new_record))

#Code starts here



# --------------
#Code starts here
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=np.mean(age)
age_std=np.std(age)

print(age,min_age,max_age,age_mean,age_std)


# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]



l=[]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
l.append(len_0)
l.append(len_1)
l.append(len_2)
l.append(len_3)
l.append(len_4)
#print(l)

minority_race=l.index(min(l))
print(minority_race)












# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=np.sum(senior_citizens[:,6],axis=0)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=round(high[:,7].mean(axis=0),2)
avg_pay_low=round(low[:,7].mean(axis=0),2)
print(avg_pay_high,avg_pay_low)


