"""
photocrawl
~~~~~~~~~~

photocrawl provides a simple script to run analysis and get insight on one's use of equipment and
settings in their practice of photography.

:copyright: (c) 2019 by Felix Soubelet.
:license: MIT, see LICENSE for more details.
"""

# Set default logging handler to avoid "No handler found" warnings.

__url__ = "https://github.com/fsoubelet/PhotoCrawl"
__version__ = "0.3.2"


from .photocrawl import PhotoCrawler  # noqa: TID252

__all__ = ["PhotoCrawler"]
