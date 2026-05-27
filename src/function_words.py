"""
Curated closed-class English function word list for stylometric analysis.
These are topic-invariant: articles, prepositions, conjunctions, pronouns,
auxiliaries, modals, common adverbs.
Source: composite of Mosteller-Wallace (1964), Burrows (1987), and stylo R package
default English list, deduplicated and lowercased.
"""

FUNCTION_WORDS = [
    # Articles + determiners
    "a", "an", "the", "this", "that", "these", "those",
    # Pronouns
    "i", "me", "my", "mine", "myself",
    "we", "us", "our", "ours", "ourselves",
    "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself",
    "she", "her", "hers", "herself",
    "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves",
    "who", "whom", "whose", "which", "what",
    "someone", "anyone", "everyone", "no", "none", "any",
    "some", "all", "each", "every", "both", "either", "neither",
    "few", "many", "several", "much",
    # Be / have / do
    "is", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having",
    "do", "does", "did", "doing", "done",
    # Modals
    "will", "would", "shall", "should", "can", "could",
    "may", "might", "must", "ought",
    # Prepositions
    "of", "to", "in", "for", "on", "with", "at", "by", "from",
    "about", "into", "through", "during", "before", "after",
    "above", "below", "between", "under", "over", "against",
    "without", "within", "among", "across", "behind",
    "beyond", "since", "until", "upon", "toward", "towards",
    "around", "near", "throughout", "via",
    # Conjunctions / connectives
    "and", "but", "or", "nor", "yet", "so",
    "if", "though", "although", "while", "whereas", "because",
    "unless", "whether", "as", "than", "that",
    "however", "therefore", "thus", "hence", "moreover",
    "furthermore", "nevertheless", "nonetheless", "indeed",
    "otherwise", "instead", "meanwhile",
    # Common adverbs (topic-invariant)
    "not", "no", "very", "too", "also", "even", "still",
    "just", "only", "more", "most", "less", "least",
    "again", "now", "then", "here", "there", "where",
    "when", "why", "how", "perhaps", "almost", "really",
    "always", "never", "often", "sometimes", "usually",
    "well", "much", "rather", "quite", "ever", "yet",
    # Auxiliaries / common verbs (frequency-invariant intent)
    "make", "made", "made", "get", "got", "go", "going", "went",
    # Linkers
    "such", "same", "other", "another", "own", "out", "up", "down",
    "off", "again", "back",
]

FUNCTION_WORDS = sorted(set(FUNCTION_WORDS))
