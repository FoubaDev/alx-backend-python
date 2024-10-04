# 0x03. Unittests and Integration Tests
In this project, I learned :

* The difference between unit and integration tests.
* Common testing patterns such as mocking, parametrizations and fixtures



## Function Prototypes :

Prototypes for functions written in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `test_utils.py`        |                        |
| `test_client.py`            |                                       |
| `test_utils.py`        |                        |

## Tasks :

* **0. Parameterize a unit testr**
  * [test_utils.py](./test_utils.py): 
  Familiarize yourself with the __utils.access_nested_map__ function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for __utils.access_nested_map__.

Create a __TestAccessNestedMap__ class that inherits from __unittest.TestCase__.

Implement the __TestAccessNestedMap.test_access_nested_map__ method to test that the method returns what it is supposed to.


* **1. Parameterize a unit test**
 Implement __TestAccessNestedMap.test_access_nested_map_exception__. Use the __assertRaises__ context manager to test that a __KeyError__ is raised for the following inputs (use __@parameterized.expand__)

* **2. Mock HTTP calls**
  * [test_utils.py](./test_utils.py):
Familiarize yourself with the __utils.get_json__ function.

Define the __TestGetJson(unittest.TestCase)__ class and implement the __TestGetJson.test_get_json__ method to test that __utils.get_json__ returns the expected result.

* **3. Parameterize and patch**
  * [test_utils.py](./test_utils.py):
Read about memoization and familiarize yourself with the __utils.memoize__ decorator.

Implement the __TestMemoize(unittest.TestCase)__ class with a __test_memoize method__.

Inside __test_memoize__, define following class


* **4. Parameterize and patch as decorators**
  * [test_client.py](./test_client.py):
Familiarize yourself with the c__lient.GithubOrgClient__ class.

In a new __test_client.py__ file, declare the __TestGithubOrgClient(unittest.TestCase)__ class and implement the __test_org__ method.

This method should test that __GithubOrgClient.org__ returns the correct value.

Use __@patch__ as a decorator to make sure __get_json__ is called once with the expected argument but make sure it is not executed.

Use __@parameterized.expand__ as a decorator to parametrize the test with a couple of org examples to pass to __GithubOrgClient__, in this order:
* google
* abc

Of course, no external HTTP calls should be made.

* **5. Mocking a property**
  * [test_client.py](./test_client.py):
__memoize__ turns methods into properties. Read up on how to mock a property (see resource).

Implement the __test_public_repos_url__ method to unit-test __GithubOrgClient._public_repos_url__.

Use __patch__ as a context manager to patch __GithubOrgClient.org__ and make it return a known payload.

Test that the result of ___public_repos_url__ is the expected one based on the mocked payload.



* **6. More patching**
  * [test_client.py](./test_client.py):
Implement __TestGithubOrgClient.test_public_repos__ to unit-test __GithubOrgClient.public_repos__.

Use __@patch__ as a decorator to mock get_json and make it return a payload of your choice.

Use patch as a context manager to mock __GithubOrgClient._public_repos_url__ and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked get_json was called once.

* **7. Parameterize**
  * [test_client.py](./test_client.py):
Implement __TestGithubOrgClient.test_has_license__ to __unit-test__ GithubOrgClient.has_license.

Parametrize the test with the following inputs



* **8. Integration test: fixtures**
  * [test_client.py](./test_client.py):
We want to test the __GithubOrgClient.public_repos__ method in an integration test. That means that we will only mock code that sends external requests.

Create the __TestIntegrationGithubOrgClient(unittest.TestCase)__ class and implement the __setUpClass__ and __tearDownClass__ which are part of the __unittest.TestCase__ API.