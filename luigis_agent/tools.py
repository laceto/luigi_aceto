from datetime import datetime, timezone


def get_current_time() -> dict:
    """Return the current UTC time.

    Returns:
        dict with status and an ISO-8601 UTC timestamp.
    """
    return {"status": "success", "utc_time": datetime.now(timezone.utc).isoformat()}
