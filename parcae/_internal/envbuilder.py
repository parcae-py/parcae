from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import AnyStr
    from typing_extensions import Self
    from types import SimpleNamespace

from pathlib import Path
from venv import EnvBuilder as BaseEnvBuilder

from parcae._internal.errors import PackageNotFound
from parcae._vendor import httpx


class EnvBuilder(BaseEnvBuilder):
    def install_from_pypi(self, context: SimpleNamespace, pypi_name: str) -> None:
        response = httpx.get(f"https://pypi.org/pypi/{pypi_name}/json")

        if response.status_code == 404:
            raise PackageNotFound(f"name {pypi_name} is not available on PyPI.")

    def _install_script(
        self, *, install_dir: str, package_name: AnyStr, download_url: str
    ) -> None:
        assert download_url.startswith("http://") or download_url.startswith("https://")
