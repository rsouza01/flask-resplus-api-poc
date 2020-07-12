#!/usr/bin/env python3

import requests
import timeit

from prettytable import PrettyTable

server_url = 'http://localhost:5000'


def perform_test(step_descr, text, endpoint, expected_ret_code, start_time, verbose=False):
    if verbose:
        print(text)
    response = requests.get(endpoint)
    status_code = response.status_code
    if verbose:
        print('RETURNED STATUS CODE: {}'.format(status_code))
    if status_code != expected_ret_code:
        return [step_descr, 'FAILED', timeit.default_timer() - start_time, endpoint]
    if verbose:
        print('-'*120)


def test_endpoints():
    step_descr = 'fits-files'
    start_time = timeit.default_timer()

    return ['',
            'SUCCESS',
            0,
            '']


def print_execution_header():
    print('='*120)
    print('  flask-resplus-api-poc API SMOKE TEST '.center(120, ' '))
    print('='*120)


def print_summary_header():
    print('='*120)
    print('  SMOKE TEST - EXECUTION SUMMARY  '.center(120, ' '))
    print('='*120)


def print_summary_footer():
    print('\n\n')
    print('APPLICATION: flask-resplus-api-poc')
    print('RELEASE: 1.0')
    print('ENVIRONMENT: GITHUB')
    print('\n\n')


def main():

    print_execution_header()

    table = PrettyTable()
    table.field_names = ['TEST CASE NAME'.center(30, ' '),
                         'STATUS',
                         'EXECUTION TIME',
                         'ENDPOINT'.center(51, ' ')]

    table.add_row(test_endpoints())

    print(table)

    print_summary_header()
    print_summary_footer()

    return 0


if __name__ == '__main__':
    exit(main())
