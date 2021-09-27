import pandas as pd
import os
from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from config import Hyper
from helper import Helper

'''
    This program is the fourth in a suite of programs to be executed in this order
    1/ App - gets tweets from Twitter API
    2/ Location - gets the country of the tweet from user location
    3/ Annotate - calculates the sentiment of each tweet
    4/ Wordcload - shows the words most in use in tweets from different countries
    5/ Datapreparation - gets the data in the correct form
    6/ Transformer - builds a transformer model from the tweets
'''
# See https://www.datacamp.com/community/tutorials/wordcloud-python
def main():
    Helper.printline(f"     Start wordcount")
    Helper.create_directory(Hyper.WordcloudDir)
    # Create stopword list:
    stopwords = set(STOPWORDS)
    stopwords.update(["coronavirus", "covid", "time", "today", "know", "support", "update", "say", "take", "please", "need", "well", "think", "virus", "thank", "read", "new", "going", "read", "help", "people", "let", "will", "one", "said", "due", "see", "day", "via", "make", "call", "really", "every", "great", "still", "keep", "now", "im", "case", "patient", "everyone", "many", "corona", "says", "go", "even", "week", "dont", "outbreak", "first", "cant", "way", "good", "work", "spread", "live", "right", "come", "back", "news", "stop", "number", "want", "may", "home", "country", "hope", "got", "US", "pandemic", "crisis", "cases", "stay", "thing", "amid", "look"])
    dirs = Helper.list_country_folders(Hyper.DataDir)
    for countrydir in dirs:
        countryfile = path.join(Hyper.DataDir, countrydir, Hyper.TweetFile)
        Helper.printline(f"     Generate wordcloud for country {countrydir}")
        filename = f"wordcloud_{countrydir}.png"
        wordcloudfig = path.join(Hyper.WordcloudDir, filename)
        output_wordcloud(countryfile, wordcloudfig, stopwords)
        Helper.printline(f"     Wordcloud output for country {countrydir}")
    
    Helper.printline(" The End")

def output_wordcloud(countryfile, wordcloudfig, stopwords):
    df = pd.read_csv(countryfile, index_col=0)
    print(df.head())
    text_arr = df["Tweet"].values
    text = ""
    for txt in text_arr:
        if type(txt) == str:
            text = " ".join([text, txt])
    Helper.printline(f"     There are {len(text)} words used in the selected tweets")
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(wordcloudfig)
    
if __name__ == "__main__":
    main()