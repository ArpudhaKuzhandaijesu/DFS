#!/usr/bin/env python
# coding: utf-8

# Depth first search
# stack operations:
# 1.push()
# 2.pop()
# 3.size()
# 4.top()

# In[3]:


graph={
    'start':['A','B'],
    'A':['start','E','F'],
    'B':['start','D','C'],
    'C':['B'],
    'D':['B','goal'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'goal':['E','F']
}


# In[5]:


def dfs(graph,start,goal,visited):
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            if node==goal:
                print(visited)
            for neighbours in graph[node]:
                dfs(graph,neighbours,goal,visited)


# In[8]:


dfs(graph,"start","goal",[])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




