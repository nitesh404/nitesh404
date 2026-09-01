FILENAME = "nitesh_typing.svg"

PHRASES = [
    "Hi there! I'm Nitesh Kumar 👋",
    "I'm a Developer 👨‍💻",
]

WIDTH = 500
HEIGHT = 45
FONT_SIZE = 20

TYPE_SPEED = 0.15
DELETE_SPEED = 0.10
PAUSE = 1.5


def build_svg_animation(phrases):

    frames = []

    current = ""
    time = 0.0

    # Create typing + deleting frames
    for phrase in phrases:

        # -------------------------
        # TYPE
        # -------------------------
        for char in phrase:

            current += char

            frames.append({
                "text": current,
                "start": time,
            })

            time += TYPE_SPEED

        # -------------------------
        # PAUSE
        # -------------------------
        time += PAUSE

        # -------------------------
        # DELETE
        # -------------------------
        for _ in phrase:

            current = current[:-1]

            frames.append({
                "text": current,
                "start": time,
            })

            time += DELETE_SPEED

        # Small pause before next phrase
        time += 0.5

    total_time = time

    # -------------------------
    # SVG
    # -------------------------

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>

<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
>

<style>

    .typing {{
        font-family: Arial, sans-serif;
        font-size: {FONT_SIZE}px;
        font-weight: bold;
        fill: #1F2328;
    }}

    @media (prefers-color-scheme: dark) {{
        .typing {{
            fill: #D1D7E0;
        }}
    }}

</style>

<clipPath id="clip">
    <rect
        x="0"
        y="0"
        width="{WIDTH}"
        height="{HEIGHT}"
    />
</clipPath>

<g clip-path="url(#clip)">
'''

    # -------------------------
    # Create frames
    # -------------------------

    for i, frame in enumerate(frames):

        start = frame["start"]

        if i + 1 < len(frames):
            end = frames[i + 1]["start"]
        else:
            end = total_time

        duration = end - start

        text = frame["text"]

        # Every frame explicitly appears
        # and then disappears.
        svg += f'''
    <text
        class="typing"
        x="5"
        y="30"
        opacity="0"
    >
        {text}

        <set
            attributeName="opacity"
            to="1"
            begin="{start:.3f}s"
        />

        <set
            attributeName="opacity"
            to="0"
            begin="{end:.3f}s"
        />

    </text>
'''

    svg += f'''
</g>

<!-- Restart the entire animation -->
<rect
    x="0"
    y="0"
    width="1"
    height="1"
    opacity="0"
>
    <animate
        attributeName="opacity"
        values="0;0"
        dur="{total_time:.3f}s"
        repeatCount="indefinite"
    />
</rect>

</svg>
'''

    return svg


def save_svg(filename, content):

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Saved SVG to {filename}")


if __name__ == "__main__":

    svg = build_svg_animation(PHRASES)

    save_svg(FILENAME, svg)
