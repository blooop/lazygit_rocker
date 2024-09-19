import pkgutil
from rocker.extensions import RockerExtension


class NewRockerExtension(RockerExtension):
    @staticmethod
    def get_name():
        return "new_rocker_extension"

    def __init__(self):
        self.name = NewRockerExtension.get_name()

    def get_snippet(self, cliargs):
        return pkgutil.get_data("lazygit_rocker", "templates/curl_snippet.Dockerfile").decode(
            "utf-8"
        )

    def get_user_snippet(self, cliargs):
        snippet = pkgutil.get_data(
            "lazygit_rocker", "templates/{}_snippet.Dockerfile".format(self.name)
        ).decode("utf-8")
        return snippet

    @staticmethod
    def register_arguments(parser, defaults=None):
        if defaults is None:
            defaults = {}
        parser.add_argument(
            f"--{NewRockerExtension.get_name()}",
            action="store_true",
            default=defaults.get("pixi"),
            help="add pixi dependency manager to your environment",
        )
