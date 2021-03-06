import importlib
import os
import yaml

from zaza import model

BUNDLE_DIR = "./tests/bundles/"
DEFAULT_TEST_CONFIG = "./tests/tests.yaml"


def get_charm_config(yaml_file=None):
    """Read the yaml test config file and return the resulting config

    :param yaml_file: File to be read
    :type yaml_file: str
    :returns: Config dictionary
    :rtype: dict
    """
    if not yaml_file:
        yaml_file = DEFAULT_TEST_CONFIG
    with open(yaml_file, 'r') as stream:
        return yaml.load(stream)


def get_class(class_str):
    """Get the class represented by the given string

       For example, get_class('zaza.charms_tests.svc.TestSVCClass1')
       returns zaza.charms_tests.svc.TestSVCClass1

    :param class_str: Class to be returned
    :type class_str: str
    :returns: Test class
    :rtype: class
    """
    module_name = '.'.join(class_str.split('.')[:-1])
    class_name = class_str.split('.')[-1]
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def set_juju_model(model_name):
    """Point environment at the given model

    :param model_name: Model to point environment at
    :type model_name: str
    """
    os.environ["JUJU_MODEL"] = model_name


def get_juju_model():
    """Retrieve current model

    First check the environment for JUJU_MODEL. If this is not set, get the
    current active model.

    :returns: In focus model name
    :rtype: str
    """

    try:
        # Check the environment
        return os.environ["JUJU_MODEL"]
    except KeyError:
        # If unset connect get the current active model
        return model.get_current_model()
