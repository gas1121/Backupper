import unittest
from unittest.mock import patch, mock_open
import os

from run import backup_job, main


class TestRun(unittest.TestCase):
    @patch.dict(os.environ, {
        "ARCHIVE_NAME_PREFIX": "archive",
        "ARCHIVE_PASS": ""})
    @patch("run.docker")
    def test_backup_job(self, docker_mock):
        m = mock_open(read_data='a=b')
        m.return_value.__iter__ = lambda self: self
        m.return_value.__next__ = lambda self: next(iter(self.readline, ''))
        with patch('run.open', m):
            backup_job()
        m.assert_called_once_with('/data/data.txt', 'r')
        expect_volumes = {
            'backupper_bypy': {'bind': '/root/.bypy', 'mode': 'rw'},
            'a': {'bind': '/backup/b', 'mode': 'rw'},
        }
        expect_env = {
            "ARCHIVE_NAME_PREFIX": "archive",
            "ARCHIVE_PASS": ""
        }
        docker_mock.DockerClient().containers.run.assert_called_once_with(
            'backupper', environment=expect_env, volumes=expect_volumes)
        m.reset_mock()
        docker_mock.reset_mock()

        m = mock_open(read_data='a')
        m.return_value.__iter__ = lambda self: self
        m.return_value.__next__ = lambda self: next(iter(self.readline, ''))
        with patch('run.open', m):
            backup_job()
        m.assert_called_once_with('/data/data.txt', 'r')
        docker_mock.DockerClient().containers.run.assert_not_called()

    @patch('run.backup_job')
    @patch('run.start_scheduler')
    def test_main(self, start_scheduler_mock, backup_job_mock):
        main(["--run"])
        backup_job_mock.assert_called_once()
        start_scheduler_mock.assert_not_called()
        backup_job_mock.reset_mock()
        start_scheduler_mock.reset_mock()

        main([])
        start_scheduler_mock.assert_called_once()
        backup_job_mock.assert_not_called()
