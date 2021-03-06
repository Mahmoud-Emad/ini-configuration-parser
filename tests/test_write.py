from pyini_parser.configure.parser import ConfigParser
from pyini_parser.errors.error import ErrorHandler
import pytest



config = ConfigParser()
error = ErrorHandler()

def define_config():
    config["deployment"] = {
        "domain_name": "www.example.com",
        "secretkey": "!@#$#$#@!!",
    }
    config["database"] = {
        "host": "localhost",
        "port": "3306",
        "user": "root",
    }
    config["email"] = {
        "host": "smtp.gmail.com",
        "port": "587",
    }
    config["devolvement"] = {
        "api_key": "!@#$%^&*()_+",
    }
    file = open("example.ini", "w")
    output = config.write(file)
    file.close()
    return output

def test_write():
    """Test write"""
    output = define_config()
    assert output == "example.ini written successfully"


def test_sections():
    """Test sections"""
    sections = config.sections()
    output = []
    for section in sections:
        output.append(section.lower())
    assert output == ["deployment", "database", "email", "devolvement"]

def test_get_found():
    """Test get"""
    assert config.get("deployment", "secretkey") == "!@#$#$#@!!"

def test_get_notfound():
    """Test get"""
    with pytest.raises(KeyError):
        config.get("database", "secretkey1")

def test_append_keys():
    """Test append keys"""
    config.append("deployment", {"test_append_key":"This is value"})
    assert config.get("deployment", "test_append_key") == "This is value"

def test_append_wrong_type():
    """Test append wrong type"""
    with pytest.raises(TypeError):
        config.append("deployment", ("test_append_key_2", "This is value"))