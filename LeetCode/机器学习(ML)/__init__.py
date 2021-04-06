# coding:utf-8
import base64
from Crypto.Cipher import AES
# 注：python3 安装 Crypto 是 pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome<br><br>


# 解密
def aes_decode(data, key):
    try:
        aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器
        decrypted_text = aes.decrypt(base64.decodebytes(bytes(data, encoding='utf8'))).decode("utf8")  # 解密
        decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]  # 去除多余补位
    except Exception as e:
        pass
    return decrypted_text


# 加密
def aes_encode(data, key):
    while len(data) % 16 != 0:  # 补足字符串长度为16的倍数
        data += (16 - len(data) % 16) * chr(16 - len(data) % 16)
    data = str.encode(data)
    # aes = AES.new(str.encode(key), AES.MODE_CBC)  # 初始化加密器
    aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器
    return str(base64.encodebytes(aes.encrypt(data)), encoding='utf8').replace('\n', '')  # 加密


if __name__ == '__main__':
    key = '12345678g01234ab'  # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    data = "E83A56F6BCF88E5BD3600C398E39EAAFA91DBA24807B73F7B76FF1E180CEA14DAED6A43F9304901044C50503198C2D3A57661"  # 待加密文本

    mi = aes_encode(data, key)
    print("加密值：", mi)
    print("解密值：", aes_decode(mi, key))