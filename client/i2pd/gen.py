def gen(index: int):
    return """[o{0}]
type=client
address=127.0.0.1
port={1}
destination=[CENSORED].b32.i2p
destinationport=1337
keys=o{0}.dat # transient-
inbound.quantity=8
outbound.quantity=8
inbound.length=4
outbound.length=4
inbound.lengthVariance=-1
outbound.lengthVariance=-1
gzip=true
i2p.streaming.initialAckDelay=20
i2p.streaming.profile=2
i2p.streaming.maxWindowSize=768
i2p.streaming.answerPings=false
crypto.ratchet.inboundTags=2400
""".format(index, 3000+index, index)

import random
for i in range(1, 25):
    print(gen(i))
