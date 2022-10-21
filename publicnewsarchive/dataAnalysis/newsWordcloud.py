import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
from collections import Counter

def newsWordcloud(input_filename, output_filename):
    path = "data/"
    jsonFile = open(path + input_filename, encoding="utf8")
    data = json.load(jsonFile)

    Keywords = []

    for newsarticle in data:
        for keyword in newsarticle['Keywords']:
            Keywords.append(keyword[0])

    freq = Counter(Keywords)
    wordcloud = WordCloud(width=900, height=900, background_color='white').generate_from_frequencies(freq)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f'{path + output_filename}', bbox_inches='tight')



