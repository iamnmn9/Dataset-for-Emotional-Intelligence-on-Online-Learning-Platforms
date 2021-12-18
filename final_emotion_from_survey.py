import glob
import os
import pandas as pd

star1 = os.path.join('/content/sheeet final', "*.csv")
star1 = glob.glob(star1)

x = sort(star1)

path_list=[]
for paths in x:
  path_list.append(paths)
len(path_list)

emotion_list_=[]
for i in range(len(path_list)-1):
  
  read = pd.read_csv(path_list[i])
  
  for j in read.columns[1:21]:
   m = read[j].value_counts().idxmax()
   emotion_list_.append(m)


read_last_csv = pd.read_csv(path_list[138])

for k in read_last_csv.columns[1:25]:
  m = read_last_csv[k].value_counts().idxmax()
  emotion_list_.append(m)
  
  
emotions = emotion_list_ 
     
# dictionary of lists  
dict = {'emotions': emotions}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('Final_face_to_emotion.csv') 

