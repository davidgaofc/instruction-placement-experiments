import responses.post.trial1.test1 as post1
import responses.pre.trial1.test1 as pre1
import responses.intra.trial1.test1 as intra1

import responses.post.trial2.test1 as post2
import responses.pre.trial2.test1 as pre2
import responses.intra.trial2.test1 as intra2

import responses.post.trial3.test1 as post3
import responses.pre.trial3.test1 as pre3
import responses.intra.trial3.test1 as intra3

def main():

    print("Trial 1")

    print("post" + post1.test())

    print("pre" + pre1.test())

    print("intra" + intra1.test())

    print("Trial 2")

    print("post" + post2.test())

    print("pre" + pre2.test())

    print("intra" + intra2.test())

    print("Trial 3")

    print("post" + post3.test())

    print("pre" + pre3.test())

    print("intra" + intra3.test())

print("TEST FILE")
main()