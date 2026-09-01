import html

FILENAME = "nitesh_typing.svg"

TEXTS = [
    "Hi there! I'm Nitesh Kumar 👋",
    "I'm a Developer 👨‍💻",
]

FONT_SIZE = 30
FONT_FAMILY = "Arial, sans-serif"

TYPE_SPEED = 0.08
DELETE_SPEED = 0.05
PAUSE = 1.5

# Fixed canvas
WIDTH = 700
HEIGHT = 70


def escape(text):
    return html.escape(text)


# Create typing/deleting frames
frames = []
time = 0

current = ""

for text_index, target in enumerate(TEXTS):

    # Type text
    for char in target:
        current += char

        frames.append({
            "text": current,
            "time": time
        })

        time += TYPE_SPEED

    # Hold the complete sentence
    time += PAUSE

    # Delete text
    for _ in target:
        current = current[:-1]

        frames.append({
            "text": current,
            "time": time
        })

        time += DELETE_SPEED

    # Small pause before next sentence
    time += 0.5


# Total animation duration
total_duration = time


svg = f'''<?xml version="1.0" encoding="UTF-8"?>

<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
>

<style>

.text {{
    font-family: {FONT_FAMILY};
    font-size: {FONT_SIZE}px;
    font-weight: 600;
    fill: #1F2328;
}}

@media (prefers-color-scheme: dark) {{
    .text {{
        fill: #D1D7E0;
    }}
}}

</style>

<rect
    width="100%"
    height="100%"
    fill="transparent"
/>

<text
    class="text"
    x="{WIDTH / 2}"
    y="45"
    text-anchor="middle"
>

'''


# Create animation using opacity
for i, frame in enumerate(frames):

    start = frame["time"]

    if i + 1 < len(frames):
        end = frames[i + 1]["time"]
    else:
        end = total_duration

    duration = max(end - start, 0.01)

    svg += f'''
<tspan
    x="{WIDTH / 2}"
    opacity="0"
>
    {escape(frame["text"])}

    <set
        attributeName="opacity"
        to="1"
        begin="{start:.3f}s"
        dur="{duration:.3f}s"
    />

</tspan>
'''


svg += f'''

<animate
    attributeName="opacity"
    values="1;1"
    dur="{total_duration:.3f}s"
    repeatCount="indefinite"
/>

</text>

</svg>
'''


with open(FILENAME, "w", encoding="utf-8") as file:
    file.write(svg)

print(f"Generated {FILENAME}")
