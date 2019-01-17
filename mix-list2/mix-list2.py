#!/usr/bin/env python3
proto = ['ssh','http','https']
print(proto)
print(proto[1])
proto.extend('dns')#this line will add 'd','n','s'to the end of the list
proto.append('dns')
print(proto)
proto2 = [22,80,443,53]
proto.extend(proto2)
print(proto)
proto.append(proto2)
print(proto2)