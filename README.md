# scoreboard
Requirents for the app are
  python=3.6.0
  flask=1.0.2
  flask-restful=0.3.6
The given app is hosted at 
walragatver.pythonanywhere.com

The following are endpoints for given app

1)To get details of a  over
  walragatver.pythonanywhere.com/over/over_number*
  
  e.g for over2 
      walragatver.pythonanywhere.com/over/2
      
2)To get details of a match
  walragatver.pythonanywhere.com/match
  
 3) To post a new ball use
  walragatver.pythonanywhere.com/match
  
Assumptions while making the app
 a) Each ball has run which are not counted in extra
 b) Oversummary has runs including extra runs
 c) There are only two players
 d) When there is "BYE" those runs will not be added in the player score
 e) An over summary will contain the no of runs made by a player during that over
 f) Match Summary will contain total runs and the number of extra runs in the total
 
