import html

TEXT = "Hi there! I'm Nitesh Kumar 👋|<<< Kumar 👋|<<<Nitesh Kumar 👋|<<<Hi there! I'm Nitesh Kumar 👋"
FILENAME = "nitesh_typing.svg"

FONT_SIZE = 32
CHAR_WIDTH = 19
TYPING_SPEED = 0.15
PAUSE = 1.5

def escape(text):
    return html.escape(text)

frames = []
current = ""

time = 0

for char in TEXT:
    if char == "|":
        time += PAUSE
        continue

    if char == "<":
        if current:
            current = current[:-1]
            time += TYPING_SPEED
        continue

    current += char
    frames.append((current, time))
    time += TYPING_SPEED

width = max(len(text) for text, _ in frames) * CHAR_WIDTH + 40

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="55"
viewBox="0 0 {width} 55">

<style>
text {{
    font-family: monospace;
    font-size: {FONT_SIZE}px;
    font-weight: 600;
    fill: #1F2328;
}}

@media (prefers-color-scheme: dark) {{
    text {{
        fill: #D1D7E0;
    }}
}}
</style>

<text x="10" y="38">{escape(frames[0][0])}</text>

</svg>
'''

with open(FILENAME, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Generated {FILENAME}")
