from abc import ABC, abstractmethod

from entities.account_class_information import account
class accountDAOinterface(ABC:)

# create
    @abstractmethod
    def create_account(self, account:account)-> Account:

    pass
#read

    def get_account_information(self_account_id:int)
        pass

#update
def update_account_by_id(self_account:account):
    pass
#delete
def delete_account_by_id(self,account_id:int)
    pass