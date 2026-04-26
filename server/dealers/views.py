from django.http import JsonResponse

def get_dealer_reviews(request, dealer_id):
    reviews = [
        {
            "dealer_id": dealer_id,
            "review": "Excellent service",
            "rating": 5
        },
        {
            "dealer_id": dealer_id,
            "review": "Very professional staff",
            "rating": 4
        }
    ]
    return JsonResponse(reviews, safe=False)
def get_all_dealers(request):
    dealers = [
        {
            "id": 1,
            "name": "Pune Cars",
            "location": "Pune"
        },
        {
            "id": 2,
            "name": "Mumbai Motors",
            "location": "Mumbai"
        }
    ]
    return JsonResponse(dealers, safe=False)
def get_dealer_by_id(request, dealer_id):
    dealers = [
        {"id": 1, "name": "Pune Cars", "location": "Pune"},
        {"id": 2, "name": "Mumbai Motors", "location": "Mumbai"}
    ]

    for dealer in dealers:
        if dealer["id"] == dealer_id:
            return JsonResponse(dealer)

    return JsonResponse({"error": "Dealer not found"}, status=404)