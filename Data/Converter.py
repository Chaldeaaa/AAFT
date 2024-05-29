#!/usr/bin/env python
# coding: utf-8

# In[24]:


import nbformat
from nbconvert import PythonExporter


# In[20]:


os.chdir('/content/drive/MyDrive/AAFT_Draft/Data')


# In[21]:


# .ipynb to .py

notebook_filename = 'Crawler.ipynb'
output_filename = 'Crawler.py'

with open(notebook_filename) as f:
    nb = nbformat.read(f, as_version=4)

python_exporter = PythonExporter()
(script, resources) = python_exporter.from_notebook_node(nb)

with open(output_filename, 'w') as f:
    f.write(script)


# In[27]:


# .ipynb to .r

notebook_filename = 'Analysis.ipynb'
output_filename = 'Analysis.R'

with open(notebook_filename) as f:
    nb = nbformat.read(f, as_version=4)

code_cells = []
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        code_cells.append(cell['source'])

script_content = "\n\n".join(code_cells)
with open(output_filename, 'w') as f:
    f.write(script_content)


# In[ ]:




