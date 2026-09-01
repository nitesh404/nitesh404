import html

TEXT = "Hi there! I'm Nitesh Kumar 👋|<<<Nitesh Kumar 👋|I'm a Developer 👨‍💻|<<<Developer 👨‍💻|Hi there! I'm Nitesh Kumar 👋"

FILENAME = "nitesh_typing.svg"

FONT_FAMILY = "monospace"
FONT_SIZE = 30
FONT_WEIGHT = 600

TYPING_SPEED = 0.12
DELETE_SPEED = 0.08
PAUSE = 1.5


def escape(text):
    return html.escape(text)


frames = []
current = ""
time = 0

for char in TEXT:

    # "|" = pause
    if char == "|":
        time += PAUSE
        continue

    # "<" = delete previous character
    if char == "<":
        if current:
            current = current[:-1]

        time += DELETE_SPEED
        continue

    current += char

    frames.append({
        "text": current,
        "time": time
    })

    time += TYPING_SPEED


# Calculate SVG width
max_length = max(len(frame["text"]) for frame in frames)
width = max_length * 18 + 80

height = 60


# Build animated SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{width}"
    height="{height}"
    viewBox="0 0 {width} {height}"
>

<style>
text {{
    font-family: {FONT_FAMILY};
    font-size: {FONT_SIZE}px;
    font-weight: {FONT_WEIGHT};
    fill: #1F2328;
}}

@media (prefers-color-scheme: dark) {{
    text {{
        fill: #D1D7E0;
    }}
}}
</style>

<text
    x="10"
    y="40"
>
'''

# Add text frames
for i, frame in enumerate(frames):

    begin = frame["time"]

    if i + 1 < len(frames):
        end = frames[i + 1]["time"]
        duration = end - begin
    else:
        duration = PAUSE

    svg += f'''
    <tspan
        opacity="0"
    >
        {escape(frame["text"])}
        <set
            attributeName="opacity"
            to="1"
            begin="{begin}s"
            dur="{duration}s"
        />
    </tspan>
'''


svg += '''
</text>

</svg>
'''


with open(FILENAME, "w", encoding="utf-8") as file:
    file.write(svg)

print(f"Generated {FILENAME}")
