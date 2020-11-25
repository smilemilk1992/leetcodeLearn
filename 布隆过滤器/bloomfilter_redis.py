# -*- coding: utf-8 -*-
from 布隆过滤器 import hash_function


class HashMap(object):
    def __init__(self, hash_function, hash_func_str):
        self.hash_function = hash_function
        self.hash_func_str = hash_func_str

    @classmethod
    def random_generator(cls, hash_value):
        return hash_value % (1 << 32)

    def hash(self, value):
        """
        Hash Algorithm
        :param value: Value
        :return: Hash Value
        """
        # 获得到hash函数对象
        hash_func = getattr(self.hash_function, self.hash_func_str)
        # 计算hash值
        hash_value = hash_func(value)
        # 将hash值映射到[0, 2^32]区间
        real_value = self.random_generator(hash_value)
        return real_value


class BloomFilter(object):
    def __init__(self,key,server):
        """
        Initialize BloomFilter
        :param server: Redis Server
        :param key: BloomFilter Key
        :param bit: m = 2 ^ bit
        """
        # default to 1 << 32 = 4294967296 = 2^32 = 1G, max filter 2^32/8 = 536870912 fingerprints
        self.hash_list = ["rs_hash", "js_hash", "pjw_hash", "elf_hash", "bkdr_hash",
                     "sdbm_hash", "djb_hash", "dek_hash","murmur3_hash"]
        self.key=key
        self.server = server
        self.maps = [HashMap(hash_function, hash_func_str) for hash_func_str in self.hash_list]

    def exists(self, value):
        """
        if value exists
        :param value:
        :return:
        """
        if not value:
            return False
        exist = True
        for map in self.maps:
            offset = map.hash(value)
            exist = exist & self.server.getbit(self.key, offset)
        return exist

    def insert(self, value):
        """
        add value to bloom
        :param value:
        :return:
        """
        for f in self.maps:
            offset = f.hash(value)
            self.server.setbit(self.key, offset, 1)


if __name__ == '__main__':
    import redis
    bl=BloomFilter(key="dd",server=redis.from_url("redis://127.0.0.1:6379"))
    for i in range(1000000):
        # bl.insert("https://github.com/wc-duck/pymmh3/blob/master/pymmh{}".format(i))
        print(bl.exists("https://github.com/wc-duck/pymmh3/blob/master/pymmh{}".format(i)))