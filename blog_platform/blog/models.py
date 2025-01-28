from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Blog(models.Model):
    user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name="blog")
    title = models.CharField(max_length=255)  
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title



class BlogRating(models.Model):
    # Define rating choices
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # 1 to 5 ratings

    user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name="rating")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="ratings")  
    rating_value = models.PositiveIntegerField(choices=RATING_CHOICES, default=1)  
    
    def __str__(self):
        return f"Rating: {self.rating_value} by {self.user.username}"



class Comment(models.Model):
    user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name="comment")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")  # ForeignKey to Blog
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Comment by {self.user.username}"



class Like(models.Model):
    user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name="like")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="likes")  # ForeignKey to Blog
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for like

    def __str__(self):
        return f"Like by {self.user.username} on {self.blog.title}"
