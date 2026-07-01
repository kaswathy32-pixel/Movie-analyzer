import pandas as pd
import matplotlib.pyplot as plt

# ── 1. Create sample movie data ────────────────────────────────────────────
data = {
    "Movie":  ["Inception", "The Dark Knight", "Interstellar", "Titanic",
               "The Notebook", "La La Land", "Avengers: Endgame", "Joker",
               "Toy Story", "Frozen", "The Conjuring", "Get Out",
               "The Matrix", "John Wick", "Coco"],
    "Genre":  ["Sci-Fi", "Action", "Sci-Fi", "Romance",
               "Romance", "Romance", "Action", "Drama",
               "Animation", "Animation", "Horror", "Horror",
               "Sci-Fi", "Action", "Animation"],
    "Rating": [8.8, 9.0, 8.6, 7.8,
               7.9, 8.0, 8.4, 8.5,
               8.3, 7.4, 7.5, 7.7,
               8.7, 7.4, 8.4],
}

# ── 2. Build DataFrame ──────────────────────────────────────────────────────
df = pd.DataFrame(data)

# ── 3. Find the top-rated movie per genre ───────────────────────────────────
# idxmax() finds the row index of the highest rating WITHIN each genre group
top_movie_idx = df.groupby("Genre")["Rating"].idxmax()
top_movies = df.loc[top_movie_idx].sort_values("Genre").reset_index(drop=True)

# ── 4. Compute average rating per genre ─────────────────────────────────────
genre_avg = df.groupby("Genre")["Rating"].mean().sort_values(ascending=False)

# ── 5. Console report ────────────────────────────────────────────────────────
print("=" * 55)
print("        MOVIE RATINGS DASHBOARD")
print("=" * 55)

print("\n── All Movies ──────────────────────────────────────")
print(df.to_string(index=False))

print("\n── Top-Rated Movie per Genre ───────────────────────")
print(top_movies.to_string(index=False))

print("\n── Average Rating per Genre ────────────────────────")
print(genre_avg.round(2).to_string())

print("\n── Overall Stats ───────────────────────────────────")
print(f"  Total movies      : {len(df)}")
print(f"  Total genres      : {df['Genre'].nunique()}")
print(f"  Highest rated     : {df.loc[df['Rating'].idxmax(), 'Movie']} "
      f"({df['Rating'].max()})")
print(f"  Lowest rated      : {df.loc[df['Rating'].idxmin(), 'Movie']} "
      f"({df['Rating'].min()})")
print("=" * 55)

# ── 6. Visualizations ────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
fig.suptitle("Movie Ratings Dashboard", fontsize=15, fontweight="bold")

colors = ["#5b8dee", "#f4a942", "#48bb78", "#e05c5c", "#9b6ddf"]

# Chart 1 — Bar chart: average rating by genre
axes[0].bar(genre_avg.index, genre_avg.values, color=colors, edgecolor="white")
axes[0].set_title("Average Rating by Genre")
axes[0].set_ylabel("Average Rating")
axes[0].set_ylim(0, 10)
for i, v in enumerate(genre_avg.values):
    axes[0].text(i, v + 0.15, f"{v:.1f}", ha="center", fontsize=10)

# Chart 2 — Horizontal bar: top-rated movie per genre
axes[1].barh(top_movies["Movie"], top_movies["Rating"], color=colors, edgecolor="white")
axes[1].set_title("Top-Rated Movie per Genre")
axes[1].set_xlabel("Rating")
axes[1].set_xlim(0, 10)
for i, v in enumerate(top_movies["Rating"]):
    axes[1].text(v + 0.1, i, f"{v}", va="center", fontsize=9)

plt.tight_layout()
plt.savefig("movie_ratings_charts.png", dpi=130, bbox_inches="tight")
plt.show()
print("\nCharts saved to movie_ratings_charts.png")