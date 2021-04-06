# coding:utf-8
import base64
from Crypto.Cipher import \
    AES  # 注：python3 安装 Crypto 是 pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome<br><br>


def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if (bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return:
    """
    try:
        length = len(text)
        unpadding = ord(text[length - 1])
        return text[0:length - unpadding]
    except Exception as e:
        pass


def aes_encode(key, content):
    """
    AES加密
    key,iv使用同一个
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    aes_encode_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    result = str(base64.b64encode(aes_encode_bytes), encoding='utf-8')
    return result


def aes_decode(key, content):
    """
    AES解密
     key,iv使用同一个
    模式cbc
    去填充pkcs7
    :param key:
    :param content:
    :return:
    """
    try:
        key_bytes = bytes(key, encoding='utf-8')
        iv = key_bytes
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        # base64解码
        aes_encode_bytes = base64.b64decode(content)
        # 解密
        aes_decode_bytes = cipher.decrypt(aes_encode_bytes)
        # 重新编码
        result = str(aes_decode_bytes, encoding='utf-8')
        # 去除填充内容
        result = pkcs7unpadding(result)
    except Exception as e:
        pass
    if result == None:
        return ""
    else:
        return result


key = '12345678g01234ab'

# 对英文加密
data = 'Hello!'
mi = aes_encode(key, data)
print(mi)
# 解密
print(aes_decode(key, mi))

# 中英文混合加密
data = 'Hello, 韩- 梅 -梅'
aes_encode_mixed = aes_encode(key, data)
print(aes_encode_mixed)
# 解密
print(aes_decode(key, aes_encode_mixed))