import random

def build_markov_chain(text):
    words = text.split()
    chain = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in chain:
            chain[current_word] = []
        chain[current_word].append(next_word)
    return chain

def generate_text(chain, length):
    word = random.choice(list(chain.keys()))
    result = [word]
    
    for _ in range(length - 1):
        next_words = chain.get(word, None)
        if not next_words:
            break
        word = random.choice(next_words)
        result.append(word)
    
    return " ".join(result)

# Example usage
text = "this is a sample text to demonstrate markov chain text generation this is fun"
chain = build_markov_chain(text)

if __name__ == "__main__":
    generated = generate_text(chain, 10)
    print("Generated text:", generated)