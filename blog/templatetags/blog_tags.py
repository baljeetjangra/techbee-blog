from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
from django.shortcuts import get_object_or_404

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

@register.inclusion_tag('blog/post/feature_post.html')
def show_feature_post():
    feature_post = Post.published.latest()
    return {'feature_post':feature_post}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.simple_tag
def total_comments(id):
    post = get_object_or_404(Post,pk=id)
    comments = post.comments.filter(active=True)
    no_of_comments = comments.count()
    return no_of_comments