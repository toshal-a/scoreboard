from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

"""TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}"""
overs = {
	'over1':{
		'ball1':{
			'run': 6,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball2':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball3':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball4':{
			'run': 3,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball5':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball6':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
	},
	'over2':{
		'ball1':{
			'run': 1,
			'wicket':False,
			'extra':None,
			'player_id': 2,
		},
		'ball2':{
			'run': 1,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball3':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 2,
		},
		'ball4':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 2,
		},
		'ball5':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 2,
		},
		'ball6':{
			'run': 3,
			'wicket':False,
			'extra':None,
			'player_id': 2,
		},
	},
	'over3':{
		'ball1':{
			'run': 0,
			'wicket':False,
			'extra':'WD',
			'player_id': 1,
		},
		'ball2':{
			'run': 4,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball3':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball4':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball5':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball6':{
			'run': 3,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		}
	},
	'over4':{
		'ball1':{
			'run': 1,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball2':{
			'run': 1,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball3':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball4':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball5':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball6':{
			'run': 3,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
	},
	'over5':{
		'ball1':{
			'run': 1,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball2':{
			'run': 1,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball3':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball4':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball5':{
			'run': 0,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
		'ball6':{
			'run': 3,
			'wicket':False,
			'extra':None,
			'player_id': 1,
		},
	},

}
overSummary={
	'over1':{
		'runs':9,
		'wickets':0,
		'Extras':0,
		'player1 score':9,
		'player2 score':0,
	},
	'over2':{
		'runs':5,
		'wickets':0,
		'Extras':0,
		'player1 score':11,
		'player2 score':4,
	},
	'over3':{
		'runs':9,
		'wickets':0,
		'Extras':0,
		'player1 score':9,
		'player2 score':0,
	},
	'over4':{
		'runs':10,
		'wickets':110,
		'Extras':0,
		'player1 score':190,
		'player2 score':111,
	},
	'over5':{
		'runs':9,
		'wickets':0,
		'Extras':0,
		'player1 score':9,
		'player2 score':0,
	}
}
matchSummary= {
	'runs':50,
	'wickets':3,
	'Extras':13,
	'player1 score':22,
	'player2 score':28,
}
def abort_if_over_doesnt_exist(over_id):
	if over_id not in overSummary:
		abort(404, message="Over {} doesn't exist".format(over_id))

parser = reqparse.RequestParser()
parser.add_argument('over_num',type = int)
parser.add_argument('ball_num',type = int)
parser.add_argument('run',type = int)
parser.add_argument('wicket',type = bool)
parser.add_argument('extra',type = str)
parser.add_argument('player_id',type = int)

# Todo
# shows a single todo item and lets you delete a todo item
class OverInfo(Resource):
	def get(self,over_id):
		over_id='over%i' % over_id
		abort_if_over_doesnt_exist(over_id)
		return overSummary[over_id]

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class MatchInfo(Resource):
	def get(self):
		return overs
	def post(self):
		args = parser.parse_args()
		over_num = args['over_num']
		ball_num = args['ball_num']
		run = args['run']
		wicket = args['wicket']
		extra = args['extra']
		player_id = args['player_id']

		over_num='over%i' % over_num
		ball_num='ball%i' % ball_num

		if not overs.get(over_num,0):
			overs[over_num]={}
		overs[over_num][ball_num] = {
			'run': run,
			'wicket':wicket,
			'extra':extra,
			'player_id': player_id,
		}
		return overs[over_num][ball_num], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(MatchInfo, '/match')
api.add_resource(OverInfo, '/over/<int:over_id>')

if __name__ == '__main__':
	app.run(debug=True)
