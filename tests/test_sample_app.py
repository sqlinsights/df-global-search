from streamlit.testing.v1 import AppTest


def test_sample_app():
    at = AppTest.from_file("../sample_app.py")
    at.run()
    assert not at.exception
