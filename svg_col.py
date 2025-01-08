import os

# Define the directory containing your SVG files
svg_directory = 'path_to_your_svg_files'

# Define the color replacements
color_replacements = {
    '#originalColor1': '#00a8ff',
    '#originalColor2': '#007acc',
    # Add more replacements as needed
}

# Iterate over all files in the directory
for filename in os.listdir(svg_directory):
    if filename.endswith('.svg'):
        filepath = os.path.join(svg_directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
        for original_color, new_color in color_replacements.items():
            content = content.replace(original_color, new_color)
        with open(filepath, 'w') as file:
            file.write(content)
