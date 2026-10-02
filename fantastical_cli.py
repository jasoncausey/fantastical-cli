#!/usr/bin/env python3
"""
Fantastical CLI - Add events to Fantastical from the command line using natural language.
"""
# MIT License <https://opensource.org/license/mit>
#
# Copyright 2025 Jason L. Causey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import subprocess
import urllib.parse
import sys
from typing import Optional, Dict, Any

# Availability ("show as") values accepted by Fantastical's URL scheme
AVAILABILITY_CHOICES = ["free", "busy", "tentative", "outofoffice", "workingelsewhere"]


def normalize_availability(value: str) -> str:
    """Lowercase and drop spaces, hyphens, and underscores (e.g. 'Out-of-Office' -> 'outofoffice')."""
    return "".join(ch for ch in value.lower() if ch not in " -_")


def add_event(
    sentence: str,
    notes: Optional[str] = None,
    calendar: Optional[str] = None,
    add_immediately: bool = False,
    availability: Optional[str] = None,
) -> None:
    """
    Add an event to Fantastical using the URL scheme approach.

    Args:
        sentence: Natural language description of the event
        notes: Optional notes to add to the event
        calendar: Optional calendar name to add the event to
        add_immediately: Whether to add the event immediately without showing UI
        availability: Optional availability (one of AVAILABILITY_CHOICES)
    """
    # Fantastical 3 URL scheme base
    FANTASTICAL_BASE_URL = "x-fantastical3://parse?"

    # Build the URL parameters
    params: Dict[str, Any] = {"s": sentence}

    if notes:
        params["n"] = notes

    if calendar:
        params["calendarName"] = calendar

    if availability:
        params["availability"] = availability

    if add_immediately:
        params["add"] = "1"

    # Encode parameters and build the URL
    # Use quote_via=urllib.parse.quote to encode spaces as %20 instead of +
    encoded_params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    url = f"{FANTASTICAL_BASE_URL}{encoded_params}"

    # Open the URL with the default handler (which should be Fantastical)
    subprocess.run(["open", url])
    print(f"Event sent to Fantastical: {sentence}")


def main() -> None:
    """Parse command line arguments and add event to Fantastical."""
    parser = argparse.ArgumentParser(
        description="Add events to Fantastical using natural language input."
    )

    parser.add_argument(
        "sentence",
        nargs="*",
        help="Natural language description of the event (e.g., 'Meeting with John tomorrow at 3pm')",
    )

    parser.add_argument(
        "-n",
        "--notes",
        help="Additional notes for the event",
    )

    parser.add_argument(
        "-c",
        "--calendar",
        help="Calendar to add the event to",
    )

    parser.add_argument(
        "-a",
        "--availability",
        type=normalize_availability,
        choices=AVAILABILITY_CHOICES,
        help="Show the event as free, busy, tentative, outofoffice, or workingelsewhere "
        "(case, spaces, hyphens, and underscores are ignored)",
    )

    parser.add_argument(
        "-g",
        "--gui",  # New flag for showing GUI
        action="store_true",
        help="Show the Fantastical UI to confirm before adding (default is immediate add)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Check if sentence was provided
    if not args.sentence:
        parser.print_help()
        sys.exit(1)

    # Join the sentence parts
    sentence = " ".join(args.sentence)

    # Add the event
    # Determine if the event should be added immediately
    # If --gui is specified, add_immediately is False. Otherwise, it's True.
    should_add_immediately = not args.gui

    add_event(sentence, args.notes, args.calendar, should_add_immediately, args.availability)


if __name__ == "__main__":
    main()
