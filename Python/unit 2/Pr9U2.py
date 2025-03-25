# Function to split text into words
def split_text_into_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()  
    return words

def join_words_to_sentences(words):
    return ' '.join(words) 

input_file = 'example_file8.txt'  
output_file = 'output.txt'  

# Process the files
try:
    words = split_text_into_words(input_file)
    
    sentence = join_words_to_sentences(words)
    
    with open(output_file, 'w') as file:
        file.write(sentence)
    
    print(f"Text has been processed and saved to {output_file}.")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")