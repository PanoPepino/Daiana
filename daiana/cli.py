"""Main CLI entry point for Daiana"""

import click
from daiana.compile import compile_command
# from daiana.erase import erase_command


@click.group()
@click.version_option()
def cli():  # This is what appears when you call the package --help
    """
    ===== Daiana =====

    A tool that aims to be LaTeX CV/Cover Letter Automation for Job Hunting.

    It will help you manage and compile LaTeX documents for your job applications in a straight forward way just using your terminal and some inputs.
    """
    pass


@cli.command(name="compile")  # this is what appears when you call daiana compile --help
@click.option('--input-dir', '-i', type=click.Path(exists=True), help='Input directory')
@click.option('--output-dir', '-o', type=click.Path(), help='Output directory')
@click.option('--clean', is_flag=True, help='Clean auxiliary files')
def compile_cmd(input_dir, output_dir, clean):
    """Compile CV + CL interactively."""
    compile_command(input_dir, output_dir, clean)


if __name__ == '__main__':
   cli()
