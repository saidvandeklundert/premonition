from premonition.device import JuniperDevice
import typer
from typing_extensions import Annotated
from pathlib import Path

from rich import print

app = typer.Typer()


@app.command()
def juniper(
    location: Annotated[
        str,
        typer.Option(help="The file to convert or the folder with files to convert"),
    ],
    information: Annotated[
        str,
        typer.Option(
            help="The information to display: 'set' for set config, 'model' for the model, or 'both' for both."
        ),
    ] = "both",
):
    path = Path(location)
    if path.is_file():
        print(f"file: {location}")
        with open(location, "rt") as f:
            configuration = f.read()
        dev = JuniperDevice(configuration=configuration, hostname=path.stem)
        dev.build_models()
        if information == "set" or information == "both":
            print(dev.configuration_set_style)
        if information == "model" or information == "both":
            print(dev.show_model())

    elif path.is_dir():
        print(f"directory: {location}, not implemented yet.")
    else:
        RuntimeError(f"The location {location} should be either a file or a folder")


if __name__ == "__main__":
    app()
