# Fantastical CLI

An (unofficial) command-line interface (CLI) tool to quickly add events to your [Fantastical](https://flexibits.com/fantastical) calendar using natural language.

## Purpose

This script allows you to add events to Fantastical directly from your terminal. You can specify the event details using natural language, add notes, target a specific calendar, and choose whether to add the event immediately or review it in the Fantastical app first.

## Requirements

- Python 3
- Fantastical 3 (or a version that supports the `x-fantastical3://` URL scheme) installed on macOS.

## Usage

To use the script, you can run it directly if it's executable, or by invoking it with `python3`.

```bash
./fantastical-cli.py [options] "event sentence"
# or
python3 fantastical-cli.py [options] "event sentence"
```

Make sure the script is executable:
```bash
chmod +x fantastical-cli.py
```

### Arguments

-   **`sentence`** (required):
    -   The natural language description of the event.
    -   Example: `"Lunch with Sarah tomorrow at 1pm at The Cafe"`
    -   If your sentence contains spaces, it's best to enclose it in quotes, or provide it as the last set of arguments.

### Options

-   **`-n, --notes "YOUR NOTES"`**:
    -   Adds additional notes to the event.
    -   Example: `--notes "Discuss project updates"`

-   **`-c, --calendar "CALENDAR NAME"`**:
    -   Specifies the calendar to add the event to.
    -   Example: `--calendar "Work"`

-   **`-g, --gui`**:
    -   If this flag is present, Fantastical will open its UI to let you review and confirm the event details before adding it.
    -   By default (if `-g` is *not* used), the event is added immediately to Fantastical without showing the confirmation UI.

## Examples

1.  **Add an event immediately:**
    ```bash
    ./fantastical-cli.py "Team meeting next Monday at 10am"
    ```

2.  **Add an event with notes:**
    ```bash
    ./fantastical-cli.py "Doctor appointment on Friday 3pm" -n "Annual check-up"
    ```

3.  **Add an event to a specific calendar and review in GUI:**
    ```bash
    ./fantastical-cli.py "Dinner with family this Saturday 7pm" -c "Personal" -g
    ```

4.  **Add an event with a multi-word sentence without quotes (less common):**
    ```bash
    ./fantastical-cli.py Coffee with Alex at 9am next Tuesday
    ```
    (Note: It's generally safer to quote sentences with spaces.)

5. **Add a TODO item with "High" priority:**
    ```bash
    ./fantastical-cli.py 'TODO: Check for project feedback today by 5pm!!!'
    ```
    (Note: Fantastical TODOs just require prefixing the sentence with "TODO" or "todo", and the
    priority is set by adding exclamation marks '!'=low, '!!'=medium, '!!!'=high.)

## How it Works

The script constructs a Fantastical URL scheme (`x-fantastical3://parse?...`) with the provided event details and uses the `open` command on macOS to send it to the Fantastical application.

## MIT License 
<https://opensource.org/license/mit>

Copyright 2025 Jason L. Causey

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
