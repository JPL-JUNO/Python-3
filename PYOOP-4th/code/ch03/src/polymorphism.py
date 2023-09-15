"""
@Title: 多态 Polymorphism
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-15 19:40:22
@Description: It is also sometimes called the Liskov Substitution Principle, honoring
Barbara Liskov's contributions to object-oriented programming.
"""

from pathlib import Path


class AudioFile:
    ext: str

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath


class MP3File(AudioFile):
    ext = ".mp3"

    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")


class WavFile(AudioFile):
    ext = ".wav"

    def play(self) -> None:
        print(f"playing {self.filepath} as wav")


class OggFile(AudioFile):
    ext = ".ogg"

    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")


class FlacFile:
    """
    这个类不是 AudioFile 的子类，
    但是它是可以在 Python 中使用完全相同的接口与之交互

    Python 的鸭子类型使得其多态不是那么酷
    """

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath

    def play(self) -> None:
        print(f"playing {self.filepath} as flac")


if __name__ == "__main__":
    p_1 = MP3File(Path("Heart of the Sunrise.mp3"))
    p_1.play()

    p_2 = WavFile(Path("Roundabout.wav"))
    p_2.play()

    p_3 = OggFile(Path("Heart of the Sunrise.ogg"))
    p_3.play()
    try:
        p_4 = MP3File(Path("The Fish.mov"))
    except ValueError as e:
        print(e)
