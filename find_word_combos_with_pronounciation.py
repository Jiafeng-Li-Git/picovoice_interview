
extended_dict = {("AE", "B", "AH", "K", "AH", "S"): ["ABACUS"],
                 ("B", "UH", "K"): ["BOOK"],
                 ("DH", "EH", "R"): ["THEIR", "THERE"],
                 ("T", "AH", "M", "AA", "T", "OW"): ["TOMATO"],
                 }


def find_word_combos_with_pronunciation(phonemes):
    # Initialize an empty list to hold the output text
    text = []

    # Iterate over each possible sublist of the input phonemes
    i = 0
    while i < len(phonemes):
        for j in range(i + 1, len(phonemes) + 1):
            sublist = phonemes[i:j]

            # Check if the sublist corresponds to a word in the phoneme map
            if tuple(sublist) in extended_dict:
                # If the sublist has multiple possible words, append all of them to the output text
                possible_words = extended_dict[tuple(sublist)]
                if not text:
                    text = [[word] for word in possible_words]
                else:
                    new_text = []
                    for word in possible_words:
                        for t in text:
                            new_text.append(t + [word])
                    text = new_text
                i = j
                break
            elif j == len(phonemes):
                i = j
                break

    return text


print(find_word_combos_with_pronunciation(["DH", "EH", "R", "DH", "EH", "R", "DH", "EH", "R"]))



