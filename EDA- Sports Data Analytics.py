#!/usr/bin/env python
# coding: utf-8

# <h1>THE SPARKS FOUNDATION</h1>
# 
# <h1>GRIP JAN2021 Data Science & Business Analytics</h1>
# 
# <h1>Task 5: Exploratory Data Analysis on IPL Dataset</h1>
# 
# <h3>Objectives:</h3>
# 
# * Perform EDA on the IPL Dataset.
# * As a sports analyst, find out the most successful teams, players and factors contributing win or loss of a team.
# * Suggest teams or players a company should endorse for its products.
# 
# 
# 
# 

# In[1]:


#importing python libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#function to plot data

def annot_plot(ax,w,h):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x()+w, p.get_height()+h))


# In[3]:


#importing the data files

delivery_data = pd.read_csv(r"C:\Users\ekta\Downloads\deliveries.csv")
match_data = pd.read_csv(r"C:\Users\ekta\Downloads\matches.csv")


# In[4]:


#understanding match_data

match_data.head()


# In[5]:


#understanding delivery_data

delivery_data.head()


# In[6]:


#understanding match_data

match_data.shape


# In[7]:


#understanding delivery_data

delivery_data.shape


# <h2>Data Information</h2>

# In[8]:


match_data.describe()


# In[9]:


match_data.info()


# In[11]:


match_data.isnull().sum()


# In[12]:


match_data['win_by'] = np.where(match_data['win_by_runs']>0,'Bat first','Bowl first')


# In[44]:


delivery_data.describe()


# In[46]:


delivery_data.info()


# In[48]:


delivery_data.isnull().sum()


# In[13]:


delivery_data['runs']=delivery_data['total_runs'].cumsum()


# <h2>Number of Matches Played in each IPL Season</h2>

# In[14]:


plt.figure(figsize = (12,6))
sns.countplot(x = 'season', data = match_data)
plt.show


# Oberservations: 
# 
# * Most number of matches were played in the IPL 2013 Season.
# * Least number of matches were played in the IPL 2009 Season.

# <h2>Number of Matches played by each Team</h2>
# 
# Obersarvation:
# 
# * It appears that the team Mumbai Indians has played the most number of matches while the team Kochi Tuskers Keralaplayed the least number of matches
# 

# In[15]:


team_df = pd.melt(match_data, id_vars = ['id', 'season'], value_vars = ['team1', 'team2'])

plt.figure(figsize = (12,6))
sns.countplot(x = 'value', data = team_df)
plt.xticks(rotation = 'vertical')
plt.show()


# <h2>Matches Won By the Teams</h2>
# 
# Oberservations:
# 
# * Mumbai Indians won maximum number of matches followed by Chennai Super Kings.
# 
#  

# In[16]:


plt.figure(figsize = (12,6))
data = match_data.winner.value_counts()
sns.barplot( y = data.index, x = data, orient = 'h')
plt.show


# In[17]:


ax=sns.countplot(x='winner',data=match_data)
plt.ylabel('Match')
plt.xticks(rotation=80)
annot_plot(ax,0.05,1)


# In[18]:


#Team won by Maximum Runs

match_data.iloc[match_data['win_by_runs'].idxmax()]['winner']


# In[19]:


#Team won by Maximum Wickets

match_data.iloc[match_data[match_data['win_by_wickets'].ge(1)].win_by_wickets.idxmax()]['winner']


# In[20]:


#Team won by Minimum Runs

match_data.iloc[match_data['win_by_runs'].idxmin()]['winner']


# In[21]:


#Team won by Minimum Wickets

