import matplotlib.pyplot as plt
import numpy as np
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import BBCodeFormatter
from pygments.styles import monokai


def create_code_snapshot(code, filename, title="Code Snapshot"):
    """Create a visually appealing code snapshot using matplotlib
    The goal of course is to utilize this syntax-highlighted code, parameterically.

    Parameters
    ----------
    code : str
        The raw Python source code to emphasize and show.
    filename ; str
        The basic filename (without the extension .png) in which the resulting ssnapshot resides and is thus "saved" in the directory `images/`.
    title : str, optional
        A title, for the code snap-shot (NOT displayed in this particular verison of course, but availbale..available for future consumption), the default value is "Code Snapshot". That's the first value of course we can set more. When we onboard more team members or perhaps transition to CollabNext then we will know.

    Notes
    _____
    1. First, uses a BBBCodeFormatter with the 'monokai" style for emphasis.
    2. The code lines, are placed secondarily in a Matplotlib figure with a monokai-colored back-ground, such that the visually match the common Integrated Development Environment type of color schemas.
    3. Saves these to `images/{filename}.png` with the transparent edges removed.
    """
    # Format the code with syntax highlighting
    formatter = BBCodeFormatter(style='monokai')
    highlighted = highlight(code, PythonLexer(), formatter)

    # Split into lines
    lines = highlighted.strip().split('\n')

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, len(lines) * 0.3))

    # Set background color
    ax.set_facecolor('#272822')  # Monokai background color
    fig.patch.set_facecolor('#272822')

    # Add code lines
    for i, line in enumerate(lines):
        # Remove BBCode formatting and add text
        clean_line = line.replace(
            '[color=#', '').replace(']', '').replace('[/color]', '')
        ax.text(0.05, 1 - (i+1)/(len(lines)+1), clean_line,
                color='white',
                fontfamily='monospace',
                fontsize=10,
                transform=ax.transAxes)

    # Remove axes
    ax.axis('off')

    # Save the figure
    plt.savefig(f'images/{filename}.png',
                bbox_inches='tight',
                dpi=300,
                facecolor='#272822',
                edgecolor='none')
    plt.close()
