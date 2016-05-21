# read the "tweets" from the CSV file and produce a wordcloud
#
# Georgetown CCPE Data Science Program
# Team CDWT
# Created:  May 2016
#
# Copyright (C) 2016
# For license information, see LICENSE.txt
#



import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


cdtwcsvs = ["YOUR_TWITTER_INPUT_FILE.csv"]

for cdtwcsv in cdtwcsvs:
    df = pd.read_csv(cdtwcsv)
    # join tweets to a single string
    words = ' '.join(df['text'])

    # remove URLs, RTs, and twitter handles
    no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])
    #wordcloud = WordCloud(font_path='Verdana.ttf').generate(no_urls_no_tags)
    wordcloud = WordCloud(font_path='/usr/share/fonts/truetype/freefont/FreeSerif.ttf').generate(no_urls_no_tags)
    #wordcloud = WordCloud(font_path='/usr/share/fonts/truetype/freefont/FreeSerif.ttf',
    #                      stopwords=STOPWORDS,background_color='black',width=1800,height=1400).generate(no_urls_no_tags)

    fileNameTemplate = cdtwcsv.replace('', '')[:-3]+"png"


    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig(fileNameTemplate, dpi=300)
    plt.show()
