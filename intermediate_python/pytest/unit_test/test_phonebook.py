import unittest
from phonebook import Phonebook

#Test fixture for strict unit test 
#1. setUp()
#2. TestCaseMethod()
#3. tearDown()
class PhonebookTest(unittest.TestCase): #declare a class containing tests
    def setUp(self) -> None: #set up fixture method
        self.phonebook = Phonebook()

    def tearDown(self) -> None: #tear down fixture method
        pass

    #test for looking up a name
    def test_lookup_by_name(self): #first test case  <- test case name
        self.phonebook.add("Bob", "12345678") #     <- arrange
        number = self.phonebook.lookup("Bob")#      <- act
        self.assertEqual(number, "12345678")#           <- assert

    #test for missiong name 
    def test_missing_name(self): #second test case
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
    
    #empty phonebook if it is consistent
    def test_empty_phonebook_is_consistent(self): #third test case 
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    def test_is_consistent_with_different_entries(self):
         self.phonebook.add("Bob", "12345678") #   <-- test case name and arrange
         self.phonebook.add("Anna", "23456789")
         self.assertTrue(self.phonebook.is_consistent())
        
    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345678") #   
        self.phonebook.add("Sue", "12345678") #identical to Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345678") #   
        self.phonebook.add("Sue", "123") #prefix of Bob
        self.assertFalse (self.phonebook.is_consistent())

    