match_data.iloc[match_data[match_data['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]['winner']


# <h2>Win Perecentage</h2>

# In[22]:


match = match_data.win_by.value_counts()
labels = np.array(match.index)
sizes = match.values
colors = ['green', 'gold']

# Plot
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%',startangle=90)

plt.title('Match Result')
plt.axis('equal')
plt.show()


# In[23]:


sns.countplot('season',hue='win_by',data=match_data,palette="Set1")


# <h2>Toss Decisions so far</h2>
# 
# Observations:
# 
# * 

# In[24]:


toss = match_data.toss_decision.value_counts()
labels = np.array(toss.index)
sizes = toss.values
colors = ['green', 'gold']
#explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow= False,startangle=90)

plt.title('Toss Result')
plt.axis('equal')
plt.show()


# In[25]:


sns.countplot('season',hue='toss_decision',data=match_data,palette="Set1")


# In[26]:


num_of_wins = (match_data.win_by_wickets > 0).sum()
num_of_loss = (match_data.win_by_wickets == 0).sum()
label = ["Wins", "Loses"]
total = float(num_of_wins + num_of_loss)
sizes = [(num_of_wins/total)*100, (num_of_loss/total)*100]
colors = ['green', 'gold']
plt.pie(sizes, labels=label, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
plt.title("Win percentage batting second")
plt.show()


# Obeservation:
# 
# * It seems that around 53.7% of the times, the teams that chose batting second have won the match. 

# <h2>IPL Winners</h2>

# In[27]:


final_matches=match_data.drop_duplicates(subset=['season'], keep='last')

final_matches[['season','winner']].reset_index(drop=True).sort_values('season')


# <h2>Player who won the most number of Player of the Match Award</h2>
# 
# Observation:
# * 

# In[28]:


top_players = match_data.player_of_match.value_counts()[:10]
fig, ax = plt.subplots(figsize = (14, 8))
ax.set_ylim([0,20])
ax.set_ylabel("Count")
ax.set_title("Top 'Player of the Match' Winners")
top_players.plot.bar()
sns.barplot( x = top_players.index, y = top_players, orient ='v')
plt.show()


# <h2>Top Scoring Batsman</h2>

# In[29]:


max_runs = delivery_data.groupby(['batsman'])['batsman_runs'].sum()
max_runs.sort_values(ascending=False,inplace=True)
max_runs[:10].plot(kind='bar')


# <h2>Batsman with Most Number of Fours</h2>

# In[30]:


temp_data = delivery_data.groupby('batsman')['batsman_runs'].agg(lambda x: (x==4).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
temp_data = temp_data.iloc[:10,:]

labels = np.array(temp_data['batsman'])
ind = np.arange(len(labels))
width = 0.5
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(temp_data['batsman_runs']), width=width, color='blue')
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel("Count")
ax.set_title("Batsman with most number of boundaries.!",fontsize = 10)
plt.show()


# <h2>Batsman with Most Number of Sixes</h2>

# In[31]:


temp_data = delivery_data.groupby('batsman')['batsman_runs'].agg(lambda x: (x==6).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
temp_data = temp_data.iloc[:10,:]

labels = np.array(temp_data['batsman'])
ind = np.arange(len(labels))
width = 0.5
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(temp_data['batsman_runs']), width=width, color='blue')
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation=90)
ax.set_ylabel("Count")
ax.set_title("Batsman with most number of sixes.!")
ax.set_xlabel('Batsmane Name')
plt.show()


# <h2>Batsman who played Most Number of Dot Balls</h2>

# In[32]:


temp_data = delivery_data.groupby('batsman')['batsman_runs'].agg(lambda x: (x==0).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
temp_data = temp_data.iloc[:10,:]

labels = np.array(temp_data['batsman'])
ind = np.arange(len(labels))
width = 0.5
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(temp_data['batsman_runs']), width=width, color='blue')
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel("Count")
ax.set_title("Batsman with most number of dot balls.!")
ax.set_xlabel('Batsmane Name')
plt.show()


# <h2>Orange Cap Winners</h2>

# In[33]:


season_data = match_data[['id','season','winner']]
complete_data = delivery_data.merge(season_data,how='inner',left_on='match_id',right_on='id')


# In[34]:


Season_orange_cap = complete_data.groupby(["season","batsman"])["batsman_runs"].sum().reset_index().sort_values(by="batsman_runs",ascending=False).reset_index(drop=True)
Season_orange_cap= Season_orange_cap.drop_duplicates(subset=["season"],keep="first").sort_values(by="season").reset_index(drop=True)
ax = Season_orange_cap.plot( x = 'season',y = 'batsman_runs',color='orange',kind='bar')
plt.xticks(rotation=80)
annot_plot(ax,0,10)
Season_orange_cap


# <h2>Bowler Analysis</h2>

# In[35]:


temp_data = delivery_data.groupby('bowler')['ball'].agg('count').reset_index().sort_values(by='ball', ascending=False).reset_index(drop=True)
temp_data = temp_data.iloc[:10,:]

labels = np.array(temp_data['bowler'])
ind = np.arange(len(labels))
width = 0.5
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(temp_data['ball']), width=width, color='blue')
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel("Count")
ax.set_title("Top Bowlers - Number of balls bowled in IPL")
ax.set_xlabel('Bowler Names')
plt.show()


# In[36]:


temp_data = delivery_data.groupby('bowler')['total_runs'].agg(lambda x: (x==0).sum()).reset_index().sort_values(by='total_runs', ascending=False).reset_index(drop=True)
temp_data = temp_data.iloc[:10,:]

labels = np.array(temp_data['bowler'])
ind = np.arange(len(labels))
width = 0.5
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(temp_data['total_runs']), width=width, color='blue')
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel("Count")
ax.set_title("Top Bowlers - Number of dot balls bowled in IPL")
ax.set_xlabel('Bowler Names')
plt.show()


# In[37]:


temp_data = delivery_data.groupby('bowler')['extra_runs'].agg(lambda x: (x>0).sum()).reset_index().sort_values(by='extra_runs', ascending=False).reset_index(drop=True)
temp_data = temp_data.iloc[:10,:]

labels = np.array(temp_data['bowler'])
ind = np.arange(len(labels))
width = 0.5
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(temp_data['extra_runs']), width=width, color='blue')
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel("Count")
ax.set_title("Bowlers with more extras in IPL")
ax.set_xlabel('Bowler Names')
plt.show()


