from lxml import etree


class BaseSpider(object):

    def start(self):
        raise NotImplementedError("This method must be provided.")

    def get_selector(self, content):
        html = etree.HTML(content)
        return html
