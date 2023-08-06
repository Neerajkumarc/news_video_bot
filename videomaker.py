import break_words
from moviepy.editor import *
from moviepy.audio.io.AudioFileClip import AudioFileClip

def videoMaker(image, text, audio, output):
    print("Video creation started....")
    imageToAdd = ImageClip(image)
    textToAdd = break_words.break_text_into_lines(text, 40)
    audioToAdd = AudioFileClip(audio)
    txt_clip = TextClip(textToAdd, fontsize=15, color="white")
    txt_clip = txt_clip.set_position(('center')).set_duration(audioToAdd.duration)
    video = CompositeVideoClip([imageToAdd, txt_clip]).set_duration(audioToAdd.duration)
    video = video.set_audio(audioToAdd)
    video.write_videofile(output, codec='libx264', audio_codec='aac', fps=12, audio_bitrate="192k")
