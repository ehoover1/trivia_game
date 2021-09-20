# trivia_game

The inception of this project dates back to the quarantine period of Spring 2020. A group of friends and I enjoyed going out and playing bar trivia on
Monday nights before the pandemic. In the several months that bars and restaurants were closed to the public, we had the idea to start a trivia night over Zoom.

We wanted a game with enough questions for us to play several times without getting repeats, and we also wanted to avoid dedicating a person to curate the questions by 
hand each game. So I began to look for an online trivia game that met these criteria. Much to my surprise, I found NOTHING close to what we envisioned.

What I did find, however, was a .csv file containing 200,000+ trivia questions taken from previously aired *Jeopardy!* episodes. I decided that I would build an 
application that incorporated these questions into a serviceable 'trivia-host-bot' to employ for our Zoom trivia nights.

controls:

game.q() .. .. display question for answering team

game.a() .. .. after team answers, displays correct answer

game.yes() .. .. IF the asking team is satisfied with the given answer, attributes appropriate number of points to answering team

game.roll() .. .. switch asking/answering teams, and randomly draws new question
