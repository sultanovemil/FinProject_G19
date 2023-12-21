import os

from streamlit.testing.v1 import AppTest


def test_input():
    at = AppTest.from_file('visualization.py', default_timeout=120)
    at.secrets['API_TOKEN'] = os.getenv('API_TOKEN')
    at.run()
    at.button[0].click().run()
    at.text_area[0].input('test').run()
    at.button[1].click().run()
    assert len(at.exception) == 0
