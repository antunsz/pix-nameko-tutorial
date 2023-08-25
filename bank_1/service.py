import json, random, string
from nameko.rpc import rpc, RpcProxy
import logging

class Bank1:
    name = 'Bank1'

    @rpc
    def transfer(self, user1, user2, value):
        return f'{user1} -> {user2} : $ {value}'
