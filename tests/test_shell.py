import unittest
from src.parser import parse_command
from src.commands import cmd_ls, cmd_cd, cmd_exit


class TestParser(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(parse_command(""))

    def test_simple_command(self):
        result = parse_command("ls")
        self.assertEqual(result, ["ls"])

    def test_command_with_args(self):
        result = parse_command("ls -la /home")
        self.assertEqual(result, ["ls", "-la", "/home"])

    def test_double_quotes(self):
        result = parse_command('ls "file name"')
        self.assertEqual(result, ["ls", "file name"])

    def test_single_quotes(self):
        result = parse_command("cd 'my dir'")
        self.assertEqual(result, ["cd", "my dir"])

    def test_unclosed_quote(self):
        with self.assertRaises(ValueError):
            parse_command('ls "unclosed')


class TestCommands(unittest.TestCase):
    def test_ls_no_args(self):
        cmd_ls([])

    def test_ls_with_args(self):
        cmd_ls(["-la", "/home"])

    def test_cd_no_args(self):
        cmd_cd([])

    def test_exit_returns_true(self):
        self.assertTrue(cmd_exit([]))


if __name__ == "__main__":
    unittest.main()