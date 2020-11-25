from 布隆过滤器.mmu3hash import xrange, xencode


def rs_hash(key):
    a = 378551
    b = 63689
    hash_value = 0
    for i in range(len(key)):
        hash_value = hash_value * a + ord(key[i])
        a = a * b
    return hash_value


def js_hash(key):
    hash_value = 1315423911
    for i in range(len(key)):
        hash_value ^= ((hash_value << 5) + ord(key[i]) + (hash_value >> 2))
    return hash_value


def pjw_hash(key):
    bits_in_unsigned_int = 4 * 8
    three_quarters = (bits_in_unsigned_int * 3) / 4
    one_eighth = bits_in_unsigned_int / 8
    high_bits = 0xFFFFFFFF << int(bits_in_unsigned_int - one_eighth)
    hash_value = 0
    test = 0

    for i in range(len(key)):
        hash_value = (hash_value << int(one_eighth)) + ord(key[i])
        test = hash_value & high_bits
    if test != 0:
        hash_value = ((hash_value ^ (test >> int(three_quarters))) & (~high_bits))
    return hash_value & 0x7FFFFFFF


def elf_hash(key):
    hash_value = 0
    for i in range(len(key)):
        hash_value = (hash_value << 4) + ord(key[i])
        x = hash_value & 0xF0000000
        if x != 0:
            hash_value ^= (x >> 24)
        hash_value &= ~x
    return hash_value


def bkdr_hash(key):
    seed = 131  # 31 131 1313 13131 131313 etc..
    hash_value = 0
    for i in range(len(key)):
        hash_value = (hash_value * seed) + ord(key[i])
    return hash_value


def sdbm_hash(key):
    hash_value = 0
    for i in range(len(key)):
        hash_value = ord(key[i]) + (hash_value << 6) + (hash_value << 16) - hash_value;
    return hash_value


def djb_hash(key):
    hash_value = 5381
    for i in range(len(key)):
        hash_value = ((hash_value << 5) + hash_value) + ord(key[i])
    return hash_value


def dek_hash(key):
    hash_value = len(key);
    for i in range(len(key)):
        hash_value = ((hash_value << 5) ^ (hash_value >> 27)) ^ ord(key[i])
    return hash_value


def bp_hash(key):
    hash_value = 0
    for i in range(len(key)):
        hash_value = hash_value << 7 ^ ord(key[i])
    return hash_value


def fnv_hash(key):
    fnv_prime = 16777619
    hash_value = 2166136261
    for i in range(len(key)):
        hash_value *= fnv_prime
        hash_value ^= ord(key[i])
    return hash_value

def fnv1Hash64(self,key):#fnv-1 对短文还行,不敏感
    fnv_prime = 1099511628211
    hash_value = 14695981039346656037
    for i in range(len(key)):
        hash_value *= fnv_prime
        hash_value ^= ord(key[i])
    hash_value = bin(hash_value).replace('0b', '').zfill(64)[-64:]
    return hash_value

def fnv1aHash64(self,key):#fnv-1a 对短文本不友好，敏感
    fnv_prime = 1099511628211
    hash_value = 14695981039346656037
    for i in range(len(key)):
        hash_value ^= ord(key[i])
        hash_value *= fnv_prime
    hash_value = bin(hash_value).replace('0b', '').zfill(64)[-64:]
    return hash_value

def murmur3_hash(key, seed=0x9747b28c):
    ''' Implements 32bit murmur3 hash. '''
    key = bytearray(xencode(key))
    def fmix(h):
        h ^= h >> 16
        h = (h * 0x85ebca6b) & 0xFFFFFFFF
        h ^= h >> 13
        h = (h * 0xc2b2ae35) & 0xFFFFFFFF
        h ^= h >> 16
        return h
    length = len(key)
    nblocks = int(length / 4)
    h1 = seed
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    for block_start in xrange(0, nblocks * 4, 4):
        k1 = key[block_start + 3] << 24 | \
             key[block_start + 2] << 16 | \
             key[block_start + 1] << 8 | \
             key[block_start + 0]
        k1 = (c1 * k1) & 0xFFFFFFFF
        k1 = (k1 << 15 | k1 >> 17) & 0xFFFFFFFF  # inlined ROTL32
        k1 = (c2 * k1) & 0xFFFFFFFF
        h1 ^= k1
        h1 = (h1 << 13 | h1 >> 19) & 0xFFFFFFFF  # inlined ROTL32
        h1 = (h1 * 5 + 0xe6546b64) & 0xFFFFFFFF
    tail_index = nblocks * 4
    k1 = 0
    tail_size = length & 3
    if tail_size >= 3:
        k1 ^= key[tail_index + 2] << 16
    if tail_size >= 2:
        k1 ^= key[tail_index + 1] << 8
    if tail_size >= 1:
        k1 ^= key[tail_index + 0]
    if tail_size > 0:
        k1 = (k1 * c1) & 0xFFFFFFFF
        k1 = (k1 << 15 | k1 >> 17) & 0xFFFFFFFF  # inlined ROTL32
        k1 = (k1 * c2) & 0xFFFFFFFF
        h1 ^= k1
    unsigned_val = fmix(h1 ^ length)
    if unsigned_val & 0x80000000 == 0:
        return unsigned_val
    else:
        return -((unsigned_val ^ 0xFFFFFFFF) + 1)

def ap_hash(key):
    hash_value = 0xAAAAAAAA
    for i in range(len(key)):
        if (i & 1) == 0:
            hash_value ^= ((hash_value << 7) ^ ord(key[i]) * (hash_value >> 3))
        else:
            hash_value ^= (~((hash_value << 11) + ord(key[i]) ^ (hash_value >> 5)))
    return hash_value
