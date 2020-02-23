# pylint: disable=R0903,W0401,W0614
'''UnitTests for basic operations module.'''
from unittest import TestCase
from peewee import *
from basic_operations import *
from customer_model import Customer, DB

class TestBasicOperations(TestCase):
    '''Unit test class for testing basic_operations.'''

    def setUp(self):
        '''setup tests'''
        self.database = DB
        self.database.drop_tables([Customer])
        self.database.create_tables([Customer])
        self.database.close()

        self.customer1 = {
            'customer_id': "Dexter",
            'name': 'Dexter',
            'lastname': 'Hamilton',
            'home_address': 'amkytflseg',
            'phone_number': '218-3604-29',
            'email_address': 'd.hamilton@washington.edu',
            'status': True,
            'credit_limit': 62649
        }
        self.customer2 = {
            'customer_id': "Carina",
            'name': 'Carina',
            'lastname': 'Bailey',
            'home_address': 'qkcuxswpmi',
            'phone_number': '914-4365-64',
            'email_address': 'c.bailey@aol.com',
            'status': True,
            'credit_limit': 81073
        }
        self.customer3 = {
            'customer_id': "Vanessa",
            'name': 'Vanessa',
            'lastname': 'Allen',
            'home_address': 'hlrxsenuzy',
            'phone_number': '857-5470-62',
            'email_address': 'v.allen@hotmail.com',
            'status': True,
            'credit_limit': 132266
        }
        self.customer4 = {
            'customer_id': "John",
            'name': 'John',
            'lastname': 'Adams',
            'home_address': 'tydzdtvgaf',
            'phone_number': '945-2288-69',
            'email_address': 'j.adams@gmail.com',
            'status': True,
            'credit_limit': 155810
        }
        self.customer5 = {
            'customer_id': "Valeria",
            'name': 'Valeria',
            'lastname': 'Tucker',
            'home_address': 'xszgdfovzd',
            'phone_number': '561-8608-77',
            'email_address': 'v.tucker@uw.edu',
            'status': True,
            'credit_limit': 83351
        }


    def test_add_customer(self):
        '''test add_customer function.'''
        add_customer(**self.customer1)
        check = Customer.get(Customer.customer_id == 'Dexter')
        self.assertEqual(check.credit_limit, 62649)
        self.customer1['credit_limit'] = 99999
        add_customer(**self.customer1)
        #Peewee does not generate error on attempting to duplicate ID.
        #Simply verify value has not changed.
        self.assertEqual(check.credit_limit, 62649)


    def test_search_customer(self):
        '''test search_customer function.'''
        add_customer(**self.customer2)
        result = search_customer('Carina')
        result_false = search_customer('Carina2')
        self.assertEqual(result, self.customer2)
        self.assertEqual(result_false, {})


    def test_delete_customer(self):
        '''test delete_customer function.'''
        add_customer(**self.customer3)
        before_delete = search_customer('Vanessa')
        delete_customer('Vanessa')
        after_delete = search_customer('Vanessa')
        self.assertEqual(before_delete, self.customer3)
        self.assertEqual(after_delete, {})
        #Delete non-existant ID does not generate error.
        delete_customer('Vanessa3')


    def test_update_customer_credit(self):
        '''test updating customer credit limit.'''
        add_customer(**self.customer4)
        self.assertEqual(Customer.get(Customer.customer_id == 'John').credit_limit, 155810)
        update_customer_credit('John', 200000)
        self.assertEqual(Customer.get(Customer.customer_id == 'John').credit_limit, 200000)
        with self.assertRaises(ValueError):
            update_customer_credit('John2', 1000)


    def test_list_active_customers(self):
        '''test list_active_customers function.'''
        add_customer(**self.customer1)
        add_customer(**self.customer2)
        self.assertEqual(list_active_customers(), 2)
        add_customer(**self.customer3)
        self.assertEqual(list_active_customers(), 3)


    def test_failing_test(self):
        '''Add failing test.'''
        #Instructions say to show some tests failing:
        self.assertEqual(1, 2)
