TEXT = "Hi there! I'm Nitesh Kumar 👋|<<<Nitesh Kumar 👋|<<<I'm a Developer 👨‍💻|<<<Developer 👨‍💻|<<<I'm a Developer 👨‍💻"
FILENAME = "nitesh_typing.svg"


def build_svg_animation(text: str) -> str:
    width = 330
    height = 40
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
            visible = visible[:-1]

        # Normal typing
        else:
            visible += char

        # Last frame
        is_last_step = (idx == len(text) - 1)

        fill_type = "freeze" if is_last_step else "remove"

        # Pause after "|"
        is_pause = (
            text[idx + 1] == "|"
            if not is_last_step
            else False
        )

        delay = 1.0 if is_pause else 0.15

        lines.append(
            f"""
        <text
            x="0"
            y="{font_size}"
            text-anchor="start"
            opacity="0"
        >
            <set
                attributeName="opacity"
                to="1"
                begin="{round(time, 3)}s"
                dur="{delay}s"
                fill="{fill_type}"
            />
            {visible}
        </text>
        """
        )

        time += delay

    # Emoji position
    emoji_x = len(visible) * font_size * 0.48

    pivot_x = emoji_x + 10
    pivot_y = font_size

    svg = f"""
<svg
    width="{width}"
    height="{height}"
    xmlns="http://www.w3.org/2000/svg"
>

<style>

text {{
    font-family: Arial, sans-serif;
    font-weight: bold;
    font-size: {font_size}px;
    fill: #1F2328;
    opacity: 0;
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
    text-anchor="start"
    opacity="0"
>

    <set
        attributeName="opacity"
        to="1"
        begin="{round(time + 2 * delay, 3)}s"
        dur="0.001s"
        fill="freeze"
    />

    👋

    <animateTransform
        attributeName="transform"
        type="rotate"
        values="-20 {pivot_x} {pivot_y};
                20 {pivot_x} {pivot_y};
                -20 {pivot_x} {pivot_y}"
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
