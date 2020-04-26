import uuid

# Returns a Universal Unique Identifier (32 Bits) as a <class 'uuid.UUID'> object
var = uuid.uuid4()
print var
print type(var)             # <class 'uuid.UUID'>
print str(var)
print len(str(var))

print var.hex               # 32-bit hex string
print var.int               # 128-bit integer
print var.urn               # Uniform Resource Name
# To have a "urn" prefix, it's optional

print var.variant
print var.version


# Converting the <class 'uuid.UUID'> object into "str" string by hex To make it usable
var2 = var.hex
print type(var2)
print len(var2)
