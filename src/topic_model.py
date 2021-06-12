import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

def hand_label_topics(H, vocabulary):
    '''
    Print the most influential words of each latent topic, and prompt the user
    to label each topic. The user should use their humanness to figure out what
    each latent topic is capturing.
    '''
    hand_labels = []
    for i, row in enumerate(H):
        top_five = np.argsort(row)[::-1][:20]
        print('topic', i)
        print('-->', ' '.join(vocabulary[top_five]))
#         label = input('please label this topic: ')
#         hand_labels.append(label)
        print()
    return hand_labels

def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[:-n_top_words - 1:-1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f'Topic {topic_idx +1}',
                     fontdict={'fontsize': 30})
        ax.invert_yaxis()
        ax.tick_params(axis='both', which='major', labelsize=20)
        for i in 'top right left'.split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.savefig("tags_catagory_clustering.png")
    plt.show()




if __name__ == '__main__':
    US_df = pd.read_csv('/Volumes/64gig data_sets/youtube_data/USvideos.csv')
    USjson_df = pd.read_json('/Volumes/64gig data_sets/youtube_data/US_category_id.json')

    vectorizer = CountVectorizer (max_features = 5000, stop_words = 'english', strip_accents='unicode')

    text = US_df.tags
    X = vectorizer.fit_transform(text)

    feature_names = vectorizer.get_feature_names()
    feature_names

    vocabulary = np.array(feature_names)

    k =10
    nmf = NMF(n_components=k, init='random', random_state=0)
    W = nmf.fit_transform(X)
    H = nmf.components_


    hand_label_topics(H, vocabulary)

    n_samples = 2000
    n_features = 1000
    n_components = 10
    n_top_words = 20

    tf_feature_names = vectorizer.get_feature_names()
    plot_top_words(nmf, tf_feature_names, n_top_words, 'Youtube tags groupings')