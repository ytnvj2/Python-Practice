import pandas as pd

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    try:

        # Extract column from DataFrame: col
        col = df[col_name]
        # Iterate over lang column in DataFrames
        for entry in col:

            # If the language is in langs_count, add 1
            if entry in langs_count.keys():
                langs_count[entry]+=1
            # Else add the language to langs_count, set the value to 1
            else:
                langs_count[entry]=1;

        # Return the langs_count dictionary
        return langs_count

    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result
result=count_entries(tweets_df,'lang')

# Print the result
print(result)



# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)



# Select retweets from the Twitter DataFrame: result
result = filter(lambda tweet:tweet[:2]=='RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list=list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
