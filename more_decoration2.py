def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)
    return wrapper


# @hello
# def foo():  #foo = hello(foo)
#     print("i am foo")
def foo():
    print("i am foo")
foo = hello(foo)#hello(foo)返回了wrapper()函数，所以，foo其实变成了wrapper的一个变量
foo() #foo()执行其实变成了wrapper()





#带参数的decrorator

def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) if "css_class" in kwds else ""

        def wrapped(*args, **kwds):
            return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"

        return wrapped

    return real_decorator


@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
@makeHtmlTag(tag="c", css_class="usa_css")
def hello(): #hello = makeHtmlTag(tag="b", css_class="bold_css")((makeHtmlTag(tag="i", css_class="italic_css")(hello))
    return "style"
print(hello())
