from pathlib import Path

from backend.audio.extractor import extract_audio_to_wav
from backend.audio.transcriber import Transcriber
from backend.pipeline.sermon_pipeline import SermonPipeline
from backend.subtitles.ass_styler import convert_srt_to_styled_ass
from backend.subtitles.burner import burn_subtitles_into_video
from backend.subtitles.refitter import refit_srt
from backend.utils.ffmpeg_manager import FfmpegManager
from backend.utils.file_utils import VideoUtils
from backend.video.concatenator import concatenate_video_clips
from backend.video.cutter import cut_video_clip
from backend.video.downloader import download_video
from backend.video.face_tracker import (
    JITTER_THRESHOLD,
    OUT_H,
    OUT_W,
    SMOOTH,
    create_face_tracked_vertical_video,
)


class VideoProcessor:
    """Backward-compatible facade over refactored video/audio functions."""

    def __init__(self, ffmpeg_manager: FfmpegManager):
        self.ffmpeg = ffmpeg_manager

    def cut_video_clip(self, source_mp4: Path, start_time: str, end_time: str, out_file: Path) -> None:
        cut_video_clip(self.ffmpeg, source_mp4, start_time, end_time, out_file)

    def concatenate_video_clips(self, inputs, out_file: Path) -> None:
        concatenate_video_clips(self.ffmpeg, inputs, out_file)

    def create_face_tracked_vertical_video(
        self,
        input_mp4: str,
        output_mp4: str,
        out_w: int = OUT_W,
        out_h: int = OUT_H,
        smooth: float = SMOOTH,
    ) -> None:
        create_face_tracked_vertical_video(self.ffmpeg.ffmpeg_path, input_mp4, output_mp4, out_w, out_h, smooth)

    def extract_audio_to_wav(self, input_mp4: Path, wav_path: Path, sample_rate: int = 16000) -> None:
        extract_audio_to_wav(self.ffmpeg, input_mp4, wav_path, sample_rate)

    def burn_subtitles_into_video(self, input_mp4: Path, ass_path: Path, out_path: Path) -> None:
        burn_subtitles_into_video(self.ffmpeg, input_mp4, ass_path, out_path)


class SermonSplitterApp(SermonPipeline):
    """Backward-compatible alias for the refactored pipeline orchestrator."""


__all__ = [
    "JITTER_THRESHOLD",
    "OUT_H",
    "OUT_W",
    "SMOOTH",
    "FfmpegManager",
    "SermonSplitterApp",
    "Transcriber",
    "VideoProcessor",
    "VideoUtils",
    "burn_subtitles_into_video",
    "concatenate_video_clips",
    "convert_srt_to_styled_ass",
    "create_face_tracked_vertical_video",
    "cut_video_clip",
    "download_video",
    "extract_audio_to_wav",
    "refit_srt",
]
