# trivia_game

very simple trivia game made to be played with friends over Zoom. Questions sources from a .csv file of questions from episodes of Jeopardy.

controls:

game.q() .. .. display question for answering team

game.a() .. .. after team answers, displays correct answer

game.yes() .. .. IF the asking team is satisfied with the given answer, attributes appropriate number of points to answering team. Ends game once one of the two teams
reaches 5,000 points.

game.roll() .. .. switch asking/answering teams, and randomly draws new question
