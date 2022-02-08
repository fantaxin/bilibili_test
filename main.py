import pytest

if __name__ == '__main__':
    command_line = ["-s", "test.py", "--alluredir=data"]
    # command_line = ["allure", "generate", "data"]
    pytest.main(command_line)

#  allure serve data
