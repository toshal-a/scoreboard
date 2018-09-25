from flask import Flask
from flask_restful import reqparse, abort, Api, Resource,inputs

app = Flask(__name__)
api = Api(app)
overs = {
	'over1':{
        'runs':9,
		'wickets':0,
		'extras':0,
		'player1_score':9,
		'player2_score':0,
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
}


def abort_if_over_doesnt_exist(over_id):
	if over_id not in overs:
		abort(404, message="Over {} doesn't exist".format(over_id))

parser = reqparse.RequestParser()
parser.add_argument('over_num',type=int)
parser.add_argument('ball_num',type=int)
parser.add_argument('run',type=int)
parser.add_argument('wicket',type=inputs.boolean)
parser.add_argument('extra',type=str)
parser.add_argument('player_id',type=int)

# Todo
# shows a single todo item and lets you delete a todo item
class OverInfo(Resource):
    def get(self,over_id):
        over_id='over%i' % over_id
        abort_if_over_doesnt_exist(over_id)
        tempOver ={}
        tempOver['runs']= overs[over_id]['runs']
        tempOver['wickets'] = overs[over_id]['wickets']
        tempOver['extras']= overs[over_id]['extras']
        tempOver['player1_score']=overs[over_id]['player1_score']
        tempOver['player2_score']=overs[over_id]['player2_score']
        return tempOver

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class MatchInfo(Resource):
    def get(self):
        matchSummary={}
        for ov in overs:
            matchSummary['runs'] =matchSummary.get('runs',0)+overs[ov]['runs']
            matchSummary['wickets'] =matchSummary.get('wickets',0)+overs[ov]['wickets']
            matchSummary['extras'] =matchSummary.get('extras',0)+overs[ov]['extras']
            matchSummary['player1_score'] =matchSummary.get('player1_score',0)+overs[ov]['player1_score']
            matchSummary['player2_score'] =matchSummary.get('player2_score',0)+overs[ov]['player2_score']
        return matchSummary
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
            overs[over_num]['runs']=0
            overs[over_num]['wickets']=0
            overs[over_num]['extras']=0
            overs[over_num]['player1_score']=0
            overs[over_num]['player2_score']=0

        if overs[over_num].get(ball_num,0)==0:
            overs[over_num][ball_num] = {
                'run': run,
                'wicket':wicket,
                'extra':extra,
                'player_id': player_id,
                }
            overs[over_num]['runs']+=run
            if wicket:
                overs[over_num]['wickets']+=1
                overs[over_num]['extras']+=1
            if player_id==1:
                overs[over_num]['player1_score']+=run
            else:
                overs[over_num]['player2_score']+=run
            return overs[over_num][ball_num], 201]
        else:
            return abort(404, message="Ball {} Already exist".format(over_id))
##
## Actually setup the Api resource routing here
##
api.add_resource(MatchInfo, '/match')
api.add_resource(OverInfo, '/over/<int:over_id>')

if __name__ == '__main__':
	app.run(debug=True)
