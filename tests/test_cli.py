from piccolino.cli import main
import sys
import pytest


def test_main_cli():
    if len(sys.argv) <= 1:
        with pytest.raises(SystemExit):
            main()
    else:
        pass
