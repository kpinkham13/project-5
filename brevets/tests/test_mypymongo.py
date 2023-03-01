from mypymongo import brevet_insert, brevet_find
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_mongo1():
    start_time = "2023-02-22 10:00"
    dist = "200"
    checkpoints = {
              "0": ("2023-02-22 10:00"),
             "50": ("2023-02-22 10:00"),
            "150": ("2023-02-22 10:00"),
            "200": ("2023-02-22 10:00"),
            }
    
    brevet_insert(start_time, dist, checkpoints)
    a, b, c = brevet_find()
    assert a == start_time
    assert b == dist
    assert c == checkpoints, f"Checkpoints didn't match: {c} != {checkpoints}"
