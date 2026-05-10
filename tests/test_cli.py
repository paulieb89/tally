import pytest
from tally.cli import cli


def test_add_creates_counter(runner):
    result = runner.invoke(cli, ["add", "tasks"])
    assert result.exit_code == 0
    assert "tasks: 1" in result.output


def test_add_increments(runner):
    runner.invoke(cli, ["add", "tasks"])
    result = runner.invoke(cli, ["add", "tasks"])
    assert result.exit_code == 0
    assert "tasks: 2" in result.output


def test_add_multiple_counters(runner):
    runner.invoke(cli, ["add", "tasks"])
    runner.invoke(cli, ["add", "bugs"])
    runner.invoke(cli, ["add", "tasks"])
    result = runner.invoke(cli, ["add", "tasks"])
    assert "tasks: 3" in result.output


def test_show_lists_counters(runner):
    runner.invoke(cli, ["add", "tasks"])
    runner.invoke(cli, ["add", "bugs"])
    result = runner.invoke(cli, ["show"])
    assert result.exit_code == 0
    assert "tasks: 1" in result.output
    assert "bugs: 1" in result.output


def test_reset_zeroes_counter(runner):
    runner.invoke(cli, ["add", "tasks"])
    runner.invoke(cli, ["add", "tasks"])
    result = runner.invoke(cli, ["reset", "tasks"])
    assert result.exit_code == 0
    assert "tasks: 0" in result.output


def test_reset_on_unknown_counter(runner):
    result = runner.invoke(cli, ["reset", "tasks"])
    assert result.exit_code == 0
    assert "tasks: 0" in result.output


def test_show_crashes_when_no_counters_exist(runner):
    # Bug: show raises FileNotFoundError on a fresh system.
    # Fix is to handle the missing-store case gracefully.
    result = runner.invoke(cli, ["show"])
    assert result.exit_code != 0
