"""The legacy ovos-audio shim ignores play() when no track is loaded."""
import unittest
from unittest.mock import patch

from ovos_utils.fakebus import FakeBus

from ovos_plugin_mpv import load_service


class TestLegacyPlayNoTrack(unittest.TestCase):
    @patch("ovos_plugin_mpv.MPV")
    def test_play_without_track_is_noop(self, mpv_cls):
        config = {"backends": {"mpv": {"type": "ovos_mpv", "active": True}}}
        service = load_service(config, FakeBus())[0]
        service.play()
        mpv_cls.return_value.play.assert_not_called()
        self.assertIsNone(service.mpv)


if __name__ == "__main__":
    unittest.main()
