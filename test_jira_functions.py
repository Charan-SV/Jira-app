# test_jira_functions.py

import unittest
from unittest.mock import patch, Mock
import json  # Import the missing json module
from jira_functions import get_projects

class TestJiraFunctions(unittest.TestCase):

    @patch('jira_functions.requests.get')
    def test_get_projects_success(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            'values': [
                {
                    'name': 'Project 1',
                    'key': 'P1',
                    'insight': {
                        'totalIssueCount': 10,
                        'lastIssueUpdateTime': '2023-01-01T00:00:00.000Z'
                    }
                },
                {
                    'name': 'Project 2',
                    'key': 'P2',
                    'insight': {
                        'totalIssueCount': 5,
                        'lastIssueUpdateTime': '2023-01-02T00:00:00.000Z'
                    }
                }
            ]
        })
        mock_get.return_value = mock_response

        # Capture the output
        with patch('builtins.print') as mock_print:
            get_projects()
            mock_print.assert_called()
            output = [call.args for call in mock_print.call_args_list]
        
        print("\n test_get_projects_success passed with output: \n")
        for line in output:
            print(line[0])

    @patch('jira_functions.requests.get')
    def test_get_projects_no_projects(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({'values': []})
        mock_get.return_value = mock_response

        # Capture the output
        with patch('builtins.print') as mock_print:
            get_projects()
            mock_print.assert_called()
            output = [call.args for call in mock_print.call_args_list]
        
        print("\n test_get_projects_no_projects passed with output:\n")
        for line in output:
            print(line[0])

    @patch('jira_functions.requests.get')
    def test_get_projects_api_failure(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = json.dumps({'errorMessages': ['Internal Server Error']})
        mock_get.return_value = mock_response

        # Capture the output
        with patch('builtins.print') as mock_print:
            get_projects()
            mock_print.assert_called()
            output = [call.args for call in mock_print.call_args_list]
        
        print("\n test_get_projects_api_failure passed with output:\n")
        for line in output:
            print(line[0])

if __name__ == '__main__':
    unittest.main()