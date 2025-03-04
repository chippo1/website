# coding: utf8
import yaml
from os.path import join, dirname

config = mirrors = packages = None

for name in ["config", "mirrors", "packages"]:
    fn = join(dirname(__file__), name) + ".yaml"
    data = yaml.load(open(fn))
    globals()[name] = data
