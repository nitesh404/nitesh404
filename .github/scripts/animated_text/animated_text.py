FILENAME = "nitesh_typing.svg"

TEXTS = [
    "Hi there! I'm Nitesh Kumar 👋",
    "I'm a Developer 👨‍💻",
]


def build_svg_animation(texts):

    width = 500
    height = 40
    font_size = 20

    lines = []
    visible = ""
    time = 0

    for phrase in texts:

        # Type the phrase
        for char in phrase:

            visible += char

            lines.append(
                f"""
                <text
                    x="10"
                    y="{font_size}"
                    text-anchor="start"
                    opacity="0"
                >
                    <set
                        attributeName="opacity"
                        to="1"
                        begin="{time:.3f}s"
                        dur="0.15s"
                        fill="remove"
                    />
                    {visible}
                </text>
                """
            )

            time += 0.15

        # Keep the phrase visible
        time += 2.0

        # Backspace the ENTIRE phrase
        for _ in phrase:

            visible = visible[:-1]

            lines.append(
                f"""
                <text
                    x="10"
                    y="{font_size}"
                    text-anchor="start"
                    opacity="0"
                >
                    <set
                        attributeName="opacity"
                        to="1"
                        begin="{time:.3f}s"
                        dur="0.08s"
                        fill="remove"
                    />
                    {visible}
                </text>
                """
            )

            time += 0.08

        # Small pause before next phrase
        time += 0.5


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


def save_svg(filename, content):

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved SVG to {filename}")


if __name__ == "__main__":

    svg = build_svg_animation(TEXTS)

    save_svg(FILENAME, svg)
