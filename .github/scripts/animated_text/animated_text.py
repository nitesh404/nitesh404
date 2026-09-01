TEXT = "Hi there! I'm Nitesh Kumar|<<<Nitesh Kumar|<<<I'm a Developer|<<<I'm a Developer"

FILENAME = "nitesh_typing.svg"


def build_svg_animation(text: str) -> str:

    # IMPORTANT:
    # Keep the SVG large enough for the longest sentence.
    width = 500
    height = 45
    font_size = 20

    lines = []

    visible = ""
    time = 0

    for idx, char in enumerate(text):

        # Pause
        if char == "|":
            continue

        # Backspace
        if char == "<":
            if visible:
                visible = visible[:-1]

        # Type character
        else:
            visible += char

        # Check whether next character is "|"
        is_last = idx == len(text) - 1

        if not is_last:
            is_pause = text[idx + 1] == "|"
        else:
            is_pause = False

        # Typing speed
        delay = 0.12

        # Pause when sentence is complete
        if is_pause:
            delay = 2.0

        fill = "freeze" if is_last else "remove"

        lines.append(
            f"""
            <text
                x="10"
                y="30"
                text-anchor="start"
                opacity="0"
            >
                <set
                    attributeName="opacity"
                    to="1"
                    begin="{time:.3f}s"
                    dur="{delay:.3f}s"
                    fill="{fill}"
                />
                {visible}
            </text>
            """
        )

        time += delay


    # Create SVG
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>

<svg
    width="{width}"
    height="{height}"
    viewBox="0 0 {width} {height}"
    xmlns="http://www.w3.org/2000/svg"
>

    <style>

        text {{
            font-family: Arial, sans-serif;
            font-size: {font_size}px;
            font-weight: bold;
            fill: #1F2328;
        }}

        @media (prefers-color-scheme: dark) {{
            text {{
                fill: #D1D7E0;
            }}
        }}

    </style>

    <!-- Keep everything inside the SVG -->
    <clipPath id="box">
        <rect
            x="0"
            y="0"
            width="{width}"
            height="{height}"
        />
    </clipPath>

    <g clip-path="url(#box)">

        {''.join(lines)}

    </g>

</svg>
"""

    return svg


def save_svg(filename: str, content: str):

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved SVG to {filename}")


if __name__ == "__main__":

    svg_content = build_svg_animation(TEXT)

    save_svg(FILENAME, svg_content)
