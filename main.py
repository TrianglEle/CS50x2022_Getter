import os, platform
current_system = platform.system()
if current_system == "Windows":
    os.mkdir(".\Raw_Files")
    os.mkdir(".\Course")
    os.chdir(".\Raw_Files")
    os.mkdir(".\subtitles")
    for i in range (0,11):
        os.system(f"curl https://cdn.cs50.net/2022/fall/lectures/{i}/lang/en/lecture{i}.srt --output .\subtitles\Lecture{i}.txt")
        os.system(f"curl https://cdn.cs50.net/2022/fall/lectures/{i}/lecture{i}-720p.mp4 --output lecture{i}.mp4")
        os.system(f"ffmpeg -i lecture{i}.mp4 -f srt -i .\subtitles\Lecture{i}.txt -map 0:0 -map 0:1 -map 1:0 -c:v copy -c:a copy -c:s srt ..\Course\Week_{i}.mkv")

    os.system("curl https://cdn.cs50.net/2022/fall/lectures/cybersecurity/lang/en/cybersecurity.srt --output .\subtitles\cybersecurity.txt")
    os.system("curl https://cdn.cs50.net/2022/fall/lectures/cybersecurity/cybersecurity-720p.mp4 --output cybersecurity.mp4")
    os.system("ffmpeg -i cybersecurity.mp4 -f srt -i .\subtitles\cybersecurity.txt -map 0:0 -map 0:1 -map 1:0 -c:v copy -c:a copy -c:s srt ..\Course\Cybersecurity.mkv")
    os.rmdir(".\Raw_Files")
else:
    print("Sorry, this currently only works for windows!")