from luigis_agent.tools import get_current_time


def test_get_current_time():
    r = get_current_time()
    assert r["status"] == "success" and "T" in r["utc_time"]


def test_root_agent_loads():
    from luigis_agent.agent import root_agent

    assert root_agent.name == "luigis_agent"
