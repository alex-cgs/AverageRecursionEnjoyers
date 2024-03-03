import smartpy as sp

@sp.module 
def transport():
    class TransportContract(sp.Contract):
        def __init__(self, params):
            self.data.buyer_address = params.buyer_address
            self.data.destination = params.destination
            self.data.contract_deadline = params.contract_deadline
            self.data.transport_deadline = params.transport_deadline 
            self.data.price = sp.tez(0)
            self.data.winner_address = params.winner_address
            self.data.origin = params.origin

        @sp.entrypoint
        def openContract(self, params): 
            self.data.buyer_address = params.buyer_address
            self.data.destination = params.destination
            self.data.contract_deadline = params.contract_deadline
            self.data.transport_deadline = params.transport_deadline 
            self.data.price = sp.tez(0)

        @sp.entrypoint
        def participate(self, params):
            if self.data.price == sp.tez(0) or params.price < self.data.price :
                self.data.price = params.price 
                self.data.winner_address = params.winner_address
                self.data.origin = params.origin
            

        # def closeContract 

@sp.module 
def main():
    class MainContract(sp.Contract): 
        def __init__(self, params):
            self.data.buyer_address = params.buyer_address
            self.data.destination = params.destination
            self.data.contract_deadline = params.contract_deadline
            self.data.transport_deadline = params.transport_deadline 
            self.data.price = sp.tez(0)
            self.data.winner_address = params.winner_address
            self.data.origin = params.origin

        @sp.entrypoint
        def openContract(self, params):
            self.data.buyer_address = params.buyer_address
            self.data.destination = params.destination
            self.data.contract_deadline = params.contract_deadline
            self.data.transport_deadline = params.transport_deadline 
            self.data.price = sp.tez(0)

        @sp.entrypoint
        def participate(self, params):
            if self.data.price == sp.tez(0) or params.price < self.data.price :
                self.data.price = params.price 
                self.data.winner_address = params.winner_address
                self.data.origin = params.origin
