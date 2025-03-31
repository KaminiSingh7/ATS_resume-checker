# -*- coding: utf-8 -*-



import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)


## More Resources

### Working with Notebooks in Colab

!pip install pandas
!pip install os
!pip install re
!pip install pdfplumber
!pip install numpy
!pip install docx2txt
import os
import re
import pandas as pd
import numpy
import pdfplumber
import docx2txt

path = "/home"
file_list = os.listdir(path)
print(type(file_list))
print(len(file_list))

path = "/home"
file_name = os.listdir(path)
print("Number of Resume:", len(file_name))
print("filenames (First 5 resumes):")
print(file_name[:5])

file_extension = []
for file_name in os.listdir(path):
  file_extension.append(os.path.splitext(file_name)[-1])
print(set(file_extension))

from collections import Counter
file_extension_count = Counter (file_extension)
print(file_extension_count)
print()
print("file e!pip install rextensions and count:")
for ext, cnt in file_extension_count.items():
  print(f"{ext} :{cnt}")

def extract_text_docx(file_path):
    text =docx2txt.process(file_path)
    return text
def extact_text_pdf(file_path):
    text = ''
    with pdfplumber.open(file_path) as pdf:
      for page in pdf.pages:
          text += page.extract_text()
    return text

import os
import pandas as pd

# Assuming extract_text_from_pdf and extract_text_from_docx are defined elsewhere

df = pd.DataFrame(columns=['file_name', 'text'])

# Directory path


for file_name in os.listdir(path):  # Correct method to list files
    file_path = path=f!pip install reile_name  # Ensure correct path handling
    text = ''

    if file_name.endswith(".pdf") or file_name.endswith(".PDF"):
        try:
            text = extact_text_pdf(file_path)  # Assuming this function is defined
        except :
            print("PDF Error For:" ,file_path)

    if file_name.endswith(".docx"):
        try:
            text = extract_text_docx(file_path)  # Assuming this function is defined
        except :
            print("DOCX Error For:", file_path)

    if text:
        df.loc[len(df)] = [file_name, text]

df.head()

import os
import pandas as pd

# Assuming extract_text_from_pdf and extract_text_from_docx are defined elsewhere

# Example: path should be a string with the folder path containing your files
path = '/home'

df = pd.DataFrame(columns=['file_name', 'text'])

# Iterate over all files in the specified directory
for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)  # Correct path handling
    text = ''

    if file_name.endswith(".pdf") or file_name.endswith(".PDF"):
        try:
            text = extact_text_pdf(file_path)  # Corrected function name
        except Exception as e:
            print(f"PDF Error For: {file_path}, {e}")

    if file_name.endswith(".docx"):
        try:
            text = extract_text_docx(file_path)  # Corrected function name
        except Exception as e:
            print(f"DOCX Error For: {file_path}, {e}")

    if text:
        df.loc[len(df)] = [file_name, text]

# Display the DataFrame's head
print(df.head())

import logging
logging.getLogger("pdfminer").setLevel(logging.ERROR)


 %%time
 email_pattern = r'[a-zA-Z0-9,_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

 phone_pattern = r'\+?\d[\d ]{8,13}\d'
# 
 def extract_email(content):
     email = re.findall(email_pattern, content)
     return email
# 
 def extract_phone(content):
     phone = re.findall(phone_pattern, content)
     return phone
 
 def extract_linkedIn(content):
   linkedIn_Id = re.findall(r'linkedin.com/in/([a-zA-Z0-9_-]+)', content)
   return linkedIn_Id
# 
  df['emails'] = df['text'].apply(lambda x: extract_email(x))
  df['phone_numbers'] = df ['text'].apply(lambda x: extract_phone(x))
  df.head()
# 
  df['linkedIn_Id'] = df['text'].apply(lambda x: extract_linkedIn(x))
  df.head()


 %%time # Checkout https://www.metacareers.com/jobs/624841835890795/
## Skills: machine learning, regression, python, recommendation system, pytorch
 skillset_score = {
    'Python': 2,
    'Machine Learning': 3, 
    'NGS': 3,
     'github': 2,  # Fixed missing comma
     'Bash': 3,    # Removed extra space in key
     'R programming': 2,
     'Molecular Docking': 3,
 }
# 
  skillset_score.keys()

regex = '(' + '|'. join(skillset_score.keys()) + ')'
regex

'(python|machine learning|R programming|Bash|Github|NGS|Molecular Docking)'

def extract_skill(content):
    skills = re.findall(regex,content.upper(),content.lower())
    return skills

df

import re

def extract_skill(content):
    skills = re.findall(regex, content, re.IGNORECASE)  # Use re.IGNORECASE for case-insensitive search
    return skills

import re

def extract_skill(content):
    # Find skills in their original case
    original_case_skills = re.findall(regex, content, re.IGNORECASE)

    # Find skills in uppercase
    uppercase_skills = re.findall(regex, content.upper(), re.IGNORECASE)

    # Combine both lists and remove duplicates using set
    all_skills = list(set(original_case_skills + uppercase_skills))

    return all_skills

df['skillset'] = df['text'].apply(lambda x: extract_skill(x))
df

df['skillset'] = df['skillset'].apply(lambda x : list(set(x)))
df.head()

df_skills = df.explode('skillset')
df_skills.head()

df_skills['skillset_score'] = df_skills['skillset'].apply(lambda x : skillset_score.get (x))
df_skills.head(20)

grouped_df = df_skills.groupby('file_name')
grouped_df['skillset_score'].sum()

profile_scores = grouped_df['skillset_score'].sum()
profile_scores.head()

sorted_profile_scores = profile_scores.sort_values(ascending=False)
sorted_profile_scores

# Filter the top profiles
sorted_profile_scores[sorted_profile_scores >=10]
