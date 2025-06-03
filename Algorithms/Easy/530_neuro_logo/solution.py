# Solution for https://coderun.yandex.ru/problem/neuro-logo
# Other solutions: https://github.com/Melodiz/CodeRun

import pandas as pd

def load_data(filename):
    """Load the TSV data file"""
    return pd.read_csv(filename, sep='\t')

def bradley_terry_ranking(df, iterations=100):
    """Bradley-Terry model for pairwise comparisons"""
    # Get all unique players
    players = set(df['p1'].unique()) | set(df['p2'].unique())
    players = sorted(list(players))
    
    # Initialize ratings (all equal initially)
    ratings = {player: 1.0 for player in players}
    
    # Iterative algorithm
    for _ in range(iterations):
        new_ratings = {player: 0.0 for player in players}
        denominators = {player: 0.0 for player in players}
        
        for _, row in df.iterrows():
            p1, p2, p1_votes, p2_votes = row['p1'], row['p2'], row['p1_votes'], row['p2_votes']
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
        df = load_data('dataset.tsv')
        print("Loaded dataset.tsv file")
    except:
        try:
            df = load_data('sample_data.tsv')
            print("Loaded sample data file")
        except:
            print("No data file found!")
            return
    
    print(f"Data shape: {df.shape}")
    print(f"Unique players: {sorted(set(df['p1'].unique()) | set(df['p2'].unique()))}")
    print()
    
    # Method 3: Bradley-Terry Model
    print("=== Bradley-Terry Model ===")
    bt_rankings = bradley_terry_ranking(df)
    for i, (player, rating) in enumerate(bt_rankings[:10]):
        print(f"{i+1}. {player}: Rating = {rating:.3f}")
    print(f"Top 3: {' '.join([r[0] for r in bt_rankings[:3]])}")
    print()

if __name__ == "__main__":
    main()