# In[38]:


wicket_bowler = delivery_data.groupby(['bowler'])['player_dismissed'].count()
wicket_bowler.sort_values(ascending=False,inplace=True)
wicket_bowler[:15].plot(kind='bar')


# In[39]:


runs_bowler = delivery_data.groupby(['bowler'])['total_runs'].sum()
runs_bowler.sort_values(ascending=False,inplace=True)
runs_bowler[:10].plot(kind='bar')


# <h2>Purple Cap Winners</h2>

# In[40]:


Season_purple_cap=complete_data[complete_data["dismissal_kind"]!="run out"]
Season_purple_cap=complete_data.groupby(["season","bowler"])["dismissal_kind"].count().reset_index().sort_values(by="dismissal_kind",ascending=False).reset_index(drop=True)
Season_purple_cap= Season_purple_cap.drop_duplicates(subset=["season"],keep="first").sort_values(by="season").reset_index(drop=True)
Season_purple_cap.columns= ["Season","Bowler","Wicket_taken"]
ax=Season_purple_cap.plot('Season','Wicket_taken',color='purple',kind='bar')
plt.xticks(rotation=80)
annot_plot(ax,0,1)
Season_purple_cap


# <h2>IPL Finals</h2>

# In[41]:


final_matches.groupby(['city','winner']).size()


# <h2>Number of IPL Seasons won by Teams</h2>

# In[42]:


final_matches[['toss_winner','toss_decision','winner']].reset_index(drop=True)


# Obeservation:
# 
# * 7 out of 10 times the team that won the toss in the finals also won the finals.

# <h2>Top Umpires</h2>

# In[43]:


temp_data = pd.melt(match_data, id_vars=['id'], value_vars=['umpire1', 'umpire2'])

temp_series = temp_data.value.value_counts()[:10]
labels = np.array(temp_series.index)
ind = np.arange(len(labels))
width = 0.9
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(temp_series), width=width,)
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel("Count")
ax.set_title("Top Umpires")
plt.show()

