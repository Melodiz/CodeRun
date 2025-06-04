# Solution for https://coderun.yandex.ru/problem/neuro-logo
# Other solutions: https://github.com/Melodiz/CodeRun

import csv

def load_data(filename):
    """Load the TSV data file without pandas"""
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            # Convert votes to int
            row['p1_votes'] = int(row['p1_votes'])
            row['p2_votes'] = int(row['p2_votes'])
            data.append(row)
    return data

def bradley_terry_ranking(data, iterations=100):
    """Bradley-Terry model for pairwise comparisons (no pandas)"""
    # Get all unique players
    players = set(row['p1'] for row in data) | set(row['p2'] for row in data)
    players = sorted(list(players))
    
    # Initialize ratings (all equal initially)
    ratings = {player: 1.0 for player in players}
    
    # Iterative algorithm
    for _ in range(iterations):
        new_ratings = {player: 0.0 for player in players}
        denominators = {player: 0.0 for player in players}
        
        for row in data:
            p1, p2 = row['p1'], row['p2']
            p1_votes, p2_votes = row['p1_votes'], row['p2_votes']
            total_votes = p1_votes + p2_votes
            
            # Bradley-Terry probability
            prob_p1_wins = ratings[p1] / (ratings[p1] + ratings[p2])
            prob_p2_wins = ratings[p2] / (ratings[p1] + ratings[p2])
            
            # Update numerators (wins)
            new_ratings[p1] += p1_votes
            new_ratings[p2] += p2_votes
            
            # Update denominators (expected wins)
            denominators[p1] += total_votes * prob_p1_wins
            denominators[p2] += total_votes * prob_p2_wins
        
        # Update ratings
        for player in players:
            if denominators[player] > 0:
                ratings[player] = new_ratings[player] / denominators[player]
    
    # Sort by rating
    rankings = [(player, ratings[player]) for player in players]
    rankings.sort(key=lambda x: x[1], reverse=True)
    return rankings

def main():
    # Try to load the actual data first, fall back to sample data
    try:
        data = load_data('dataset.tsv')
        print("Loaded dataset.tsv file")
    except:
        try:
            data = load_data('sample_data.tsv')
            print("Loaded sample data file")
        except:
            print("No data file found!")
            return
    
    print(f"Data shape: ({len(data)}, 4)")
    unique_players = sorted(set(row['p1'] for row in data) | set(row['p2'] for row in data))
    print(f"Unique players: {unique_players}")
    print()
    
    # Method 3: Bradley-Terry Model
    print("=== Bradley-Terry Model ===")
    bt_rankings = bradley_terry_ranking(data)
    for i, (player, rating) in enumerate(bt_rankings[:10]):
        print(f"{i+1}. {player}: Rating = {rating:.3f}")
    print(f"Top 3: {' '.join([r[0] for r in bt_rankings[:3]])}")
    print()

if __name__ == "__main__":
    main()
