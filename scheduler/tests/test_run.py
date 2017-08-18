import unittest
from unittest.mock import patch, mock_open

from run import backup_job


class TestRun(unittest.TestCase):
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
        docker_mock.DockerClient().containers.run.assert_called_once_with(
            'backupper', volumes=expect_volumes)
        m.reset_mock()
        docker_mock.reset_mock()

        m = mock_open(read_data='a')
        m.return_value.__iter__ = lambda self: self
        m.return_value.__next__ = lambda self: next(iter(self.readline, ''))
        with patch('run.open', m):
            backup_job()
        m.assert_called_once_with('/data/data.txt', 'r')
        docker_mock.DockerClient().containers.run.assert_not_called()
