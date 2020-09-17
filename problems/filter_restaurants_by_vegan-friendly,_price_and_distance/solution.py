from collections import namedtuple

    
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int):
        # entry format is [id, rating, veganFriendly, price, distance]
        Restaurant = namedtuple('Restaurant', ['id', 'rating', 'veganFriendly', 'price', 'distance'])
        r_tuples = [Restaurant(*r) for r in restaurants]
        r_tuples = [r for r in r_tuples if r.price <= maxPrice and r.distance <= maxDistance]
        if veganFriendly:
            r_tuples = [r for r in r_tuples if r.veganFriendly == veganFriendly]
        r_tuples.sort(key=lambda r: (r.rating, r.id), reverse=True)
        return [r.id for r in r_tuples]
    