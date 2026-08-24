import sys
from unittest.mock import patch
from app.task_cli import main
from app.constant import RESULT
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).parent.parent
testFilePath = PROJECT_ROOT / "test_task.txt"

@pytest.fixture(scope="module")
def test_file():
    # Setup
    testFilePath.write_text("[]")
    yield testFilePath

    # Cleanup
    if testFilePath.exists():
        testFilePath.unlink()

def test_main_without_arguments(test_file):
    with patch.object(sys, "argv", [
        'main.py'
    ]):
      result = main(testFilePath)
      assert result == RESULT["NO_ARGUMENTS"]()

def test_add_task(test_file):
    with patch.object(sys, "argv", [
        'main.py',
        'add',
        'add task by test'
    ]):
      result = main(test_file)
      assert result == RESULT["TASK_ADDED"](1)

def test_update_task(test_file):
    with patch.object(sys, "argv", [
        'main.py',
        'update',
        '1',
        'update task by test'
    ]):
      result = main(test_file)
      assert result == RESULT["TASK_UPDATED"](1)


def test_mark_in_progress(test_file):
    with patch.object(sys, "argv", [
        'main.py',
        'mark-in-progress',
        '1'
    ]):
      result = main(test_file)
      assert result == RESULT["TASK_UPDATED"](1)


def test_mark_done(test_file):
    with patch.object(sys, "argv", [
        'main.py',
        'mark-done',
        '1'
    ]):
      result = main(test_file)
      assert result == RESULT["TASK_UPDATED"](1)

def test_delete(test_file):
    with patch.object(sys, "argv", [
        'main.py',
        'delete',
        '1'
    ]):
      result = main(test_file)
      assert result == RESULT["TASK_DELETED"](1)