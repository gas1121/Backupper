import unittest
from unittest.mock import patch
import os

import arrow

from run import main


class TestRun(unittest.TestCase):
    @patch.dict(os.environ, {"ARCHIVE_NAME_PREFIX": "archive"})
    @patch('run.ByPy')
    @patch('run.subprocess.run')
    def test_main(self, run_mock, bypy_mock):
        date = arrow.now().format('YYYYMMDD')
        main()
        sync = '/sync/archive-' + date + '.7z'
        run_mock.assert_called_once_with(['7z', 'a', sync, '/backup/'])
        bypy_mock().syncup.assert_called_once_with(
            localdir='/sync/', remotedir='/sync/')
        run_mock.reset_mock()
        bypy_mock.reset_mock()

        with patch.dict(os.environ, {
                "ARCHIVE_NAME_PREFIX": "archive",
                "ARCHIVE_PASS": "pass"}):
            main()
            sync = '/sync/archive-' + date + '.7z'
            run_mock.assert_called_once_with(
                ['7z', 'a', sync, '/backup/', '-ppass'])
            bypy_mock().syncup.assert_called_once_with(
                localdir='/sync/', remotedir='/sync/')
