import os

from streamlit.testing.v1 import AppTest

text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."""

def test_input():
    at = AppTest.from_file('app.py', default_timeout=120)
    at.run()
    at.text_area[0].input(text).run()
    at.button[0].click().run()
    assert len(at.text_area) == 2
    assert len(at.exception) == 0
