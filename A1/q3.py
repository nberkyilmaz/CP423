#Import inverted index
from q2 import build_inverted_index

def evaluate_query(inverted_index, query):
    # Tokenize the query based on spaces, assuming a space-delimited format
    tokens = query.upper().split()
    # Initialize an empty result set
    result_set = None
    # Keep track of the current operator
    current_operator = None
    #Keep track of total comparisons
    total_comparisons = 0  

    for token in tokens:
        if token in ['AND', 'OR', 'NOT']:
            # Update the current operator if an operator token is encountered
            current_operator = token
        else:
            # Convert the token to lowercase for consistent matching
            token = token.lower()
            # Retrieve the document set for the current token (word) from the inverted index
            current_set = inverted_index.get(token, set())

            if current_operator == 'AND':
                if result_set is not None:
                    #Increasing total comparison by length of result set intersect the current set
                    total_comparisons += len(result_set) + len(current_set)
                # Intersect with the result set if the operator is AND
                result_set = result_set & current_set if result_set is not None else current_set
            elif current_operator == 'OR':
                if result_set is not None:
                    total_comparisons += len(result_set) + len(current_set)
                # Union with the result set if the operator is OR
                result_set = result_set | current_set if result_set is not None else current_set
            elif current_operator == 'NOT':
                if result_set is not None:
                    total_comparisons += len(result_set) + len(current_set)
                    # Subtract from the result set if the operator is NOT
                    result_set = result_set - current_set
                else:
                    all_documents = set.union(*inverted_index.values())
                    result_set = all_documents - current_set
            else:
                # Initialize result_set with the current set if no operator is set
                result_set = current_set
            # Reset the operator after processing
            current_operator = None

    return result_set, total_comparisons


if __name__ == "__main__":
    # Build the inverted index from the files in data set 
    inverted_index = build_inverted_index()

    # Define queries to test the inverted index
    queries = [
        "Holmes OR Watson",
        "Holmes AND Watson",
        "Holmes AND NOT Moriarty",
        "Holmes OR NOT Lestrade"
    ]

    # Test executing the queries against the inverted index
    for query in queries:
        result_files = evaluate_query(inverted_index, query)
        print(f"Query '{query}' found in files: {result_files}")