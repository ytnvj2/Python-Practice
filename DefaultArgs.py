# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1*echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo('Hey',5)

# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey',echo=5,intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey',intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for k, v in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(k + ": " + v)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi",status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")


def add_all(*args,n=1):
    sum_all=0
    print(type(args))
    print(n)
    for num in args:
        sum_all+=num
    return sum_all*n;

def key_all(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k)
        print(v)

print(add_all(1,2,3,4,n=2));
print(add_all(1,2,3,4))
key_all(a="asd")
