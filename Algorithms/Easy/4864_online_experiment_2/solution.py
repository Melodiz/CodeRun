# Solution for https://coderun.yandex.ru/problem/online-experiment-2
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    p = float(input())
    
    dp = {}
    
    dp[(1, 1, 0, 0)] = p      
    dp[(1, 0, 0, 0)] = 1 - p  
    
    for i in range(2, n + 1):
        new_dp = {}
        
        for (pos, last, x, y), prob in dp.items():
            if pos != i - 1:
                continue
                
            new_x, new_y = x, y
            if last == 1: 
                new_y += 1
            
            key = (i, 1, new_x, new_y)
            new_dp[key] = new_dp.get(key, 0) + prob * p

            new_x, new_y = x, y
            if last == 1: 
                new_x += 1
            
            key = (i, 0, new_x, new_y)
            new_dp[key] = new_dp.get(key, 0) + prob * (1 - p)
        
        dp.update(new_dp)
    
    petya_wins = 0  
    draw = 0        
    vasya_wins = 0  
    
    for (pos, last, x, y), prob in dp.items():
        if pos == n:
            if x > y:
                petya_wins += prob
            elif x == y:
                draw += prob
            else:
                vasya_wins += prob
    
    print(f"{round(petya_wins, 10)} {round(draw, 10)} {round(vasya_wins, 10)}")

if __name__ == "__main__":
    main()
