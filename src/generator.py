from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader


def read_options(yml_path: str = "src/options.yml") -> dict:
    """Read the options file and returns a dictionary with the options."""
    with Path.open(yml_path) as file:
        return yaml.safe_load(file)


def generate_html(options: dict) -> None:
    """Generate the HTML file from the options."""
    env = Environment(
        loader=FileSystemLoader("src"),
        autoescape=True,
    )
    template = env.get_template("signature-logo.html")

    output = template.render(options)

    with Path.open("output.html", "w") as file:
        file.write(output)


if __name__ == "__main__":
    options = read_options()
    generate_html(options)
