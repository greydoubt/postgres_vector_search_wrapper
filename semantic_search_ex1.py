import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor
cur = conn.cursor()

# Define the query for vector search
def vector_search(query_vector, table_name, vector_column, similarity_threshold):
    cur.execute(
        f"SELECT * FROM {table_name} WHERE {vector_column} <-> %s < %s",
        (query_vector, similarity_threshold)
    )
    results = cur.fetchall()
    return results

# Example usage
if __name__ == '__main__':
    # Assuming you have a table called 'movies' with a 'description' column
    table_name = 'movies'
    vector_column = 'description_vector'
    similarity_threshold = 0.8
    query_vector = [0.5, 0.2, 0.7, ...]  # Example query vector

    # Perform the vector search
    search_results = vector_search(query_vector, table_name, vector_column, similarity_threshold)

    # Print the search results
    for result in search_results:
        print(result)

# Close the cursor and connection
cur.close()
conn.close()
