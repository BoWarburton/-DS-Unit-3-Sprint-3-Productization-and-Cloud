#!/usr/bin/env python
"""
Entry point for aq_dashboard web app
"""
from .app import create_app

APP = create_app()
