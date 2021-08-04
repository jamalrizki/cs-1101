
cross_promo_podcasts = [{'id': '41a4dabb-f247-4eb3-a6e3-f62b39d585e8', 'priority': 6, 'title': 'It Was Said', 'image_url': '/static/img/cover-images/it-was-said.jpg', 'slug': 'it-was-said', 'author': 'C13Originals | Jon Meacham | The HISTORY® Channel'}, {'id': 'c065f8c9-2262-45b6-81d1-4e246d5f88c7', 'priority': 5, 'title': 'Relative Unknown', 'image_url': 'https://megaphone.imgix.net/podcasts/a9a2787a-d72a-11ea-b74e-73d602820fdd/image/uploads_2F1596655237594-zxylftpi7j-d0e4fc31c42aa49ea554ec9e56d2f4d5_2FRelative%2BUnknown%2BCover_1800.jpg?ixlib=rails-2.1.2&w=250', 'slug': 'relative-unknown', 'author': 'C13Originals'}, {'id': '2c68e65a-f5d1-41a8-a350-921354bac6e5', 'priority': 4, 'title': 'Once Upon a Time… In the Valley', 'image_url': 'https://megaphone.imgix.net/podcasts/454a54b8-bbde-11ea-82da-87a3b5598a13/image/uploads_2F1594046357146-je7jqmzxgz-05fbfaa9daa41742e7a32717074d9c06_2FOnce%2BUpon%2Ba%2BTime%2BCovers%2BFINAL%2B1800.jpg?ixlib=rails-2.1.2&w=250', 'slug': 'in-the-valley', 'author': 'C13Originals'}, {'id': 'f57e22d4-eec4-45e9-80d2-175a2de702e0', 'priority': 3, 'title': 'Hope, Through History', 'image_url': 'https://megaphone.imgix.net/podcasts/d7209054-7a9e-11ea-8538-ab7bc78732e3/image/HTH_S2_FinalCover_1800.jpg?ixlib=rails-2.1.2&w=250', 'slug': 'hope-through-history', 'author': 'C13Originals | Jon Meacham | The HISTORY® Channel'}, {'id': 'b5a631f7-4780-4d44-97a8-19b8d12c9dfc', 'priority': 2, 'title': 'Gangster Capitalism', 'image_url': '/static/img/cover-images/gangster-capitalism.jpg', 'slug': 'gangster-capitalism', 'author': 'C13Originals'}, {'id': 'e432d67e-9dda-4182-9ed0-9e690a8cef88', 'priority': 1, 'title': 'Long May They Run', 'image_url': '/static/img/cover-images/lmtr.jpg', 'slug': 'lmtr', 'author': 'C13Originals'}]



def shuffle_podcasts(cross_promo_podcasts):
    import random
    random.shuffle(cross_promo_podcasts)    
    return cross_promo_podcasts


print(shuffle_podcasts(cross_promo_podcasts))
