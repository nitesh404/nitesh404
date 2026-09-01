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

    # Build all typing/backspace states
    for idx, char in enumerate(text):
        if char == "|":
            continue

        if char == "<":
            visible = visible[:-1]
        else:
            visible += char

        is_pause = (
            idx + 1 < len(text)
            and text[idx + 1] == "|"
        )

        delay = 1.0 if is_pause else 0.15

        frames.append({
            "time": current_time,
            "duration": delay,
            "text": visible,
        })

        current_time += delay

    # Time to wait before restarting
    restart_pause = 2.0
    cycle = current_time + restart_pause

    lines = []

    for frame in frames:
        start = frame["time"]
        duration = frame["duration"]
        end = start + duration

        # Use one repeating opacity animation per frame.
        values = "0;1;1;0"

        key_times = (
            f"0;"
            f"{start / cycle:.6f};"
            f"{(start + 0.001) / cycle:.6f};"
            f"{end / cycle:.6f}"
        )

        lines.append(f"""
        <text
            x="0"
            y="{font_size}"
            opacity="0">

            {html.escape(frame["text"])}

            <animate
                attributeName="opacity"
                values="{values}"
                keyTimes="{key_times}"
                dur="{cycle:.3f}s"
                repeatCount="indefinite"
            />

        </text>
        """)

    # Waving emoji
    emoji_x = len(visible) * font_size * 0.48
    pivot_x = emoji_x + 10
    pivot_y = font_size

    emoji_start = current_time

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

    <!-- Typing animation -->
    {''.join(lines)}

    <!-- Waving hand -->
    <text
        x="{emoji_x}"
        y="{font_size}"
        opacity="0">

        👋

        <animate
            attributeName="opacity"
            values="0;0;1;1;0"
            keyTimes="
                0;
                {emoji_start / cycle:.6f};
                {(emoji_start + 0.001) / cycle:.6f};
                {(emoji_start + 1.5) / cycle:.6f};
                {(emoji_start + 1.501) / cycle:.6f}
            "
            dur="{cycle:.3f}s"
            repeatCount="indefinite"
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
