import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import textwrap


def create_markdown_image(markdown_text, filename, figsize=(12, 16)):
    """Convert markdown text to a visually appealing image FILE.
    Parameters
    ----------
    markdown_text : str
        Here you will find..the markdown content to be rendered into a figure.
    filename : str
        This is the path of the file (including the name of the image) where we save the final screen-shot.
    figsize : tuple of (float, float), optional
        This is the size of the figure that results, in inches, measured as (12, 16).

    Notes
    _____
    1. The function "we have here" creates a figure that has "NO" axes and sets a light background.
    2. Markdown headers (#, ##, bullet points) receive distinct format.
    3. A subtle border we add for "aesthetic" purposes.
    """

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_facecolor('#f5f5f5')
    fig.patch.set_facecolor('#f5f5f5')

    # Remove axes
    ax.axis('off')

    # Process markdown text
    lines = markdown_text.split('\n')
    y_position = 0.98
    line_height = 0.03

    for line in lines:
        if line.strip() == '':
            y_position -= line_height/2
            continue

        # Handle headers
        if line.startswith('# '):
            ax.text(0.05, y_position, line[2:],
                    fontsize=16, fontweight='bold',
                    transform=ax.transAxes)
            y_position -= line_height*1.5

        elif line.startswith('## '):
            ax.text(0.05, y_position, line[3:],
                    fontsize=14, fontweight='bold',
                    color='#2c3e50',
                    transform=ax.transAxes)
            y_position -= line_height*1.2

        # Handle bullet points
        elif line.strip().startswith('- '):
            wrapped_text = textwrap.fill(line[2:], width=80)
            for wrapped_line in wrapped_text.split('\n'):
                ax.text(0.07, y_position, '•', fontsize=12,
                        transform=ax.transAxes)
                ax.text(0.09, y_position, wrapped_line,
                        fontsize=11,
                        transform=ax.transAxes)
                y_position -= line_height

        elif line.strip().startswith('* '):
            wrapped_text = textwrap.fill(line[2:], width=80)
            for wrapped_line in wrapped_text.split('\n'):
                ax.text(0.09, y_position, '◦', fontsize=10,
                        transform=ax.transAxes)
                ax.text(0.11, y_position, wrapped_line,
                        fontsize=11,
                        transform=ax.transAxes)
                y_position -= line_height

        # Handle regular text
        else:
            wrapped_text = textwrap.fill(line, width=90)
            for wrapped_line in wrapped_text.split('\n'):
                ax.text(0.05, y_position, wrapped_line,
                        fontsize=11,
                        transform=ax.transAxes)
                y_position -= line_height

    # Add a subtle border
    border = Rectangle((0.03, 0.02), 0.94, 0.96,
                       fill=False,
                       color='#bdc3c7',
                       transform=ax.transAxes,
                       linewidth=1)
    ax.add_patch(border)

    # Save the figure
    plt.savefig(filename,
                dpi=300,
                bbox_inches='tight',
                facecolor='#f5f5f5',
                edgecolor='none')
    plt.close()
