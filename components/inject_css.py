# components/inject_css.py
# Place this file at: components/inject_css.py
# Usage: from components.inject_css import inject_css, inject_fonts
# Call inject_fonts() and inject_css() at the top of every page file.

import streamlit as st

def inject_fonts():
    """Injects Google Fonts — call once per page, before inject_css."""
    st.markdown(
        '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1'
        '&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" '
        'rel="stylesheet">',
        unsafe_allow_html=True
    )

def inject_css():
    """Reads assets/style.css and injects it into the Streamlit page."""
    with open("assets/style.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def nav_html(active_page: str) -> str:
    """
    Returns the nav HTML string. Pass the active page name so the
    correct link gets the 'active' class.
    active_page: one of 'home', 'calculator', 'trends', 'sources'
    """
    def cls(page):
        return 'nav-link active' if page == active_page else 'nav-link'

    return f"""
    <nav>
      <div class="nav-logo">
        <div class="nav-logo-dot"></div>
        InflaTrack
      </div>
      <div class="nav-links">
        <a class="{cls('home')}" href="/" target="_self">Home</a>
        <a class="{cls('calculator')}" href="/Calculator" target="_self">Calculator</a>
        <a class="{cls('trends')}" href="/Trends" target="_self">Trends</a>
        <a class="{cls('sources')}" href="/Sources" target="_self">Sources</a>
        <a class="nav-cta" href="/Calculator" target="_self">Calculate Mine →</a>
      </div>
    </nav>
    """

def footer_html(note: str = "Data sourced from MOSPI and RBI DBIE. Calculated rates are estimates based on user-declared spending. For educational and informational purposes only.") -> str:
    return f"""
    <footer>
      <div class="footer-logo">InflaTrack</div>
      <div class="footer-note">{note}</div>
      <div class="footer-links">
        <a class="footer-link" href="/" target="_self">Home</a>
        <a class="footer-link" href="/Calculator" target="_self">Calculator</a>
        <a class="footer-link" href="/Trends" target="_self">Trends</a>
        <a class="footer-link" href="/Sources" target="_self">Sources</a>
      </div>
    </footer>
    """
