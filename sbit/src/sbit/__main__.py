"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Sbit."""


if __name__ == "__main__":
    main(prog_name="sbit")  # pragma: no cover
