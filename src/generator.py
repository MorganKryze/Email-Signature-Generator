from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader


def read_options(yml_path: str) -> dict:
    """Read the options file and returns a dictionary with the options."""
    with Path.open(yml_path) as file:
        return yaml.safe_load(file)


def generate_html(
    options: dict,
    path_with_photo: str,
    path_without_photo: str,
    path_output_file: str,
) -> None:
    """Generate the HTML file from the options."""
    env = Environment(
        loader=FileSystemLoader("src"),
        autoescape=True,
    )
    if "photo" in options:
        template = env.get_template(path_with_photo)
    else:
        template = env.get_template(path_without_photo)

    output = template.render(options)

    with Path.open(path_output_file, "w") as file:
        file.write(output)


if __name__ == "__main__":
    # Paths
    options_source = "src/options.yml"
    html_template_logo = "signature-logo.html"
    html_template_photo = "signature-photo.html"
    output_file = "output.html"

    # Generate the HTML file
    options = read_options(options_source)
    generate_html(options, html_template_photo, html_template_logo, output_file)

    # Print acknowledgment
    print("HTML file generated successfully!")
