import pytest

import main.artificial_pancreas as ap

@pytest.fixture 
def system():
    controller = ap.ArtificialPancreasSystem(100, 1.0, 100, 10)
    return controller


