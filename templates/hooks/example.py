"""Optional inert authoring template; no registration or side effects here."""
import json
import sys


def main():
    payload = json.load(sys.stdin)
    if payload.get("format_version") != 1:
        return
    if payload.get("event") not in ("session_start", "turn_complete"):
        return
    # Add only requested bounded, replay-safe notification work here.
    # No secrets, network, background processes or output-based host control.


if __name__ == "__main__":
    main()
