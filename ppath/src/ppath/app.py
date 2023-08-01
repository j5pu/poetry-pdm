"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"ppath v{version('ppath')}")  # type: ignore[no-untyped-call]
