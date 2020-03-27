bands = ("Journey", "Foreigner", "Garth Brooks", "REO Speedwagon", "Styx", "Thompson Twins", "Tiffany", "Debbie Gibson", "The Beatles", "Herman's Hermits", "Neil Diamond", "The Monkees")
bandRatings = {}

for band in bands:
    print("Rate " + band + ". (1-10)")
    rating = input(": ")
    bandRatings.update({band : rating})
totalRatings = 0
numRatings = 0

print("\nYour Ratings:")
for band, rating in bandRatings.items():
    print(band + ": " + str(rating))
    totalRatings = totalRatings + rating
    numRatings = numRatings + 1
average = totalRatings/numRatings

print("\nYour average Rating is a: " + str(average))
