# Generated by CodiumAI
import argparse
import pytest
from unittest.mock import patch
from template_rocker.new_rocker_extension import NewRockerExtension


class TestPixiExtension:

    # Instantiating PixiExtension and verifying the name attribute is set correctly
    def test_name_attribute_initialization(self):
        extension = NewRockerExtension()
        assert extension.name == "new_rocker_extension"

    def test_register_arguments(self):
        parser = argparse.ArgumentParser()
        NewRockerExtension.register_arguments(parser)
        args = parser.parse_args([])
        assert "new_rocker_extension" in vars(args)

    # Handling missing template files in get_snippet method
    def test_get_snippet_missing_template(self):

        extension = NewRockerExtension()
        with patch("pkgutil.get_data", return_value=None):
            with pytest.raises(AttributeError):
                extension.get_snippet({})

    # Retrieving the default snippet using get_snippet method
    def test_retrieve_default_snippet(self):

        extension = NewRockerExtension()
        snippet = extension.get_snippet(None)

        assert snippet is not None

    # Retrieving the user-specific snippet using get_user_snippet method
    def test_retrieve_user_specific_snippet(self):

        extension = NewRockerExtension()
        snippet = extension.get_user_snippet(None)

        assert snippet is not None
