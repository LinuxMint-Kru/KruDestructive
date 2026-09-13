#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic tests for Krud module."""

def test_import():
    """Test that Krud module can be imported."""
    try:
        import Krud
        assert True
    except ImportError:
        assert False, "Failed to import Krud module"


def test_cryptography_available():
    """Test that cryptography is installed."""
    from cryptography.fernet import Fernet
    assert Fernet is not None


def test_distro_available():
    """Test that distro is installed."""
    import distro
    assert distro.version() is not None
