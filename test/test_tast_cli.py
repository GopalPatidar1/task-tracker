import sys
from unittest.mock import patch
from app.task_cli import main


def test_main_without_arguments():
    with patch.object(sys, "argv", [
        'main.py'
    ]):
      result = main()
      assert result == "no arguments passed"
