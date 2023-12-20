from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

OPTIONS_FILENAME = "src/options.yml"
HTML_TEMPLATE = "signature-template.html"
OUTPUT_FILENAME = "output.html"

def read_options(yml_path: str) -> dict:
    """Read the options file and returns a dictionary with the options.

    Args:
    ----
        yml_path (str): Path to the options file.

    Returns:
    -------
        dict: Dictionary with the options.
    """
    with Path.open(yml_path) as file:
        return yaml.safe_load(file)


def generate_html(
    options: dict,
) -> None:
    """Generate the HTML file with the options.

    Args:
    ----
        options (dict): Dictionary with the options.

    Returns:
    -------
        None
    """
    env = Environment(
        loader=FileSystemLoader("src"),
        autoescape=False,
    )
    template = env.get_template(HTML_TEMPLATE)

    social_media_html = ""
    for social_media, url in options["social_media"].items():
        if url != "None":
            social_media_html += (
                f'\n\t\t\t\t<a href="{url}"><img'
                f' src="https://raw.githubusercontent.com/MorganKryze/Signature-Generator/main/src/assets/icons/{social_media}.svg"></a>'
            )
    options["social_media_html"] = social_media_html

    output = template.render(**options)
    with Path.open(OUTPUT_FILENAME, "w") as file:
        file.write(output)


if __name__ == "__main__":
    # Generate the HTML file
    options = read_options(OPTIONS_FILENAME)
    generate_html(options)

    # Print acknowledgment
    print("HTML file generated successfully!")
