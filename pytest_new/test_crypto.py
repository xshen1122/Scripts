# coding: utf-8
from Crypto.PublicKey import RSA #加密库
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5, SHA256
import base64

def data_process(data):
    '''

    :param data: 字典
    :return:处理后的字符串
    '''
    if 'sign' in data:
        del data['sign']
    if 'sign_type' in data:
        del data['sign_type']
    pre_data = []
    for key in sorted(data): # 对字典的key进行排序
        if data[key]:
            pre_data.append('%s=%s' % (key,data[key]))
    final_data = '&'.join(pre_data).strip()
    return final_data


def hash_method(data,hash_type):
    if hash_type == 'MD5':
        return MD5.new(data.encode(encoding='utf-8'))
    elif hash_type == 'SHA256':
        digest = SHA256.new()
        digest.update(data.encode(encoding='utf-8'))
    else:
        print 'only support MD5 and SHA256'

def sign_RSA(data, private_key):
    '''

    :param data: 未加密数据
    :param private_key:第三方私钥
    :return:签名后的字段
    '''
    key=RSA.importKey(private_key)
    signer = PKCS1_v1_5.new(key)
    data = data_process(data)
    hash_obj = hash_method(data, SHA256)
    sign = signer.sign(hash_obj)
    signature = base64.b64encode(sign)
    return signature

def verify_RSA(data,publickey, sigature):
    '''

    :param data:明文数据
    :param publickey:服务器方公钥
    :param sigature:接收来自服务器方的签名字段
    :return:表明签验结果
    '''
    key = RSA.importKey(publickey)
    verifier = PKCS1_v1_5.new(key)
    hash_obj = hash_method(data,SHA256)
    return verifier.verify(hash_obj, base64.b64decode(sigature))