import html

TEXT = "Hi there! I'm Nitesh 👋|<<<<<<<< a Developer 👨‍💻"
FILENAME = "nitesh_typing.svg"


def build_svg_animation(text: str) -> str:
    width = 500
    height = 35
    font_size = 20

    visible = ""
    frames = []
    current_time = 0.0

    # Build every typing/backspace state
    for idx, char in enumerate(text):
        if char == "|":
            continue

        if char == "<":
            visible = visible[:-1]
        else:
            visible += char

        # Pause after "|"
        pause = (
            idx + 1 < len(text)
            and text[idx + 1] == "|"
        )

        duration = 1.0 if pause else 0.15

        frames.append(
            (current_time, duration, visible)
        )

        current_time += duration

    # Time to wait before starting again
    restart_delay = 2.0
    cycle_duration = current_time + restart_delay

    # Create one animated text element.
    # The text content itself changes using <animate>.
    values = []
    key_times = []

    for start, duration, value in frames:
        values.append(html.escape(value))
        key_times.append(start / cycle_duration)

    # Add the final frame
    values.append(html.escape(visible))
    key_times.append(current_time / cycle_duration)

    values_str = ";".join(values)
    key_times_str = ";".join(
        f"{x:.5f}" for x in key_times
    )

    # Position of waving hand
    emoji_x = len(visible) * font_size * 0.48
    pivot_x = emoji_x + 10
    pivot_y = font_size

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>

<svg
    width="{width}"
    height="{height}"
    viewBox="0 0 {width} {height}"
    xmlns="http://www.w3.org/2000/svg">

    <style>
        text {{
            font-family: Arial, sans-serif;
            font-weight: bold;
            font-size: {font_size}px;
            fill: #1F2328;
        }}

        @media (prefers-color-scheme: dark) {{
            text {{
                fill: #D1D7E0;
            }}
        }}
    </style>

    <!--
        Complete typing animation.
        The entire sequence repeats forever.
    -->

    <text
        x="0"
        y="{font_size}"
        opacity="1">

        <animate
            attributeName="textContent"
            values="{values_str}"
            keyTimes="{key_times_str}"
            dur="{cycle_duration:.3f}s"
            repeatCount="indefinite"
        />

    </text>

    <!-- Waving hand -->
    <text
        x="{emoji_x}"
        y="{font_size}"
        opacity="0">

        👋

        <set
            attributeName="opacity"
            to="1"
            begin="{current_time:.3f}s"
        />

        <animateTransform
            attributeName="transform"
            type="rotate"
            values="
                -20 {pivot_x} {pivot_y};
                 20 {pivot_x} {pivot_y};
                -20 {pivot_x} {pivot_y}
            "
            dur="0.5s"
            repeatCount="indefinite"
        />

    </text>

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
```
