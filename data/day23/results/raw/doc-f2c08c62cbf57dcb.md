---
document_id: "doc-f2c08c62cbf57dcb"
source_name: "reference/glossary/shuffle-sharding.md"
source_type: "text"
source_format: "md"
source_sha256: "2f44160f6919b162efc09c017377f8c35b2788bb12fdbbaeb5b17d697c25b5cf"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/shuffle-sharding.md"
extracted_sha256: "2f44160f6919b162efc09c017377f8c35b2788bb12fdbbaeb5b17d697c25b5cf"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/shuffle-sharding.md"
---

---
title: Shuffle-sharding
id: shuffle-sharding
full_link:
short_description: >
  A technique for assigning requests to queues that provides better isolation than hashing modulo the number of queues.

aka:
tags:
- fundamental
---
A technique for assigning requests to queues that provides better isolation than hashing modulo the number of queues.

<!--more--> 

We are often concerned with insulating different flows of requests
from each other, so that a high-intensity flow does not crowd out low-intensity flows.
A simple way to put requests into queues is to hash some
characteristics of the request, modulo the number of queues, to get
the index of the queue to use. The hash function uses as input
characteristics of the request that align with flows. For example, in
the Internet this is often the 5-tuple of source and destination
address, protocol, and source and destination port.

That simple hash-based scheme has the property that any high-intensity flow
will crowd out all the low-intensity flows that hash to the same queue.
Providing good insulation for a large number of flows requires a large
number of queues, which is problematic. Shuffle-sharding is a more
nimble technique that can do a better job of insulating the low-intensity
flows from the high-intensity flows. The terminology of shuffle-sharding uses
the metaphor of dealing a hand from a deck of cards; each queue is a
metaphorical card. The shuffle-sharding technique starts with hashing
the flow-identifying characteristics of the request, to produce a hash
value with dozens or more of bits. Then the hash value is used as a
source of entropy to shuffle the deck and deal a hand of cards
(queues). All the dealt queues are examined, and the request is put
into one of the examined queues with the shortest length. With a
modest hand size, it does not cost much to examine all the dealt cards
and a given low-intensity flow has a good chance to dodge the effects of a
given high-intensity flow. With a large hand size it is expensive to examine
the dealt queues and more difficult for the low-intensity flows to dodge the
collective effects of a set of high-intensity flows. Thus, the hand size
should be chosen judiciously.
