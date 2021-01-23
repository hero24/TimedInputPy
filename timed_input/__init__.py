#!/usr/bin/env python3
"""
Module for timed reading of input.
Available readers:
TimedInput => A thread-based timeout wrapper around input function.
"""

from .timed_input import TimedInput
from .timed_input import timed_input
__all__ = ['TimedInput', 'timed_input']
