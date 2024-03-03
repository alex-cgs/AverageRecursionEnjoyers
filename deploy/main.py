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
            

            

@sp.add_test()
def test():
    scenario = sp.test_scenario("Minimal", [transport, main])
    scenario.h1("Minimal")
    alice_address = sp.test_account("alice")
    bob_address = sp.test_account("bob")
    c1 = main.MainContract(params = sp.record(buyer_address="some house", destination="Uni.Lu", 
                           contract_deadline="after the hackathon", transport_deadline="after the hackathon",
                          winner_address="some house", origin="hackathon"))
    c2 = transport.TransportContract(params = sp.record(buyer_address="some house", destination="Uni.Lu", 
                           contract_deadline="somewhen", transport_deadline="somewhen",
                          winner_address="some house", origin="hackathon"))
    scenario += c1
    scenario += c2
    c2.participate(price = sp.tez(100), winner_address = "not LUX", origin = "Belarus")
    c1.participate(price = sp.tez(80), winner_address = "Bakhmut", origin = "Ukraine")
