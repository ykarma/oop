def main():
    from people.models import Blog
    blog = Blog()
    blog.name = 'blog1'
    blog.tagline = 'tagline1'
    blog.save()

if __name__ == '__main__':
    main()
    print('Done......')