#!/usr/bin/env python3
"""
Module for timed reading of input.
Available readers:
TimeoutInput => A thread based timeout wrapper around input function.
"""

from TimedInput.timeout_input import TimeoutInput
__all__ = ["TimeoutInput"]
