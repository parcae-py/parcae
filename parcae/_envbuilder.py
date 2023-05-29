from __future__ import annotations
from typing import TYPE_CHECKING, AnyStr


if TYPE_CHECKING:
    from typing_extensions import Self
    from types import SimpleNamespace

from pathlib import Path


from parcae._vendor import httpx
from venv import EnvBuilder as _BaseEnvBuilder

from parcae.errors import InvalidPypiName



class EnvBuilder(_BaseEnvBuilder):
    def install_from_pypi(self, context: SimpleNamespace, pypi_name: str) -> None:
        x = httpx.get(f"https://pypi.org/pypi/{pypi_name}/json")
        if x.status_code == 404:
            raise InvalidPyPIName(f"name {pypi_name} is not available on PyPI.")
    
    def _install_script(self, *, install_dir: str, package_name: AnyStr, download_url: str) -> None:
        assert (download_url.startswith("http://") or download_url.startswith("https://"))

            
        
        
            

