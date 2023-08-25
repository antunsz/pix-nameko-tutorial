import json 
from nameko.rpc import rpc, RpcProxy

class Bank2:
    name = 'Bank2'

    bank1_service = RpcProxy('Bank1')

    @rpc
    def transfer(self, user1, user2, value):
        return self.bank1_service.transfer(user1, user2, value)
