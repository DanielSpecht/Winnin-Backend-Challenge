from flask_restful_swagger_2 import swagger, Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime

from os.path import *
import sys
sys.path.append(join(dirname(__file__), ".."))
from request_response import ListPostsRequest
from use_cases import ListPostsUseCase

class PostResource(Resource):
    @swagger.doc({
        'description': "Returns a list of posts in the time period defined by 'start' and end parameters. The results are ordered acording to the value of 'order parameter'",
        'parameters': [{ 'name': 'order',
                         'description': 'Indicates the attribute used to order the list of posts',
                         'in':'query',
                         'required':True,
                         'enum': ['ups','comments'],
                         'type': 'string'},

                       { 'name': 'start',
                         'description': 'The date that indicates the start of the period',
                         'in':'query',
                         'required':True,
                         'type': 'date'},

                       { 'name': 'end',
                         'description': 'The date that indicates the end of the period',
                         'in':'query',
                         'required':True,
                         'type': 'date'}],

        'responses': {'200': {'description': 'Successfully obtained a list of posts matching the period of time and ordered according to the specified criteria.'}}})
    def get(self):
        
        # parse inputs
        parser = RequestParser(bundle_errors=True)
        
        date_format = '%d-%m-%Y'
        date_type = lambda x: datetime.strptime(x, date_format)
        order_options = ('ups','comments')
        parser.add_argument('order', choices = order_options, help = '{error_msg}. Possible values for parameter are: %s'%(str(order_options)), required = True)
        parser.add_argument('start', required = True, type = date_type)
        parser.add_argument('end', required = True, type = date_type )
        args = parser.parse_args()

        if args['start'] > args['end']:
            return {'message': "The 'start' param must be a date prior to the date 'end' param"}, 400
        
        # get data
        request = ListPostsRequest(args['order'], args['start'], args['end'])
        uc = ListPostsUseCase()
        response = uc.execute(request)

        # internal errors during execution
        if response.has_errors:
            return response.errors, 500

        posts = [p.to_dict() for p in response.data]
        return posts
