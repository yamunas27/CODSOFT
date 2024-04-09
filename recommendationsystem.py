# Sample user-item ratings data
data = {
    'user1': {'Item1': 5, 'Item2': 0, 'Item3': 4, 'Item4': 0},
    'user2': {'Item1': 4, 'Item2': 0, 'Item3': 5, 'Item4': 0},
    'user3': {'Item1': 0, 'Item2': 3, 'Item3': 0, 'Item4': 2},
    'user4': {'Item1': 0, 'Item2': 4, 'Item3': 0, 'Item4': 3}
}

# Calculate similarity between users using Pearson correlation coefficient
def pearson_correlation(user1, user2):
    common_items = [item for item in user1 if item in user2]
    if len(common_items) == 0:
        return 0
    sum1 = sum(user1[item] for item in common_items)
    sum2 = sum(user2[item] for item in common_items)
    sum_sq1 = sum(user1[item] ** 2 for item in common_items)
    sum_sq2 = sum(user2[item] ** 2 for item in common_items)
    sum_prod = sum(user1[item] * user2[item] for item in common_items)
    num = sum_prod - (sum1 * sum2 / len(common_items))
    den = ((sum_sq1 - (sum1 * 2 / len(common_items))) * 0.5) * ((sum_sq2 - (sum2 * 2 / len(common_items))) * 0.5)
    if den == 0:
        return 0
    return num / den

# Get user input for target user
target_user = input("Enter user: ")

if target_user in data:
    target_ratings = data[target_user]

    # Generate recommendations for target user
    recommendations = []
    for other_user, other_ratings in data.items():
        if target_user != other_user:
            similarity = pearson_correlation(target_ratings, other_ratings)
            for item, rating in other_ratings.items():
                if rating > 0 and target_ratings.get(item) == 0:
                    recommendations.append((item, similarity))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    print(f"Recommendations for {target_user}: {[item[0] for item in recommendations[:3]]}")
else:
    print("User not found.")