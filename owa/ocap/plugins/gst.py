"""
Plugin specification for the GStreamer environment plugin.

This module is kept separate to avoid circular imports during plugin discovery.
"""

from owa.core.plugin_spec import PluginSpec


def _get_package_version() -> str:
    """Get the version of the ocap package."""
    try:
        from importlib.metadata import version
    except ImportError:  # For Python <3.8
        from importlib_metadata import version

    try:
        return version("ocap")
    except Exception:
        return "unknown"


# Plugin specification for entry points discovery
plugin_spec = PluginSpec(
    namespace="gst",
    version=_get_package_version(),
    description="High-performance GStreamer-based screen capture and recording plugin",
    author="OWA Development Team",
    components={
        "listeners": {
            "omnimodal.appsink_recorder": "owa.ocap.gst.omnimodal.appsink_recorder:AppsinkRecorder",
        },
    },
)

