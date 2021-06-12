import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.ticker

# def catagory_dict(df, dict):




# US_df['title'].value_counts().value_counts(lambda x:x>1)

if __name__ == '__main__':
    US_df = pd.read_csv('/Volumes/64gig data_sets/youtube_data/USvideos.csv')
    USjson_df = pd.read_json('/Volumes/64gig data_sets/youtube_data/US_category_id.json')

    catagory_dict={
2 : 'Autos & Vehicles'
,1 :  'Film & Animation'
,10 : 'Music'
,15 : 'Pets & Animals'
,17 : 'Sports'
,18 : 'Short Movies'
,19 : 'Travel & Events'
,20 : 'Gaming'
,21 : 'Videoblogging'
,22 : 'People & Blogs'
,23 : 'Comedy'
,24 : 'Entertainment'
,25 : 'News & Politics'
,26 : 'Howto & Style'
,27 : 'Education'
,28 : 'Science & Technology'
,29 : 'Nonprofits & Activism'
,30 : 'Movies'
,31 : 'Anime/Animation'
,32 : 'Action/Adventure'
,33 : 'Classics'
,34 : 'Comedy'
,35 : 'Documentary'
,36 : 'Drama'
,37 : 'Family'
,38 : 'Foreign'
,39 : 'Horror'
,40 : 'Sci-Fi/Fantasy'
,41 : 'Thriller'
,42 : 'Shorts'
,43 : 'Shows'
,44 : 'Trailers'}

    US_df['catagory_new']= US_df.category_id.map(catagory_dict)

    catagory_df = US_df.groupby(by=["catagory_new"], dropna=False).sum()

    # catagory_df.sort_values('views', ascending=False)[['views']].plot.bar()
    # plt.title( 'views by catagory')
    # plt.ylabel('Views (tens of Billions)')
    # plt.xlabel('')
    # plt.yticks(fontsize = 8)
    # plt.xticks(fontsize = 8)
    # plt.tight_layout()

    # plt.savefig("squares.png")
    # plt.savefig("views_by_catagory.png")
    # plt.show()

    # catagory_df.sort_values('likes', ascending=False)[['likes']].plot.bar()
    # plt.title( 'Likes by catagory')
    # plt.ylabel('Views (Billions)')
    # plt.xlabel('')
    # plt.yticks(fontsize = 8)
    # plt.xticks(fontsize = 8)
    # plt.tight_layout()
    # plt.savefig("likes_by_catagory.png")
    # plt.show()


    # catagory_df.sort_values('comment_count', ascending=False)[['comment_count']].plot.bar()
    # plt.title( 'Comments by catagory')
    # plt.ylabel('Comments (Tens of Millions)')
    # plt.xlabel('')
    # plt.yticks(fontsize = 8)
    # plt.xticks(fontsize = 8)
    # plt.tight_layout()
    # plt.savefig("comments_by_catagory.png")
    # plt.show()

    # US_df['channel_title'].value_counts().loc[lambda x : x>1].hist()

    # plt.title( 'Distribution of Videos per Channel')
    # plt.ylabel('Number of Videos')
    # plt.xlabel('Number of Channels')
    # plt.yticks(fontsize = 8)
    # plt.xticks(fontsize = 8)
    # plt.tight_layout()
    # plt.savefig("dist_videos_per_channel.png")
    # plt.show()

    # rating_disabled_df = US_df[US_df.ratings_disabled == True]
    # rating_disabled_df_catagory_df = rating_disabled_df.groupby(by=["catagory_new"], dropna=False).sum()
    # rating_disabled_df_catagory_df.sort_values('views', ascending=False)[['views']].plot.bar()
    # plt.title( 'Disabled Ratings by Catagory')
    # plt.ylabel('Views (Tens of Millions)')
    # plt.xlabel('')
    # plt.yticks(fontsize = 8)
    # plt.xticks(fontsize = 8)
    # plt.tight_layout()
    # plt.savefig("Disable_ratings_by_cat.png")
    # plt.show()

    comment_disabled_df = US_df[US_df.comments_disabled == True]
    comment_disabled_df_df_catagory_df = comment_disabled_df.groupby(by=["catagory_new"], dropna=False).sum()
    comment_disabled_df_df_catagory_df.sort_values('views', ascending=False)[['views']].plot.bar()
    plt.title( 'Comments Disabled by Catagory')
    plt.ylabel('Views (Tens of Millions)')
    plt.xlabel('')
    plt.yticks(fontsize = 8)
    plt.xticks(fontsize = 8)
    plt.tight_layout()
    plt.savefig("Disable_comments_by_cat.png")
    plt.show()