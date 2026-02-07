# to visulaise netflix content
# how many it has parental content and restricted content and Tv14 content
import pandas as pd
import matplotlib.pyplot as plt

# now loading the data
df = pd.read_csv(r"C:\Users\anura\OneDrive\Desktop\matplotlib\projects\netflix_titles.csv")


# now to clean data
df=df.dropna(subset=['show_id', 'type','director','cast','country','date_added','release_year','rating','duration','listed_in','description'])

type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))

plt.bar(type_counts.index, type_counts.values,color=['b','r'],label=["movies","TV shows"])
plt.title("Netflix-Total no. of movies vs TV shows")
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.legend()
plt.savefig("tv shows vs movies.png")

plt.show()

# rating
# rating_counts=df['rating'].value_counts()
# plt.figure(figsize=(8,6))
# plt.pie(rating_counts,labels=rating_counts.index, autopct='%1.1f%%',startangle=90,textprops={'rotation': 45})
# plt.title("Netflix-Percentage of content ratings")
# plt.tight_layout()
# plt.legend()
# plt.savefig("contentratings.jpg")
# plt.show()
rating_counts = df['rating'].value_counts()

# Combine categories below 2%
threshold = 2
small = rating_counts[rating_counts / rating_counts.sum() * 100 < threshold]
rating_counts['Other'] = small.sum()
rating_counts = rating_counts.drop(small.index)


plt.figure(figsize=(9,7))

plt.pie(
    rating_counts,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

plt.legend(
    rating_counts.index,
    title="Ratings",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

plt.title("Netflix Content Ratings Distribution.png")
plt.tight_layout()
plt.show()

# to get movie duration distributed
movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))

plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='k')
plt.title("Netflix-Movie Duration")
plt.xlabel("Duration in minutes")
plt.ylabel("no.of movies")
plt.tight_layout()
plt.savefig("Netflix-movie duration.png")
plt.show()


# release year vs no. of shows

release_counts=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,8))

plt.scatter(release_counts.index,release_counts.values,color="m")
plt.title("Netflix-Release year vs no. of shows")
plt.xlabel("Release year")
plt.ylabel("No.of shows")
plt.tight_layout()
plt.savefig("Netflix-Scatter plot of Release year.png")
plt.show()

# no. of shows by country

country_counts=df['country'].value_counts().head(20)
plt.figure(figsize=(8,8))

plt.barh(country_counts.index,country_counts.values,color="teal")
plt.title("Netflix-Top 20 countries by no. of shows")
plt.xlabel("No.of shows")
plt.ylabel("country")
plt.tight_layout()
plt.grid()
plt.savefig("Netflix-Countrywise content top 20.png")
plt.show()


content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)


fig, ax = plt.subplots(1, 2, figsize=(12,6))

# Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'])
ax[0].set_title("Movies Released per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'])
ax[1].set_title("TV Shows Released per Year")
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle("Comparison of Movies and TV Shows on Netflix")
plt.tight_layout()
plt.savefig("movies_vs_tv_shows_comparison.png")
plt.show()







