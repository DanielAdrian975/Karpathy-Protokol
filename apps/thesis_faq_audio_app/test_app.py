import tempfile
import unittest
from pathlib import Path

from apps.thesis_faq_audio_app.app import generate_audio, sanitize_filename, split_text


class TextToAudioAppTests(unittest.TestCase):
    def test_sanitize_filename(self):
        self.assertEqual(sanitize_filename("Bab 1: Pendahuluan!!!"), "bab-1-pendahuluan")
        self.assertEqual(sanitize_filename(""), "audio")

    def test_split_text_paragraphs(self):
        chunks = split_text("Paragraf satu.\n\nParagraf dua.")
        self.assertEqual(chunks, ["Paragraf satu.", "Paragraf dua."])

    def test_split_text_hard_splits_long_text(self):
        chunks = split_text("a" * 25, max_chars=10)
        self.assertEqual([len(c) for c in chunks], [10, 10, 5])

    def test_dry_run_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = generate_audio(
                text="Halo Gysje. Ini dry run.",
                title="Tes Manifest",
                content_type="thesis",
                output_dir=Path(tmp),
                dry_run=True,
            )
            manifest_path = Path(str(manifest["manifest_path"]))
            self.assertTrue(manifest_path.exists())
            self.assertEqual(manifest["chunk_count"], 1)
            self.assertTrue(Path(tmp).exists())


if __name__ == "__main__":
    unittest.main()
