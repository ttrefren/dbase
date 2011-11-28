import random
import string
from doctyl.models import Topic, Article

class MockupGenerator(object):

    def __init__(self):
        self.passwords = {}
        self._created = []

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        for item in self._created:
            if getattr(item, 'id'):
                item.delete()

    def get_password(self, user):
        return self.passwords[user]

    def gen_string(self, length):
        random.seed()
        chars = string.letters + string.digits
        return ''.join([random.choice(chars) for i in xrange(length)])

    def gen_int(self, maximum=1000000000):
        random.seed()
        return int(random.random() * maximum)

    def create_topic(self):
        topic = Topic.objects.create(name=self.gen_string(10))
        self._created.append(topic)
        return topic

    def create_article(self, topic):
        article = Article.objects.create(topic=topic, name=self.gen_string(10), content=self.gen_string(100))
        self._created.append(article)
        return article


