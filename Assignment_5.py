#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
titanic = pd.read_csv("Titanic Data.csv")
titanic.head()


# In[2]:


###number one
import plotly.graph_objects as go
trace1 = go.Histogram(
    x=titanic.Age,
    opacity=0.75,
    name = "Age",
    marker=dict(color='rgba(171, 50, 96, 0.6)'))

data = [trace1]
layout = go.Layout(barmode='overlay',
                   title=' Age of passengers',
                   xaxis=dict(title='Age of passengers'),
                   yaxis=dict( title='Count'),
)
fig = go.Figure(data=data, layout=layout)
fig.show()


# In[3]:


###number two
female = titanic.Age[titanic.Sex == "female"]
male = titanic.Age[titanic.Sex == "male"]
trace1 = go.Histogram(
    x=female,
    opacity=0.75,
    name = "female",
    marker=dict(color='rgba(171, 50, 96, 0.6)'))
trace2 = go.Histogram(
    x=male,
    opacity=0.75,
    name = "male",
    marker=dict(color='rgba(12, 50, 196, 0.6)'))

data = [trace1, trace2]
layout = go.Layout(barmode='overlay',
                   title='Age of female and male passengers',
                   xaxis=dict(title='Age of female and male passengers'),
                   yaxis=dict( title='Count'),
)
fig = go.Figure(data=data, layout=layout)
fig.show()


# In[4]:


##number 3
import plotly.figure_factory as ff
import numpy as np
corrMatrix = titanic.corr()
print (corrMatrix)


# In[ ]:


##number 4
pd.pivot_table(titanic,'Survived', 'Fare','Pclass')
# data preparation
one = titanic[titanic.Pclass == 1]
two = titanic[titanic.Pclass == 2]
three = titanic[titanic.Pclass == 3]

trace0 = go.Box(
    y=one.Fare,
    name = 'Fare for class 1',
    marker = dict(
        color = 'rgb(12, 12, 140)',
    )
)
trace1 = go.Box(
    y=two.Fare,
    name = 'Fare for class 2',
    marker = dict(
        color = 'rgb(12, 128, 128)',
    )
)
trace2 = go.Box(
    y=three.Fare,
    name = 'Fare for class 3',
    marker = dict(
        color = 'rgb(12, 128, 128)',
    )
)
data = [trace0, trace1, trace2]

layout = go.Layout(title='Distribution of fare by passenger class',
                   xaxis=dict(title='Class of passenger'),
                   yaxis=dict( title='Count'),
)
fig = go.Figure(data=data, layout = layout)


#fig = go.Figure(dict(data = data, layout = layout))

fig.show()


# In[ ]:





# In[ ]:


##number 5
pd.crosstab(titanic.Survived,titanic.Sex)
Sex=['Female', 'Male']

fig = go.Figure(data=[
    go.Bar(name='Did Not survive', x=Sex, y=[81, 468]),
    go.Bar(name='Survived', x=Sex, y=[233, 109])
])
# Change the bar mode
fig.update_layout(barmode='stack',
                  title="Distribution of survival by gender",
                  xaxis=dict(title='Gender of passengers'),
                  yaxis=dict(title='Number of passengers')
                 )
fig.show()


# In[ ]:


##number 6
female = titanic[titanic.Sex == "female"]
male = titanic[titanic.Sex == "male"]
trace1 = go.Scatter(
                    x = female.Age,
                    y = female.Fare,
                    mode = "markers",  # type of plot like marker, line or line + markers
                    name = "Females",#name of the plots
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)')
                    ) #The hover text (hover is curser)
# Creating trace2
trace2 = go.Scatter(
                    x = male.Age,
                    y = male.Fare,
                    mode = "markers",
                    name = "males",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)')
                    )


# data 
data = [trace1, trace2]


#layoout 

layout = dict(title = 'Age versus fare for male and female passengers',
              xaxis=dict( title= 'Age of passenger',ticklen= 5,zeroline= False),
              yaxis=dict( title= 'Fare of passenger',ticklen= 5,zeroline= False)
             )



fig = go.Figure(dict(data = data, layout = layout))

fig.show()


# In[ ]:


##number 7
data = [
    {
        'y': titanic.Age,
        'x': titanic.Fare,
        'mode': 'markers',
        'marker': {
            'size': titanic.Pclass,
            'color':titanic.Survived
            
        },
        "text" :  titanic.PassengerId
    }
]

fig = go.Figure(data)

fig.show()

