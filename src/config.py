"""[General Configuration Params]"""
from os import path

# Package: python-dotenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))
