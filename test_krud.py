#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic tests for Krud module dependencies."""

def test_cryptography_available():
    """Test that cryptography is installed."""
    from cryptography.fernet import Fernet
    assert Fernet is not None


def test_distro_available():
    """Test that distro is installed."""
    import distro
    version = distro.version()
    assert version is not None


def test_pathlib_available():
    """Test that pathlib is available."""
    from pathlib import Path
    assert Path is not None


def test_basic_imports():
    """Test basic Python imports used by Krud."""
    import threading
    import subprocess
    import os
    import sys
    import time
    import datetime
    assert all([threading, subprocess, os, sys, time, datetime])
