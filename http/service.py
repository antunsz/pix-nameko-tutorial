import json
from nameko.web.handlers import http
from nameko.rpc import  rpc, RpcProxy
from werkzeug import Response

class HttpService:

    name = "HttpSerivce"
    service_bank1 = RpcProxy('Bank1')

    @http('POST', '/transfer')
    def post(self, request):
        print(request.data)
        data = json.loads(request.data)
        response = self.service_bank1.transfer(
            data['user1'],
            data['user2'],
            data['value']
        )

        return Response(json.dumps(response), status=201, mimetype='application/json')
