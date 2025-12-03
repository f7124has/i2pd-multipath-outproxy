def gen(index: int):
    return """[o{0}]
type=client
address=127.0.0.1
port={1}
destination=[CENSORED].b32.i2p
destinationport=1337
keys=transient-o{0}.dat
inbound.quantity=3
outbound.quantity=3
inbound.length=3
outbound.length=3
i2p.streaming.initialAckDelay=200
gzip=true
i2p.streaming.profile=2
i2p.streaming.maxWindowSize=768
crypto.ratchet.inboundTags=1600
""".format(index, 3000+index, index)

import random
for i in range(1, 33):
    print(gen(i))
