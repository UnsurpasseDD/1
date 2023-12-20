#from news.models import User
# user1 = User.objects.create_user('Ganry Kavel')
#user2 = User.objects.create_user('Ludovico Einaudi')
#Author.objects.create(author = user1)
#Author.objects.create(author = user2)
#from news.models import Category
#Category.objects.create(_category = 'Sport') x4 Polit, Music, FOOD
#from news.models import Post
#Post.objects.create(post = author,
                   # post_category = 'A',
                    # tittle = 'RUN FOREST!',
                     #text = 'text')
Post.objects.create(post_author = author,
                   category = 'A',
                    title = 'Ludovico',
                   content = ' Its beautiful')
 Post.objects.create(post_author = author,
                    category = 'N',
                  title = 'Mc_donalds',
                    content = 'its 50/50..')
Post.objects.get(id=1).post_category.add(Category.objects.get(id=3))
Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=4))
Post.objects.get(id=3).post_category.add(Category.objects.get(id=2))
from news.models import Comment
Comment.objects.create( comment_post = Post.objects.get(id=1),
                        comment_user = Author.objects.get(id=1).author,
                        feedback_text = ' Maybe so good ')
Comment.objects.create( comment_post = Post.objects.get(id=2),
                        comment_user = Author.objects.get(id=2).author,
                        feedback_text = ' Maybe so good ')
Comment.objects.create( comment_post = Post.objects.get(id=3),
                        comment_user = Author.objects.get(id=2).author,
                        feedback_text = ' MARY CRISMAS ')
Comment.objects.create( comment_post = Post.objects.get(id=3),
                        comment_user = Author.objects.get(id=1).author,
                        feedback_text = ' MARY CRISMAS ')
Comment.objects.get(id=1).like()
Post.objects.get(id=1).dislike()
Post.objects.get(id=3).like()

u1 = Author.objects.get(id=1)
u1.update_rating()
u1.user_rate



s = Author.objects.order_by('user_rate')
for i in s:
    i.user_rate
    i.author.username
3
'Ganry Kavel'
4
'Ludovico Einaudi'


#p = Post.objects.order_by('-post_rate')
#for i in p[:1]:
#    i.date_created
#    i.post_author.author
#    i.post_rate
 #   i.title
 #   i.preview()



# Post.objects.all().order_by('-post_rate')[0].comment_set.values(
#'comment_date_created',
#'comment_user',
#'comment_rate', 'feedback_text'
#)