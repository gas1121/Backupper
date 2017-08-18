import unittest
from unittest.mock import patch

import arrow

from run import main


class TestRun(unittest.TestCase):
    @patch('run.ByPy')
    @patch('run.subprocess.run')
    def test_main(self, run_mock, bypy_mock):
        date = arrow.now().format('YYYYMMDD')
        main()
        sync = '/sync/archive-' + date + '.7z'
        run_mock.assert_called_once_with(['7z', 'a', sync, '/backup/'])
        bypy_mock().syncup.assert_called_once_with(
            localdir='/sync/', remotedir='/sync/')
