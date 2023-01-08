# Garfield-Comic-Mass-Downloader
 It takes way too fucking long to download them all
 
 This is a scraper for gogocomics.com, specifically the Garfield comics. It downloads them all into the directory where py file is located. Also, sometimes when mass downloading its going to mess up a download once in a while, idk, go into the code and change start_date and end_date

 How to run?
You're first going to need to make sure you have the following packages:

`pip install bs4`
`pip install time`
`pip install schedule`
`pip install request`

Then run `massdownloader.py` and let it run for however long it will require to download 16.5k Garfield comics

During the download, some files might fail to download either due to the request failing or whatever, afterwards just run `fixer.py`, it will download all files that failed to download