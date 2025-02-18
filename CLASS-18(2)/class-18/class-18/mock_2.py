def analysis_ratings(ratings):
    if not ratings:
        return None
    
    for i in ratings:
        if not isinstance(i , int):
            return
        
        if i not in [1,2,3,4,5]:
            return
    
    max_rating = max(ratings)
    min_rating = min(ratings)

    return [max_rating, min_rating]



PI = 3.1416

if __name__ == "__main__":
    print(f"Hello from {__name__}")
    print(analysis_ratings([1, 2, '3', 4, 5]))



