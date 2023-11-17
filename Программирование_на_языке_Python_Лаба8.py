from PIL import Image, ImageSequence
import os

class GifProcessor:
    def __init__(self):
        pass

    @staticmethod
    def split_gif(gif_path):
        with Image.open(gif_path) as img:
            frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

        base_path, ext = os.path.splitext(gif_path)
        output_dir = f"{base_path}_frames"
        os.makedirs(output_dir, exist_ok=True)

        frame_paths = []
        for i, frame in enumerate(frames):
            frame_path = os.path.join(output_dir, f"frame_{i + 1}.png")
            frame.save(frame_path, "PNG")
            frame_paths.append(frame_path)

        return frame_paths

    @staticmethod
    def create_gif_from_frames(frame_dir, output_gif_path):
        frames = []
        for file_name in sorted(os.listdir(frame_dir)):
            if file_name.endswith(".png"):
                frame_path = os.path.join(frame_dir, file_name)
                frame = Image.open(frame_path)
                frames.append(frame)

        frames[0].save(output_gif_path, format="GIF", save_all=True, append_images=frames[1:], duration=100, loop=0)


if __name__ == "__main__":
    gif_path = "C:\Games\pWV5zlPXlUwAAAAd.gif"
    gif_processor = GifProcessor()

    frame_paths = gif_processor.split_gif(gif_path)
    print(f"Frames saved at: {', '.join(frame_paths)}")

    output_gif_path = "C:\Games\pWV5zlPXlUwAAASHEESH.gif"
    gif_processor.create_gif_from_frames("C:\Games\pWV5zlPXlUwAAAAd_frames", output_gif_path)
    print(f"New gif saved at: {output_gif_path}")

