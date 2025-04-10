# Function to play the Minion Game
def minion_game(word):
    # Define vowels for Kevin's score
    vowels = 'AEIOUaeiou'
    # Initialize scores for Kevin and Stuart
    kevin_score = 0
    stuart_score = 0
    # Get the length of the word
    word_length = len(word)

    # Loop through each character in the word
    for i in range(word_length):
        # If the character is a vowel, add points to Kevin's score
        if word[i] in vowels:
            kevin_score += word_length - i
        # Otherwise, add points to Stuart's score
        else:
            stuart_score += word_length - i

    # Determine the winner based on the scores
    if kevin_score > stuart_score:
        # Print Kevin's score if he wins
        print(f'Kevin {kevin_score}')
    elif stuart_score > kevin_score:
        # Print Stuart's score if he wins
        print(f'Stuart {stuart_score}')
    else:
        # Print 'Draw' if scores are equal
        print('Draw')

# Take input from the user for the word
s = input()
# Call the function to play the game with the input word
minion_game(s)