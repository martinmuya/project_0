 """This module contains account dao unit tests"""

from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from entities.account_class_information import account

account_dao = AccountDAOImp()

""" create account tests
business logic:
 Accounts may not be the same,
 Accounts may have different account number.
 """
 def test_create_account_success():
  test_account = account(0,"checking","savings")
  result = account_dao.create_account(test_account)
  assert result.account_id !=0

 def test_catch_non_unique_id():
  test_account =Account(1,"loan",)