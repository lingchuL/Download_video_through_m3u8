# Download_video_through_m3u8
Download ts files with the (given) m3u8 file and merge them into a mp4 file with ffmpeg.

To use it, you may install ffmpeg for Windows cmd at first. Before running, you may change the path of Desktop in code to yours, and put the m3u8 file at Desktop.

May work on downloading the ts files with the original video link, but the goal seems a little difficult and bothering for me right now.

-- 2019.9.5 -- Uploaded a new code which may be useful when the ts files are encrypted. It can decrypt the ts files with the python's AES module. In a few weeks, I may make it modular to be easily imported into other projects.  
-- 2019.10.9 --Replace the old two scripts with one. Changes: 1.No more need to put the m3u8 file on desktop. Now you only need to give the program the web link of m3u8.(Having problem of how to find the link of m3u8, google might be helpful:) 2. You can download a batch of videos just giving a txt file which includes several m3u8 links. You can choose whether to download it in this default way or just download only one video a time.  
-- 2020.4.21 -- Change the method to finding ts links in m3u8 file. Regular expression is good but seems don't fit this problem well. And also, now the code can detect the proxy setting through the computer's registry, which means it can support the vpn now.
