topic= "1"
category = "travel"
tag_string = "12"
page_head = f'''---
        layout: single
        title:  "{topic}"
        categories: {category}
        tag: [{tag_string}]
        toc: false
        author_profile: false
        sidebar:
            nav: "counts"
        ---
        '''
print(page_head)

