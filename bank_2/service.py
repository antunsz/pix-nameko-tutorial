import json 
from nameko.rpc import rpc, RpcProxy

class Bank2:
    name = 'Bank2'

    @rpc
    def transfer(user1, user2, value):
        return f'{user1} -> {user2} : {value}'
