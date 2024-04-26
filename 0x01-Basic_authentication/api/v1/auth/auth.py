#!/usr/bin/env python3

"""API authentication"""

from flask import request


class Auth():
    """A class to manage API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns A False - path"""
