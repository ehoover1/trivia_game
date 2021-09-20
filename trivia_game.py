import pandas as pd 
import numpy as np
from pandasql import sqldf

pysqldf = lambda q: sqldf(q, globals())   

trivia = pd.read_csv('JEOPARDY_CSV.csv').iloc[ :, 3:7]  # load only needed portion of csv

# use SQL syntax to weed out junk questions; questions using images only contain HTML tag, need to be discarded
trivia = pysqldf("SELECT * FROM trivia WHERE trivia.' Question' NOT LIKE '%href%';")            
        
for i in range(0, len(trivia)):

    #  clean and update numeric data types
    trivia.iloc[i, 1] = trivia.iloc[i, 1].replace('$', '')
    trivia.iloc[i, 1] = trivia.iloc[i, 1].replace(',', '')
    if trivia.iloc[i, 1] == 'None':
        trivia.iloc[i, 1] = 1000
    trivia.iloc[i, 1] = int(trivia.iloc[i, 1])      

class Trivia:
    def __init__(self, index):
        self.team = 'alpha'
        self.score = {'alpha': 0, 'omega': 0}
        self.category = trivia.iloc[index, 0]
        self.points = trivia.iloc[index, 1]
        self.question = trivia.iloc[index, 2]
        self.answer = trivia.iloc[index, 3]

    def roll(self):
        if self.team == 'alpha':
            self.team = 'omega'
        else:
            self.team = 'alpha' 
        index = np.random.randint(0, len(trivia))
        self.category = trivia.iloc[index, 0]
        self.points = trivia.iloc[index, 1]
        self.question = trivia.iloc[index, 2]
        self.answer = trivia.iloc[index, 3]
        
    def q(self):
        print(f'Team {self.team.title()}??\n\n{self.category} for {self.points} points: \n')
        print(f'{self.question}')

    def a(self):
        print(self.answer.upper())

    def yes(self):
        if self.team == 'alpha':
            self.score['alpha'] += self.points
        if self.team == 'omega':
            self.score['omega'] += self.points
        print(self.score)
        if self.score['alpha'] >= 5000:
            print('GAME OVER! TEAM ALPHA WINS!!')
            self.score = {'alpha': 0, 'omega': 0}
        if self.score['omega'] >= 5000:
            print('GAME OVER! TEAM OMEGA WINS!!')
            self.score = {'alpha': 0, 'omega': 0}
        
game = Trivia(np.random.randint(0, len(trivia)))  # instatiate game
