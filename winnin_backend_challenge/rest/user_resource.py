from flask_restful_swagger_2 import swagger, Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime

from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))

from request_response import ListUsersRequest
from use_cases import ListUsersUseCase

class UserResource(Resource):
    @swagger.doc({
        'description': "Returns a list of users. The results are ordered acording to the value of 'order parameter'",
        'parameters': [{ 'name': 'order',
                         'description': 'Indicates the attribute used to order the list of posts',
                         'in':'query',
                         'required':True,
                         'enum': ['ups','comments'],
                         'type': 'string'}],

        'responses': {'200': {'description': 'Successfully obtained a list of users ordered according to the specified criteria'}}})

    def get(self):
        # parse inputs
        parser = RequestParser(bundle_errors=True)
        order_options = ('ups','comments')
        parser.add_argument('order', choices = order_options, help = '{error_msg}. Possible values for parameter are: %s'%(str(order_options)), required = True)
        args = parser.parse_args(strict=True)
        
        # get data
        request = ListUsersRequest(args.get('order'))
        uc = ListUsersUseCase()
        response = uc.execute(request)

        # internal errors during execution
        if response.has_errors:
            return response.errors, 500

        users =  [u.to_dict() for u in response.data]

        return users